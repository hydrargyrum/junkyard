
import inspect

from pydantic import BaseModel


def deserialize_params(func):
    """Decorator which unpacks dict to pydantic objects using param type hints

        class SomePydanticModel(BaseModel):
            some_attr: int

        @deserialize_params
        def my_func(foo: SomePydanticModel):
            print(foo.some_attr)

        my_func(SomePydanticModel(some_attr=1).dict())

    When calling my_func with a serialized (to dict) pydantic object param, my_func will actually
    receive the deserialized object as param.
    """
    sig = inspect.signature(func)

    for parameter in sig.parameters.values():
        if parameter.kind & (parameter.VAR_POSITIONAL | parameter.VAR_KEYWORD):
            raise NotImplementedError("deserialize_params does not support yet variadic args")

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)

        new_posits = []
        for posit, parameter in zip(args, sig.parameters.values()):
            old_value = bound.arguments[parameter.name]
            if (
                not isinstance(old_value, BaseModel)
                and isinstance(parameter.annotation, type)
                and issubclass(parameter.annotation, BaseModel)
            ):
                new_posits.append(parameter.annotation(**old_value))
            else:
                new_posits.append(old_value)

        for kwarg_name in kwargs:
            parameter = sig.parameters[kwarg_name]
            old_value = bound.arguments[kwarg_name]
            if (
                not isinstance(old_value, BaseModel)
                and isinstance(parameter.annotation, type)
                and issubclass(parameter.annotation, BaseModel)
            ):
                kwargs[kwarg_name] = parameter.annotation(**old_value)

        return func(*new_posits, **kwargs)

    return wrapper
