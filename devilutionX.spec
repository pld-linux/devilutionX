Summary:	Diablo build for modern operating systems
Name:		devilutionX
Version:	1.2.0
Release:	1
License:	Unlicense
Group:		X11/Applications/Games
Source0:	https://github.com/diasurgical/devilutionX/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f6569e0eff2f5d69489775bdc288f3f5
URL:		https://github.com/diasurgical/devilutionX/
BuildRequires:	SDL2-devel
BuildRequires:	SDL2_mixer-devel
BuildRequires:	SDL2_ttf-devel
BuildRequires:	cmake >= 3.13
BuildRequires:	libsodium-devel
BuildRequires:	libstdc++-devel >= 6:4.8.1
BuildRequires:	rpmbuild(macros) >= 1.605
Requires(post,postun):	fontpostinst
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
Diablo build for modern operating systems.

%prep
%setup -q

%build
cd build
%cmake .. \
	-DTTF_FONT_DIR='"%{_ttffontsdir}/"' \
	-DVERSION_NUM="%{version}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_ttffontsdir}
mv $RPM_BUILD_ROOT%{_prefix}/share/fonts/truetype/*.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF
%update_icon_cache hicolor

%postun
fontpostinst TTF
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/devilutionx
%{_desktopdir}/devilutionx.desktop
%{_desktopdir}/devilutionx-hellfire.desktop
%{_ttffontsdir}/CharisSILB.ttf
%{_iconsdir}/hicolor/512x512/apps/devilutionx.png
%{_iconsdir}/hicolor/512x512/apps/devilutionx-hellfire.png
%dir %{_datadir}/diasurgical
%dir %{_datadir}/diasurgical/devilutionx
%{_datadir}/diasurgical/devilutionx/devilutionx.mpq
