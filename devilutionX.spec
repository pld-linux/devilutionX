Summary:	Diablo build for modern operating systems
Name:		devilutionX
Version:	1.4.0
Release:	1
License:	Unlicense
Group:		X11/Applications/Games
Source0:	https://github.com/diasurgical/devilutionX/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	83136a831916cb62c8b14bee3c03831e
URL:		https://github.com/diasurgical/devilutionX/
BuildRequires:	SDL2-devel
BuildRequires:	SDL2_image-devel >= 2.0.5
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 3.13
BuildRequires:	libfmt-devel >= 7.0.0
BuildRequires:	libsodium-devel
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	smpq
BuildRequires:	zlib-devel
Requires(post,postun):	fontpostinst
Requires:	SDL2_image >= 2.0.5
Requires:	hicolor-icon-theme
Requires:	libfmt >= 7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Diablo build for modern operating systems.

%prep
%setup -q

%build
%cmake -B build \
	-DVERSION_NUM="%{version}" \
	-DDISABLE_ZERO_TIER:BOOL=ON \
	-DDEVILUTIONX_STATIC_CXX_STDLIB:BOOL=OFF \
	-DBUILD_TESTING:BOOL=OFF
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/devilutionx
%{_desktopdir}/devilutionx.desktop
%{_desktopdir}/devilutionx-hellfire.desktop
%{_iconsdir}/hicolor/512x512/apps/devilutionx.png
%{_iconsdir}/hicolor/512x512/apps/devilutionx-hellfire.png
%dir %{_datadir}/diasurgical
%dir %{_datadir}/diasurgical/devilutionx
%{_datadir}/diasurgical/devilutionx/devilutionx.mpq
