Name: python-mezogis
Version: 0.1.5
Release: 9
Summary: Graphical interface to query and analyse spatial data
Source: http://initd.org/svn/psycopg/geotypes/releases/mezogis-%{version}.tar.gz 
URL: https://www.mezogis.org
License: GPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
Provides: mezogis = %{version}-%{release}
Requires: python-geotypes
Requires: python-psycopg
Requires: pygtk2.0

%description
mezoGIS is a GIS application, a graphical interface to query and analyse
spatial data. mezoGIS does not store or compute data directly, but operates
external PostGIS databases. The goal of mezoGIS is to provide a tool for geo-
spatial analysis with PostGIS, through on-the-fly SQL queries as well as
through larger, external plugin scripts.

%prep
%setup -q -n mezogis-%{version} 

%install
rm -rf %buildroot
python setup.py install --root=%buildroot

rm -f %buildroot%_datadir/locale/messages.pot

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%_bindir/mezogis.py
%_datadir/applications/mezogis.desktop
%_datadir/mezogis
%_datadir/pixmaps/*
%py_puresitedir/*


%changelog
* Mon Nov 08 2010 Funda Wang <fwang@mandriva.org> 0.1.5-8mdv2011.0
+ Revision: 594928
- rebuild for py2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.1.5-7mdv2010.0
+ Revision: 442314
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.1.5-6mdv2009.1
+ Revision: 323794
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.1.5-5mdv2009.0
+ Revision: 259705
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.1.5-4mdv2009.0
+ Revision: 247513
- rebuild

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 0.1.5-2mdv2008.1
+ Revision: 168508
- rebuild
- fix summary
- fix no-buildroot-tag
- fix description-line-too-long
- fix summary-ended-with-dot

* Tue Dec 18 2007 Helio Chissini de Castro <helio@mandriva.com> 0.1.5-1mdv2008.1
+ Revision: 132723
- import python-mezogis


