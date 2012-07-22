%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

# Last updated for version 2.29.1
# The order here corresponds to that in configure.ac,
# for easier comparison.  Please do not alphabetize.
%define pygtk_version                   2.10.3
%define glib_version                    2.6.0
%define gtk_version                     2.4.0
%define python_mate_version             1.1.0
%define mate_panel_version              1.1.0
%define gtksourceview_version           1.8.5-2
%define libmatewnck_version             1.3.0
%define libgtop_version                 2.13.0
%define mate_media_version              1.1.0
%define mate_conf_version               1.1.0
%define marco_version                   1.1.0
%define librsvg2_version                2.13.93
%define mate_keyring_version            1.1.0
%define mate_desktop_version            1.1.0

### Abstract ###

Name: 		python-mate-desktop
Version: 	1.4.0
Release: 	1%{?dist}
License: 	GPLv2+
Group: 		Development/Languages
Summary: 	The sources for additional PyMATE Python extension modules
URL: 		http://mate-desktop.org
Source: 	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

Patch0: 	python-mate-desktop_change-directories.patch
Patch1: 	python-mate-desktop_mediaprofiles.patch

### Dependencies ###

Requires: python-mate-canvas >= %{python_mate_version}

### Build Dependencies ###

BuildRequires: glib2-devel >= %{glib_version}
BuildRequires: mate-conf-devel >= %{mate_conf_version}
BuildRequires: mate-desktop-devel >= %{mate_desktop_version}
BuildRequires: mate-keyring-devel >= %{mate_keyring_version}
BuildRequires: mate-panel-devel >= %{mate_panel_version}
BuildRequires: python-mate-matecomponent >= %{python_mate_version}
BuildRequires: python-mate-canvas >= %{python_mate_version}
BuildRequires: python-mate-devel >= %{python_mate_version}
BuildRequires: python-mate-mateconf >= %{python_mate_version}
BuildRequires: gtk2-devel >= %{gtk_version}
BuildRequires: libmateui-devel
BuildRequires: libgtop2-devel >= %{libgtop_version}
BuildRequires: librsvg2-devel >= %{librsvg2_version}
BuildRequires: libmatewnck-devel >= %{libmatewnck_version}
BuildRequires: marco-devel >= %{marco_version}
BuildRequires: pygtk2-devel >= %{pygtk_version}
BuildRequires: python-devel
BuildRequires: autoconf, automake, libtool
BuildRequires: mate-common
BuildRequires: dbus-glib-devel
BuildRequires: dbus-devel
BuildRequires: openssl-devel
BuildRequires: libgcrypt-devel
BuildRequires: avahi-glib-devel
BuildRequires: libselinux-devel
BuildRequires: mate-media-devel
BuildRequires: atril-devel

Obsoletes: 		mate-python2-desktop
Obsoletes: 		python-mate-evolution
Provides:  		python-mate-desktop

%description
The mate-python-desktop package contains the source packages for additional 
Python bindings for MATE. It should be used together with mate-python.

%package -n python-mate-applet
Summary: Python bindings for MATE Panel applets.
License: LGPLv2
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
# applets from GNOME 1.4 are no longer supported - we only have 1 panel
Obsoletes: pymate-applet <= 1.4.2
Requires: python-mate-matecomponent
Requires: python-mate-mate

Obsoletes: 		mate-python2-applet
Provides:  		python-mate-applet

%description -n python-mate-applet
This module contains a wrapper that allows MATE Panel applets to be
written in Python.

%package -n python-mate-atril
Summary: Python bindings for interacting with atril
License: LGPLv2
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: atril-libs >= %{atril_version}

%description -n python-mate-atril
This module contains a wrapper that allows the use of atril via Python.

#%package -n python-mate-gnomeprint
#Summary: Python bindings for interacting with libgnomeprint
#License: LGPLv2
#Group: Development/Languages
#Requires: %{name} = %{version}-%{release}
#Requires: libgnomeprint22
#Requires: libgnomeprintui22
#Requires: gnome-python2-canvas

#%description -n gnome-python2-gnomeprint
#This module contains a wrapper that allows the use of libgnomeprint via
#Python.

