Name:           caja-image-converter
Version:        1.4.0
Release:        1%{?dist}
Summary:        Caja extension to mass resize images

Group:          User Interface/Desktops
License:        GPLv2+
URL:			http://pub.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libglade2-devel >= 2.4.0
BuildRequires:	glib2-devel >= 2.15.0
BuildRequires:	caja-devel >= 1.1.0
BuildRequires:	gettext
BuildRequires:	perl(XML::Parser)
BuildRequires:  mate-common
BuildRequires:  intltool
Requires:		ImageMagick
 

%description
Adds a "Resize Images..." menu item to the context menu of all images. This
opens a dialog where you set the desired image size and file name. A click
on "Resize" finally resizes the image(s) using ImageMagick's convert tool.


%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure \
	--disable-static

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_datadir}/%{name}/
%{_libdir}/caja/extensions-2.0/*.so


%changelog
* Tue Jul 17 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.4.0-1
- update to 1.4.0

* Thu Mar 15 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.2.0-1
- update to 1.2.0

* Mon Feb 13 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - caja-image-converter-1.1.0-2
- rebuild for enable builds for .i686

* Wed Jan 04 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - caja-image-converter-1.1.0-1
- caja-image-converter.spec based on nautilus-image-converter-0.3.0-5.el6 spec

* Sun Apr 25 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.3.0-5
- Removed clean section. No longer needed.

