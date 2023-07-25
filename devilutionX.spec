Summary:	Diablo build for modern operating systems
Summary(pl.UTF-8):	Diablo zbudowane dla współczesnych systemów operacyjnych
Name:		devilutionX
Version:	1.5.0
Release:	1
License:	Unlicense
Group:		X11/Applications/Games
Source0:	https://github.com/diasurgical/devilutionX/releases/download/%{version}/devilutionx-src.tar.xz
# Source0-md5:	3963eeff2447222f2e35fc8701ba83e5
URL:		https://github.com/diasurgical/devilutionX/
BuildRequires:	SDL2-devel
BuildRequires:	SDL2_image-devel >= 2.0.5
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 3.15
BuildRequires:	gettext-tools
BuildRequires:	libfmt-devel >= 8.0.0
BuildRequires:	libsodium-devel
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	simpleini-devel >= 4.19
BuildRequires:	smpq
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	SDL2_image >= 2.0.5
Requires:	hicolor-icon-theme
Requires:	libfmt >= 8.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Diablo build for modern operating systems.

%description -l pl.UTF-8
Diablo zbudowane dla współczesnych systemów operacyjnych.

%prep
%setup -q -n devilutionx-src-%{version}

%build
%cmake -B build \
	-DVERSION_NUM="%{version}" \
	-DDISABLE_ZERO_TIER:BOOL=ON \
	-DDEVILUTIONX_STATIC_CXX_STDLIB:BOOL=OFF \
	-DDEVILUTIONX_SYSTEM_SIMPLEINI:BOOL=ON \
	-DBUILD_TESTING:BOOL=OFF
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%attr(755,root,root) %{_bindir}/devilutionx
%{_desktopdir}/devilutionx.desktop
%{_desktopdir}/devilutionx-hellfire.desktop
%{_iconsdir}/hicolor/512x512/apps/devilutionx.png
%{_iconsdir}/hicolor/512x512/apps/devilutionx-hellfire.png
%dir %{_datadir}/diasurgical
%dir %{_datadir}/diasurgical/devilutionx
%{_datadir}/diasurgical/devilutionx/devilutionx.mpq
%{_datadir}/metainfo/devilutionx.metainfo.xml
