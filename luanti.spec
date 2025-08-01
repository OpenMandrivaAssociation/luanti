Summary:	An InfiniMiner/Minecraft inspired game engine
Name:		luanti
Version:	5.12.0
Release:	2
License:	GPLv2+
Group:		Games/Other
Url:		https://luanti.org

Source0:	https://github.com/luanti-org/luanti/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	xinput
BuildRequires:	gmp-devel
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	gettext-devel
# Upstream bundling own fork
#BuildRequires:	irrlicht-devel
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libzstd)
BuildRequires:	pkgconfig(luajit)
BuildRequires:	pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(vorbisfile)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(jsoncpp)

# for compiling irrlichtMT
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:	pkgconfig(xi)
BuildRequires:  pkgconfig(xxf86vm)

# renamed from minetest
Obsoletes: minetest < %{version}

BuildSystem:	cmake
BuildOption:	-DENABLE_GETTEXT=ON
BuildOption:	-DENABLE_SYSTEM_GMP=ON
BuildOption:	-DENABLE_SYSTEM_JSONCPP=ON
BuildOption:	-DBUILD_SERVER=ON
BuildOption:	-DBUILD_CLIENT=ON
BuildOption:	-DENABLE_UPDATE_CHECKER=OFF
BuildOption:	-DRUN_IN_PLACE=OFF

%description
One of the first InfiniMiner/Minecraft(/whatever) inspired games (started
October 2010), with a goal of taking the survival multiplayer gameplay
to a slightly different direction.

This game is under development, and as of now, the game does not really
differ from Minecraft except for having a lot less features. Still, playing
is quite fun already, especially for people who have not been able to
experience Minecraft.

%package server

Summary: Luanti (formerly minetest) server binary

%description server
Luanti (formerly minetest) server binary

This game is under development, and as of now, the game does not really
differ from Minecraft except for having a lot less features. Still, playing
is quite fun already, especially for people who have not been able to
experience Minecraft.

%files -f %{name}.lang
%doc doc/*.txt doc/*.md
%{_datadir}/doc/%{name}/README.md
%{_datadir}/doc/%{name}/minetest.conf.example
%{_bindir}/%{name}
%{_bindir}/minetest
%{_datadir}/%{name}
%{_datadir}/metainfo/org.luanti.luanti.metainfo.xml
%{_datadir}/applications/org.luanti.luanti.desktop
%{_iconsdir}/hicolor/*/apps/%{name}*
%{_mandir}/man6/%{name}.6*

%files server
%{_bindir}/%{name}server
%{_bindir}/minetestserver
%{_mandir}/man6/%{name}server.6*

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}
