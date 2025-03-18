%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Name:		five-or-more
Version:	48.0
Release:	1
Summary:	GNOME Five or More game
License:	GPLv2+ and GFDL
Group:		Games/Puzzles
URL:		https://wiki.gnome.org/Five_or_more
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:	pkgconfig(libgnome-games-support-1)
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  vala-devel
BuildRequires:  librsvg-vala-devel
Obsoletes:	glines
Obsoletes:	glines-extra-data
# For help
Requires:	yelp

%description
Five or More is the GNOME port of the once popular Windows game called
Color Lines. The game's objective is to align as often as possible five
or more objects of the same color and shape causing them to disappear.
Play as long as possible, and be #1 in the High Scores!

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.five-or-more.desktop
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
%{_iconsdir}/*/*/apps/org.gnome.five-or-more.*
%{_iconsdir}/*/*/apps/org.gnome.five-or-more-symbolic.svg
%{_mandir}/man6/%{name}.6*
%{_datadir}/metainfo/org.gnome.five-or-more.metainfo.xml

