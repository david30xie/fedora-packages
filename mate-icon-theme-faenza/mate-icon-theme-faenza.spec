Summary:		MATE icon theme faenza
Name:			mate-icon-theme-faenza
Version:		1.5.0
Release:		1%{?dist}
URL:			http://mate-desktop.org
Source0:		http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
License:		GPLv2
BuildArch:		noarch
Group:			User Interface/Desktops
BuildRequires:	icon-naming-utils
BuildRequires:	mate-common

%description
This icon theme uses Faenza and Faience icon themes by ~Tiheum and
some icons customized for MATE by Rowen Stipe.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure \
	--enable-icon-mapping

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%post
/bin/touch --no-create %{_datadir}/icons/matefaenza &>/dev/null || :
/bin/touch --no-create %{_datadir}/icons/matefaenzagray &>/dev/null || :
/bin/touch --no-create %{_datadir}/icons/matefaenzadark &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/matefaenza &>/dev/null
    /bin/touch --no-create %{_datadir}/icons/matefaenzagray &>/dev/null
    /bin/touch --no-create %{_datadir}/icons/matefaenzadark &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/matefaenza &>/dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/matefaenzagray &>/dev/null || :
    gtk-update-icon-cache %{_datadir}/icons/matefaenzadark &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/matefaenza &>/dev/null || :
gtk-update-icon-cache %{_datadir}/icons/matefaenzagray &>/dev/null || :
gtk-update-icon-cache %{_datadir}/icons/matefaenzadark &>/dev/null || :

%files
%doc COPYING AUTHORS
%{_datadir}/icons/matefaenza/
%{_datadir}/icons/matefaenzagray/
%{_datadir}/icons/matefaenzadark/

%changelog
* Tue Jan 15 2013 David Xie <david.scriptfan@gmail.com> - 1.5.0-1
- Initiate version

