Name:       connman-qt5
Summary:    Qt bindings for connman
Version:    1.3.1
Release:    1
License:    ASL 2.0
URL:        https://github.com/sailfishos/libconnman-qt/
Source0:    %{name}-%{version}.tar.bz2
Requires:   connman >= 1.32+git191
Requires:   libdbusaccess >= 1.0.4
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libdbusaccess) >= 1.0.4

%{!?qtc_qmake6:%define qtc_qmake6 %qmake6}
%{!?qtc_make:%define qtc_make make}


%description
This is a library for working with connman using Qt


%package declarative
Summary:    Declarative plugin for Qt Quick for connman-qt
Requires:   %{name} = %{version}-%{release}
Requires:   connman-qt6

%description declarative
This package contains the files necessary to develop
applications using libconnman-qt


%package devel
Summary:    Development files for connman-qt
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the files necessary to develop
applications using libconnman-qt


%prep
%setup -q -n %{name}-%{version}

%build
%qtc_qmake6 -r VERSION=%{version}
%qtc_make %{?_smp_mflags}

%install
%qmake6_install
# MeeGo.Connman legacy import
mkdir -p %{buildroot}%{_libdir}/qt6/qml/MeeGo/Connman
ln -sf ../../Connman/libConnmanQtDeclarative.so %{buildroot}%{_libdir}/qt6/qml/MeeGo/Connman/
sed 's/module Connman/module MeeGo.Connman/' < plugin/qmldir > %{buildroot}%{_libdir}/qt6/qml/MeeGo/Connman/qmldir

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libconnman-qt6.so.*

%files declarative
%defattr(-,root,root,-)
%{_libdir}/qt6/qml/Connman
%{_libdir}/qt6/qml/MeeGo/Connman

%files devel
%defattr(-,root,root,-)
%{_includedir}/connman-qt6
%{_libdir}/pkgconfig/connman-qt6.pc
%{_libdir}/libconnman-qt6.prl
%{_libdir}/libconnman-qt6.so
