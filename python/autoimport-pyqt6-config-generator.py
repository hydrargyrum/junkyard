#!/usr/bin/env python3
# SPDX-License-Identifier: WTFPL

# autoimport <https://lyz-code.github.io/autoimport/> is a tool for
# automatically adding missing imports in python source code.
# autoimport-pyqt6-config-generator.py generates autoimport config
# so it can find PyQt6 imports.

# typical usage:
# 	autoimport-pyqt6-config-generator.py > ~/.autoimport.toml
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
try_import_add("PyQt6.QtCore")
try_import_add("PyQt6.QtGui")
try_import_add("PyQt6.QtWidgets")
try_import_add("PyQt6.Qsci")
try_import_add("PyQt6.QtBluetooth")
try_import_add("PyQt6.QtCharts")
try_import_add("PyQt6.QtDBus")
try_import_add("PyQt6.QtDesigner")
try_import_add("PyQt6.QtHelp")
try_import_add("PyQt6.QtMultimedia")
try_import_add("PyQt6.QtMultimediaWidgets")
try_import_add("PyQt6.QtNetwork")
try_import_add("PyQt6.QtOpenGL")
try_import_add("PyQt6.QtOpenGLWidgets")
try_import_add("PyQt6.QtPositioning")
try_import_add("PyQt6.QtPrintSupport")
try_import_add("PyQt6.QtQml")
try_import_add("PyQt6.QtQuick")
try_import_add("PyQt6.QtQuick3D")
try_import_add("PyQt6.QtQuickWidgets")
try_import_add("PyQt6.QtRemoteObjects")
try_import_add("PyQt6.QtSensors")
try_import_add("PyQt6.QtSerialPort")
try_import_add("PyQt6.QtSpatialAudio")
try_import_add("PyQt6.QtSql")
try_import_add("PyQt6.QtSvg")
try_import_add("PyQt6.QtSvgWidgets")
try_import_add("PyQt6.QtWebChannel")
try_import_add("PyQt6.QtWebEngineCore")
try_import_add("PyQt6.QtWebEngineWidgets")
try_import_add("PyQt6.QtWebSockets")
try_import_add("PyQt6.QtXml")

if not modules:
	raise AssertionError("No PyQt6 modules could be loaded, is it installed?")


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
