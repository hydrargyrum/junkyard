#!/usr/bin/env python3
# SPDX-License-Identifier: WTFPL

# autoimport <https://lyz-code.github.io/autoimport/> is a tool for
# automatically adding missing imports in python source code.
# autoimport-pyqt5-config-generator.py generates autoimport config
# so it can find PyQt5 imports.

# typical usage:
# 	autoimport-pyqt5-config-generator.py > ~/.autoimport.toml
# 	autoimport --config-file ~/.autoimport.toml myfile.py

from importlib import import_module
import sys


# not all PyQt modules may be installed
# don't crash the generator if some of them are not installed
# just skip them
def try_import_add(module_name):
	try:
		module = import_module(module_name)
	except ModuleNotFoundError:
		print(f"not found {module_name}", file=sys.stderr)
	else:
		modules.append(module)


modules = []
try_import_add("PyQt5.QtCore")
try_import_add("PyQt5.QtGui")
try_import_add("PyQt5.QtWidgets")
try_import_add("PyQt5.Qsci")
try_import_add("PyQt5.QtDBus")
try_import_add("PyQt5.QtDesigner")
try_import_add("PyQt5.QtHelp")
try_import_add("PyQt5.QtLocation")
try_import_add("PyQt5.QtMultimedia")
try_import_add("PyQt5.QtMultimediaWidgets")
try_import_add("PyQt5.QtNetwork")
try_import_add("PyQt5.QtPrintSupport")
try_import_add("PyQt5.QtSql")
try_import_add("PyQt5.QtSvg")
try_import_add("PyQt5.QtWebChannel")
try_import_add("PyQt5.QtWebEngine")
try_import_add("PyQt5.QtWebEngineCore")
try_import_add("PyQt5.QtWebEngineWidgets")
try_import_add("PyQt5.QtWebKit")
try_import_add("PyQt5.QtWebKitWidgets")
try_import_add("PyQt5.QtWebSockets")
try_import_add("PyQt5.QtXml")
try_import_add("PyQt5.QtXmlPatterns")

if not modules:
	raise AssertionError("No PyQt5 modules could be loaded, is it installed?")


# use a dict to avoid duplicates
imports = {}

for module in modules:
	for symbol in dir(module):
		if symbol.startswith("_"):
			# internal symbols not meant to be imported
			continue
		# use setdefault() so prior modules are not overridden
		imports.setdefault(symbol, module.__name__)

# output autoimport TOML
print("[common_statements]")
for symbol, module_name in imports.items():
	print(f'"{symbol}" = "from {module_name} import {symbol}"')