#%package -n python-mate-gtksourceview
#Summary: Python bindings for interacting with the gtksourceview library 
#License: GPLv2+
#Group: Development/Languages
#Requires: %{name} = %{version}-%{release}
#Requires: gtksourceview >= %{gtksourceview_version}
#Requires: gnome-python2-gnomeprint

#%description -n python-mate-gtksourceview
#This module contains a wrapper that allows the use of gtksourceview via
#Python.

%package -n python-mate-libmatewnck
Summary: Python bindings for interacting with libwnck
License: LGPLv2
Group: Development/Languages
Requires: libwnck >= %{libwnck_version}

Obsoletes: 		python-mate-libwnck
Provides:  		python-mate-libmatewnck

%description -n python-mate-libmatewnck
This module contains a wrapper that allows the use of libwnck via
Python.

%package -n python-mate-libgtop2
Summary: Python bindings for interacting with libgtop
License: GPLv2+
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: libgtop2 >= %{libgtop_version}

Obsoletes: 		mate-python2-libgtop2
Provides:  		python-mate-libgtop2

%description -n python-mate-libgtop2
This module contains a wrapper that allows the use of libgtop via
Python.

%package -n python-mate-marco
Summary: Python bindings for interacting with marco
License: GPLv2
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: marco >= %{marco_version}

Obsoletes: 		mate-python2-marco
Provides:  		python-mate-marco

%description -n python-mate-marco
This module contains a wrapper that allows the use of marco
via Python.

#%package -n gnome-python2-totem
#Summary: Python bindings for interacting with totem
#License: LGPLv2
#Group: Development/Languages
#Requires: %{name} = %{version}-%{release}
#Requires: totem-pl-parser >= %{totem_version}
#Requires: gnome-python2-gconf

#%description -n gnome-python2-totem
#This module contains a wrapper that allows the use of totem
#via Python.

%package -n python-mate-rsvg
Summary: Python bindings for interacting with librsvg
License: LGPLv2
Group: Development/Languages
Requires: librsvg2 >= %{librsvg2_version}

Obsoletes: 		mate-python2-rsvg
Provides:  		python-mate-rsvg

%description -n python-mate-rsvg
This module contains a wrapper that allows the use of librsvg
via Python.

%package -n python-mate-matedesktop
Summary: Python bindings for interacting with mate-desktop
License: LGPLv2
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: mate-desktop >= %{mate_desktop_version}

Obsoletes: 		mate-python2-matedesktop
Provides:  		python-mate-matedesktop

%description -n python-mate-matedesktop
This module contains a wrapper that allows the use of mate-desktop
via Python.

%package -n python-mate-matekeyring
Summary: Python bindings for interacting with mate-keyring
License: LGPLv2
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: mate-keyring >= %{mate_keyring_version}

Obsoletes: 		mate-python2-matekeyring
Provides:  		python-mate-matekeyring

%description -n python-mate-matekeyring
This module contains a wrapper that allows the use of mate-keyring
via Python.

%package -n python-mate-mediaprofiles
Summary: Python bindings for interacting with mate-keyring
License: LGPLv2
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: mate-media-libs >= %{mate_media_version}

%description -n python-mate-mediaprofiles
This module contains a wrapper that allows the use of mate-media-profiles
via Python.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .python-mate-desktop_change-directories
%patch1 -p1 -b .python-mate-desktop_mediaprofiles.patch
NOCONFIGURE=1 ./autogen.sh

%build
%configure \
	--disable-static\
	--enable-marco \
	--enable-applet \
	--enable-matekeyring \
 	--enable-matedesktop \
	--enable-atril \
	--enable-rsvg \
	--enable-gtop \
	--enable-matewnck \
	--enable-mediaprofiles

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

#find $RPM_BUILD_ROOT -name '*.la' -exec rm {} \;

rm -rf $RPM_BUILD_ROOT/%{_libdir}/python*/site-packages/gtk-2.0/gksu
rm -rf $RPM_BUILD_ROOT/%{_libdir}/python*/site-packages/gtk-2.0/bugbuddy.*

