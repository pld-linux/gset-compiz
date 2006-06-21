#
# TODO:
# - find out bout the License
# - check my 'preatty' descriptions
# - find out BR and R's
# - make it R to some compiz metapackage (both compiz and
#   compiz-quinnstorm are ok for gset)
#
Summary:	A GTK tool to configure compiz
Summary(pl):	Narzêdzie GTK do konfiguracji compiza
Name:		gset-compiz
%define		_rel	r1
Version:	0.3.3
Release:	%{rel}.0.1
License:	CHGW
Group:		X11/Window Managers/Tools
Source0:	%{name}-%{version}-%{_rel}.tar.bz2
URL:		http://www.xgl-coffee.org
#BuildRequires:	-
Requires:	compiz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool is a all You'd ever need to configure compiz. It let's You
select whichever compiz plugin You like to load, tweak all the
possible variables in all possible compiz plugins in an easy fasion.
This package puts a radical stop to configuring compiz via GConf
editor.

%description -l pl
To narzêdzie jest wszystkim co by¶ kiedykolwiek potrzebowa³ do
skonfigurowania compiza. Pozawal Ci wybraæ, które wtyczki copmiza
chcia³by¶ za³±dowaæ, pozwala manipulowaæ wszystkimi mo¿liwymi
zmiennymi we wszystkich mo¿liwych wtyczkach compiza w prosty sposób.
Ta paczka powoduje radykalny koniec konfigurowaniu compiza przez
edytora konfiguracji GConf.

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
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/gset.glade
%{_datadir}/pixmaps/%{name}.png
