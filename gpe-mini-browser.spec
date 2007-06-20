Summary:	GPE mini browser
Summary(pl.UTF-8):	Mała przeglądarka GPE
Name:		gpe-mini-browser
Version:	0.21
Release:	1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.gz
# Source0-md5:	a1297dfd14c008e3415f89b01eef75cd
URL:		http://gpe.linuxtogo.org/projects/gpe-mini-browser.shtml
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	libgpewidget-devel
BuildRequires:	osb-nrcit-devel
BuildRequires:	pkgconfig
BuildRequires:	sqlite
# optional: hildon-libs hildon-fm libosso
Requires:	gpe-icons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mini browser for GPE embedded devices.

%description -l pl.UTF-8
Mała przeglądarka GPE dla urządzeń wbudowanych.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpe-mini-browser
%{_desktopdir}/gpe-mini-browser.desktop
%{_pixmapsdir}/gpe-mini-browser.png
