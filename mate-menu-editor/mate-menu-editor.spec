%define libxml2_version 2.4.12
%define mate_corba_version 1.1.0
%define glib2_version 2.25.9
%define dbus_version 1.0.1
%define dbus_glib_version 0.74

Summary: 	A process-transparent configuration system
Name: 		mate-menu-editor
Version:	1.5.0
Release: 	1%{?dist}
License:	LGPLv2+
Group: 		System Environment/Base
URL: 		http://pub.mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

#BuildRequires: libxml2-devel >= %{libxml2_version}
#BuildRequires: libxslt-devel
#BuildRequires: mate-corba-devel >= %{mate_corba_version}
#BuildRequires: glib2-devel >= %{glib2_version}
#BuildRequires: gtk-doc >= 0.9
#BuildRequires: pkgconfig >= 0.14
#BuildRequires: gettext
#BuildRequires: openldap-devel
BuildRequires: intltool
#BuildRequires: polkit-devel >= 0.92
#BuildRequires: dbus-glib-devel >= 0.8
#BuildRequires: gobject-introspection-devel >= 0.6.7
BuildRequires: autoconf automake libtool
#BuildRequires: mate-doc-common
BuildRequires: mate-menus-devel
#BuildRequires: gtk2-devel
Requires: dbus


%description
mate-conf is a process-transparent configuration database API used to
store user preferences. It has pluggable backends and features to
support workgroup administration.

%prep
%setup -q -n mate-menu-editor-%{version}
NOCONFIGURE=1 ./autogen.sh

%build
%configure \

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/mateconf/schemas
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/mateconf/mateconf.xml.system
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm/
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/rpm-state/mateconf
mkdir -p $RPM_BUILD_ROOT%{_datadir}/MateConf/matesettings

install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/rpm/


%find_lang %{name}

%post
/sbin/ldconfig

if [ $1 -gt 1 ]; then
    if ! fgrep -q mateconf.xml.system %{_sysconfdir}/mateconf/2/path; then
        sed -i -e 's@xml:readwrite:$(HOME)/.mateconf@&\n\n# Location for system-wide settings.\nxml:readonly:/etc/mateconf/mateconf.xml.system@' %{_sysconfdir}/mateconf/2/path
    fi
fi

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root)
%doc COPYING NEWS README backends/README.evoldap
%config(noreplace) %{_sysconfdir}/mateconf/2/path
%config(noreplace) %{_sysconfdir}/mateconf/2/evoldap.conf
%dir %{_sysconfdir}/mateconf
%dir %{_sysconfdir}/mateconf/2
%dir %{_sysconfdir}/mateconf/mateconf.xml.defaults
%dir %{_sysconfdir}/mateconf/mateconf.xml.mandatory
%dir %{_sysconfdir}/mateconf/mateconf.xml.system
%dir %{_sysconfdir}/mateconf/schemas
%{_bindir}/mateconf-merge-tree
%{_bindir}/mateconftool-2
%{_libexecdir}/mateconfd-2
%{_libdir}/*.so.*
%{_libdir}/MateConf/2/*.so
%dir %{_datadir}/sgml
%{_datadir}/sgml/mateconf
%{_datadir}/MateConf
%{_mandir}/man1/*
%dir %{_libdir}/MateConf
%dir %{_libdir}/MateConf/2
%{_sysconfdir}/dbus-1/system.d/org.mate.MateConf.Defaults.conf
%{_libexecdir}/mateconf-defaults-mechanism
%{_datadir}/polkit-1/actions/org.mate.mateconf.defaults.policy
%{_datadir}/dbus-1/system-services/org.mate.MateConf.Defaults.service
%{_datadir}/dbus-1/services/org.mate.MateConf.service
%dir %{_localstatedir}/lib/rpm-state/
%{_localstatedir}/lib/rpm-state/mateconf/
%{_libdir}/girepository-1.0
%{_libdir}/MateConf/2/libmateconfbackend-evoldap.la
%{_libdir}/MateConf/2/libmateconfbackend-oldxml.la
%{_libdir}/MateConf/2/libmateconfbackend-xml.la
%{_libdir}/libmateconf-2.la
%{_sysconfdir}/rpm/macros.mateconf
%{_sysconfdir}/xdg/autostart/mateconf-gsettings-data-convert.desktop
%{_bindir}/mateconf-gsettings-data-convert
%{_bindir}/mateconf-gsettings-schema-convert
%{_libdir}/gio/modules/libgsettingsmateconfbackend.la
%{_libdir}/gio/modules/libgsettingsmateconfbackend.so

%changelog
* Thu Jul 05 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.4.0-1
- update to 1.4.0

* Sun Jul 01 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.2.1-2
- enable gsettings-backend

* Thu Mar 01 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.2.1-1
-update verion to 1.2

* Fri Feb 17 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.1.0-3
- rebuild for enable builds for .i686

* Wed Feb 08 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.1.0-2
- added patches from fedora GConf2-2.32.4-1.fc16


* Sun Dec 25 2011 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.1.0-1
- mate-conf.spec based on GConf2-2.32.4-1.fc16 spec

* Fri Jun 17 2011 Tomas Bzatek <tbzatek@redhat.com> - 2.32.4-1
- Update to 2.32.4

