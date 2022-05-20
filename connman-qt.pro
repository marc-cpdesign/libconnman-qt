TEMPLATE = subdirs
SUBDIRS += libconnman-qt

# Qt6 requires c++17
greaterThan(QT_MAJOR_VERSION, 5): CONFIG += c++17

# Adds 'coverage' target
include(coverage.pri)
# CONFIG flag to disable qml plugin
!noplugin {
    SUBDIRS += plugin
    libconnman-qt.target = lib-target
    plugin.depends = lib-target
}
example {
   SUBDIRS += examples/counters
}

OTHER_FILES += rpm/connman-qt5.spec
