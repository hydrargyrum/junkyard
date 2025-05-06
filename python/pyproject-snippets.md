# `pyproject.toml` snippets

## Nicer syntax for defining authors/maintainers

```toml
[[project.authors]]
name = "Foo Bar"
email = "foo@example.com"
```

Rather than:

```toml
authors = [
    { name = "Foo Bar", email = "foo@example.com" },
]
```

## Install data in (for example) /usr/share with Hatch backend

```toml
[tool.hatch.build.targets.wheel.shared-data]
"foo/my.png" = "share/icons/128x128/my.png"

[tool.hatch.build.targets.sdist]
include = [
    "/foo/my.png",
]
```

`my.png` is under `foo/` in source repository (starting at `pyproject.toml`)

## Switch from setup.cfg to pyproject.toml easily

Keep `setup.cfg` as-is, and create this `pyproject.toml`:

```toml
[build-system]
requires = [
    "setuptools >= 48",
    "wheel >= 0.29.0",
]
build-backend = 'setuptools.build_meta'
```

## Entrypoints/plugins

- a module registers `externalinterface.subname` interfaces and will accept implementations plugins
- we package an implementation
    - its key for the external interface will be `custom_name`
    - the symbol to expose as a plugin can be obtained with `from implpackage.mymodule import Exposed`

```
[project.entry-points."externalinterface.subname"]
custom_name = "implpackage.mymodule:ExposedSymbol"
```

### Example for fsspec

```
[project.entry-points."fsspec.specs"]
my_fs = "mypackage:MyFS"
```
