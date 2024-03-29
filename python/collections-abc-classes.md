# diagram showing `collections.abc` classes with abstract methods and mixins

```mermaid
classDiagram
    Container <|-- Sequence
    Iterable <|-- Iterator
    Iterable <|-- Reversible
    Iterator <|-- Generator
    Sized <|-- Collection
    Iterable <|-- Collection
    Container <|-- Collection
    Reversible <|-- Sequence
    Collection <|-- Sequence
    Sequence <|-- MutableSequence
    Collection <|-- Set
    Collection <|-- Mapping
    Mapping <|-- MutableMapping
    Set <|-- MutableSet

    class Iterable {
        - __iter__()*
    }

    class Iterator {
        - __next__()*
        + __iter__()
    }

    class Container {
        - __contains__(value)*
    }

    class Sequence {
        - __getitem__(item)*
        - __len__()*
        + __contains__(value)
        + __iter__()
        + __reversed__()
        + index(value)
        + count(value)
    }

    class Reversible {
        - __reversed__()*
    }

    class Generator {
        - send(value)*
        - throw(value)*
        + close()
        + __iter__()
        + __next__()
    }

    class Sized {
        - __len__()*
    }

    class Collection {
        - __contains__(value)*
        - __iter__()*
        - __len__()*
    }

    class MutableSequence {
        - __getitem__(item)*
        - __setitem__(item, value)*
        - __delitem__(item)*
        - __len__()*
        - insert(index, value)*
        + append(value)
        + reverse()
        + extend(value)
        + pop(index)
        + remove(value)
        + __iadd__(other)
    }

    class Set {
        - __contains__(value)*
        - __iter__()*
        - __len__()*
        + __le__(other)
        + __lt__(other)
        + __eq__(other)
        + __ne__(other)
        + __gt__(other)
        + __ge__(other)
        + __and__(other)
        + __or__(other)
        + __sub__(other)
        + __xor__(other)
        + isdisjoint(other)
    }

    class MutableSet {
        - __contains__(value)*
        - __iter__()*
        - __len__()*
        - add(value)*
        - discard(value)*
        + clear()
        + pop(value)
        + remove(value)
        + __ior__(other)
        + __iand__(other)
        + __ixor__(other)
        + __isub__(other)
    }

    class Mapping {
        - __getitem__(item)*
        - __iter__()*
        - __len__()*
        + __contains__(value)
        + keys()
        + items()
        + values()
        + get(value, default)
        + __eq__(other)
        + __ne__(other)
    }

    class MutableMapping {
        - __getitem__(item)*
        - __setitem__(item, value)*
        - __delitem__(item)*
        - __iter__()*
        - __len__()*
        + pop(value)
        + popitem(value)
        + clear()
        + update(*, **)
        + setdefault(item, value)
    }
```

Uses [Mermaid](https://mermaid.js.org/) for rendering
