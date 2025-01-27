# SQLAlchemy: query, execute and scalars

Suppose we have this entity:

```python
class Entity(SqlalchemyBase):
    id = mapped_column(Integer, primary_key=True)
    data = mapped_column(Integer)
```

`query()` is legacy (sqlalchemy v1.x) and has been replaced by `execute()` and `scalars()`.
But `query` is not strictly equivalent to `execute` or `scalars`, the return types are a bit different.

## When selecting a single entity class or a single column

|                                     | `Entity`       | `Entity.id` |
|-------------------------------------|----------------|-------------|
| `session.query(xxx).one()`          | `Entity`       | `tuple[int]`|
| `session.execute(select(xxx)).one()`| `tuple[Entity]`| `tuple[int]`|
| `session.scalars(select(xxx)).one()`| `Entity`       | `int`       |

With `all()`:

|                                     | `Entity`             | `Entity.id`       |
|-------------------------------------|----------------------|-------------------|
| `session.query(xxx).all()`          | `list[Entity]`       | `list[tuple[int]]`|
| `session.execute(select(xxx)).all()`| `list[tuple[Entity]]`| `list[tuple[int]]`|
| `session.scalars(select(xxx)).all()`| `list[Entity]`       | `list[int]`       |


## When selecting multiple columns or entity classes

For example, `select(Entity.id, Entity.data)`

- `query()` behaves like `execute()`: both return tuples
- `scalars()` return only the first selected column and ignores the other columns (`scalars()` should not be used then)

## See also

[SQLAlchemy various selects, as a code example](sqlalchemy-various-select.py)
