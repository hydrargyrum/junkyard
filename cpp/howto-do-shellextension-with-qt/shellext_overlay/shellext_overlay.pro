# -------------------------------------------------
# Project created by QtCreator 2010-06-29T13:55:54
# -------------------------------------------------
QT -= gui

# ##
CONFIG += dll \
    qaxserver \
    qt
LIBS += -luser32     -lole32     -loleaut32     -lgdi32     -luuid
#LIBS +=

# qaxserver.def and qaxserver.rc come from <qt>\src\activeqt\control
DEF_FILE = qaxserver.def
RC_FILE = qaxserver.rc

# ##
TARGET = shellext_overlay
TEMPLATE = lib
DEFINES += SHELLEXT_OVERLAY_LIBRARY
SOURCES += shelloverlay.cpp \
    dllmain.cpp
HEADERS += shelloverlay.h \
    shellext_overlay_global.h
OTHER_FILES += qaxserver.rc \
    qaxserver.def \
    qtdemo.ico
