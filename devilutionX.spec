Summary:	Diablo build for modern operating systems
Name:		devilutionX
Version:	1.3.0
Release:	1
License:	Unlicense
Group:		X11/Applications/Games
Source0:	https://github.com/diasurgical/devilutionX/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	23791a40dfc5b6fbe6a935a3b76d5bc3
Source1:	https://github.com/diasurgical/asio/archive/ebeff99f539da23d27c2e8d4bdbc1ee011968644.tar.gz
# Source1-md5:	4195600342abf307b8a9a571b87d687f
Source2:	https://github.com/realnc/SDL_audiolib/archive/aa79660eba4467a44f9dcaecf26b0f0a000abfd7.tar.gz
# Source2-md5:	7c79bb0d97f8469bbe5339061e910095
Source3:	https://github.com/brofield/simpleini/archive/7bca74f6535a37846162383e52071f380c99a43a.zip
# Source3-md5:	af067f743dd5c7aac3212ca22da6f621
Patch0:		system_sdl_image.patch
Patch1:		no_static.patch
URL:		https://github.com/diasurgical/devilutionX/
BuildRequires:	SDL2-devel
BuildRequires:	SDL2_image-devel >= 2.0.5
BuildRequires:	SDL2_mixer-devel
BuildRequires:	cmake >= 3.13
BuildRequires:	libfmt-devel >= 7.0.0
BuildRequires:	libpng-devel
BuildRequires:	libsodium-devel
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	smpq
Requires(post,postun):	fontpostinst
Requires:	SDL2_image >= 2.0.5
Requires:	hicolor-icon-theme
Requires:	libfmt >= 7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Diablo build for modern operating systems.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

install -d build/_deps/asio-subbuild/asio-populate-prefix/src
cp -p  %{SOURCE1} build/_deps/asio-subbuild/asio-populate-prefix/src
install -d build/_deps/sdl_audiolib-subbuild/sdl_audiolib-populate-prefix/src
cp -p %{SOURCE2} build/_deps/sdl_audiolib-subbuild/sdl_audiolib-populate-prefix/src
install -d build/_deps/simpleini-subbuild/simpleini-populate-prefix/src
cp -p %{SOURCE3} build/_deps/simpleini-subbuild/simpleini-populate-prefix/src

%build
cd build
%cmake .. \
	-DVERSION_NUM="%{version}" \
	-DDISABLE_ZERO_TIER:BOOL=ON
%{__make}

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
