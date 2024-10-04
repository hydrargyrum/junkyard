#!/usr/bin/env python3
# imports
from sqlalchemy import Column, Integer, String
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import select


# model declaration
Base = declarative_base()


class Entity(Base):
    __tablename__ = "entity"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Integer)


# start an in-memory sqlite database
engine = create_engine("sqlite://")
engine = engine.execution_options(isolation_level="AUTOCOMMIT")

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# --- create tables
Base.metadata.create_all(engine)

# --- add a few entities
session.add(Entity(name="foo", value=42))
session.add(Entity(name="bar", value=53))

# --- fetching elements
# execute() returns a lazy iterator
for row in session.execute(select(Entity)):
    # row is a tuple[Entity]
    print(row[0].name)

# execute().all() fetches everything and returns a list
for row in session.execute(select(Entity)).all():
    # row is a tuple[Entity]
    print(row[0].name)

# expanding the tuple directly
for (obj,) in session.execute(select(Entity)):
    # (obj,) is a tuple[Entity], so obj is an Entity
    print(obj.name)

for row in session.execute(select(Entity.name, Entity.value)):
    # row is a tuple[str, int]
    print(f"name = {row[0]}, value = {row[1]}")
    # but row also has field names, extracted from the select, best-effort
    # like a https://docs.python.org/3/library/collections.html#collections.namedtuple
    print(f"name = {row.name}, value = {row.value}")

# extracting the tuple directly
for name, value in session.execute(select(Entity.name, Entity.value)):
    print(f"name = {name}, value = {value}")

for obj in session.scalars(select(Entity)):
    # scalars extracts the first element of the tuple
    # typically if there's only one param to select()
    print(obj.name)

# ---
# getting the first element
(obj,) = session.execute(select(Entity)).first()
obj = session.scalars(select(Entity)).first()

# fetching a lone element
obj = session.scalars(select(Entity).where(Entity.id == 1)).one_or_none()
if obj is None:
    print("entity not found")
else:
    print(f"name = {obj.name}")

# will raise an exception if no row is returned (or more than one row)
obj = session.scalars(select(Entity).where(Entity.id == 1)).one()
