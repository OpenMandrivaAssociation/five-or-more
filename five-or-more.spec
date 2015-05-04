%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		five-or-more
Version:	3.16.1
Release:	1
Summary:	GNOME Five or More game
License:	GPLv2+ and GFDL
Group:		Games/Puzzles
URL:		https://wiki.gnome.org/Five_or_more
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
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
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
%{_iconsdir}/*/*/apps/%{name}.*
%{_mandir}/man6/%{name}.6*
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Tue Feb 17 2015 wally <wally> 3.14.1-3.mga5
+ Revision: 815335
- require yelp for showing help

* Wed Oct 15 2014 umeabot <umeabot> 3.14.1-2.mga5
+ Revision: 741679
- Second Mageia 5 Mass Rebuild

* Mon Oct 13 2014 ovitters <ovitters> 3.14.1-1.mga5
+ Revision: 738443
- new version 3.14.1

* Sun Sep 28 2014 wally <wally> 3.14.0-1.mga5
+ Revision: 731401
- new version 3.14.0

* Tue Sep 16 2014 umeabot <umeabot> 3.13.92-2.mga5
+ Revision: 679217
- Mageia 5 Mass Rebuild

* Tue Sep 16 2014 ovitters <ovitters> 3.13.92-1.mga5
+ Revision: 676957
- new version 3.13.92

* Tue Aug 19 2014 fwang <fwang> 3.13.90.1-1.mga5
+ Revision: 665400
- update file list

  + ovitters <ovitters>
    - new version 3.13.90.1

* Mon May 12 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 622083
- new version 3.12.2

* Mon Apr 14 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 614072
- new version 3.12.1

* Mon Mar 24 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 607933
- new version 3.12.0

* Sun Mar 16 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604235
- new version 3.11.92

* Tue Feb 18 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 594233
- new version 3.11.90

* Wed Feb 05 2014 dams <dams> 3.11.5-1.mga5
+ Revision: 582955
- new version 3.11.5

* Mon Nov 11 2013 ovitters <ovitters> 3.10.2-1.mga4
+ Revision: 550506
- new version 3.10.2

* Sat Nov 09 2013 ovitters <ovitters> 3.10.1-3.mga4
+ Revision: 550149
- fix url

* Tue Oct 22 2013 umeabot <umeabot> 3.10.1-2.mga4
+ Revision: 541397
- Mageia 4 Mass Rebuild

* Sat Oct 12 2013 ovitters <ovitters> 3.10.1-1.mga4
+ Revision: 495860
- new version 3.10.1

* Mon Sep 23 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 483892
- new version 3.10.0

* Tue Sep 17 2013 ovitters <ovitters> 3.9.92-1.mga4
+ Revision: 480565
- new version 3.9.92

* Wed Aug 21 2013 fwang <fwang> 3.9.90-1.mga4
+ Revision: 468736
- new version 3.9.90
- cleanup spec

* Sun Jun 09 2013 dams <dams> 3.8.2-3.mga4
+ Revision: 440874
- Better 'Obsoletes'

* Sun Jun 09 2013 dams <dams> 3.8.2-2.mga4
+ Revision: 440806
- Obsoletes 'gnome-games-extra-data'

* Sun Jun 09 2013 dams <dams> 3.8.2-1.mga4
+ Revision: 440765
- add 'libxml2-utils' as BR
- imported package five-or-more