%files
%defattr(-,root,root,-)
%doc AUTHORS NEWS README COPYING COPYING.GPL COPYING.LGPL
%{_libdir}/pkgconfig/mate-python-desktop-2.0.pc
%{_datadir}/pygtk

%files -n python-mate-applet
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/mate/applet.*
%{python_sitearch}/gtk-2.0/mateapplet.so
%{python_sitearch}/gtk-2.0/mateapplet.la

%files -n python-mate-atril
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/atril.so
%{python_sitearch}/gtk-2.0/atril.la

#%files -n gnome-python2-gnomeprint
#%defattr(-,root,root,-)
#%{python_sitearch}/gtk-2.0/gnomeprint/
#%{_datadir}/gtk-doc/html/pygnomeprint
#%{_datadir}/gtk-doc/html/pygnomeprintui
#%defattr(644,root,root,755)
#%doc ../gnome-python-desktop-%{version}/examples/gnomeprint/*

#%files -n python-mate-gtksourceview
#%defattr(-,root,root,-)
#%{python_sitearch}/gtk-2.0/gtksourceview.so
#%{_datadir}/gtk-doc/html/pygtksourceview
#%defattr(644,root,root,755)
#%doc ../gnome-python-desktop-%{version}/examples/gtksourceview/*

%files -n python-mate-libmatewnck
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/matewnck.so
%{python_sitearch}/gtk-2.0/matewnck.la

%files -n python-mate-libgtop2
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/mate/gtop.so
%{python_sitearch}/gtk-2.0/mate/gtop.la

%files -n python-mate-marco
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/marco.so
%{python_sitearch}/gtk-2.0/marco.la

#%files -n gnome-python2-totem
#%defattr(-,root,root,-)
#%ifnarch s390 s390x
#%{python_sitearch}/gtk-2.0/mediaprofiles.so
#%endif
#%{python_sitearch}/gtk-2.0/totem

%files -n python-mate-rsvg
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/mate/rsvg.so
%{python_sitearch}/gtk-2.0/mate/rsvg.la

%files -n python-mate-matedesktop
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/matedesktop

%files -n python-mate-matekeyring
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/matekeyring.so
%{python_sitearch}/gtk-2.0/matekeyring.la

%files -n python-mate-mediaprofiles
%defattr(-,root,root,-)
%{python_sitearch}/gtk-2.0/mediaprofiles.so
%{python_sitearch}/gtk-2.0/mediaprofiles.la

%changelog
* Tue Jul 17 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.4.0-1
- update to 1.4.0

* Sat Jun 09 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.3.0-2
- test build

* Sat Jun 09 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.3.0-1
- update to 1.3.0
- switch to libmatewnck

* Tue Apr 12 2012 Wolfgang Ulbrich <chat-to@raveit.de> - 1.2.0-3
- rename mate-python2-desktop to python-mate-desktop

* Fri Mar 09 2012 Wolfgang Ulbrich <chat-to@raveit.de> - 1.2.0-1
- update to 1.2.0

* Fri Mar 09 2012 Wolfgang Ulbrich <chat-to@raveit.de> - 1.1.0-5
- test build

* Mon Feb 20 2012 Wolfgang Ulbrich <chat-to@raveit.de> - 1.1.0-4
- rebuild for enable builds for .i686
- move some directories to avoid conflicts with gnome-python2-desktop
- change %{_datadir} back

* Tue Feb 09 2012 Wolfgang Ulbrich <chat-to@raveit.de> - 1.1.0-3
- rebuild for pymatecorba-1.1.0-2

* Wed Jan 04 2012 Wolfgang Ulbrich <chat-to@raveit.de> - 1.1.0-2
- change %{_datadir} from /usr/share to /usr/share/mate-defs to avoid conflicts
- with gnome-python2-desktop

* Wed Jan 04 2012 Wolfgang Ulbrich <chat-to@raveit.de> - 1.1.0-1
- mate-python2-desktop.spec based on ggnome-python2-desktop-2.32.0-3.fc14 spec

* Tue Feb  7 2011 Daniel Drake <dsd@laptop.org> - 2.32.0-3
- Fix applying of patch from 2.6.32.0-2

