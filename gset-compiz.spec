#
# TODO:
# - find out BR and R's
# - make it R to some compiz metapackage (both compiz and
#   compiz-quinnstorm are ok for gset)
#
Summary:	A GTK+ tool to configure compiz
Summary(pl):	Narz�dzie GTK+ do konfiguracji compiza
Name:		gset-compiz
%define		_rel	r1
Version:	0.3.3
Release:	%{_rel}.0.1
License:	GPL v2+
Group:		X11/Window Managers/Tools
Source0:	http://distfiles.xgl-coffee.org/%{name}-%{version}-%{_rel}.tar.bz2
# Source0-md5:	af40f2b8bf6e5f7f18debf2ecdee5248
URL:		http://www.xgl-coffee.org/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	pkgconfig
Requires:	compiz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool is all you'd ever need to configure compiz. It lets you
select whichever compiz plugin you like to load, tweak all the
possible variables in all possible compiz plugins in an easy fasion.
This package puts a radical stop to configuring compiz via GConf
editor.

%description -l pl
To narz�dzie jest wszystkim co potrzeba do skonfigurowania compiza.
Pozwala wybra�, kt�re wtyczki compiza za�adowa� oraz manipulowa�
wszystkimi mo�liwymi zmiennymi we wszystkich mo�liwych wtyczkach
compiza w prosty spos�b. Ten pakiet powoduje radykalny koniec
konfigurowaniu compiza za pomoc� edytora konfiguracji GConf.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
