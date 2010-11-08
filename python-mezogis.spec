Name: python-mezogis
Version: 0.1.5
Release: %mkrel 8
Summary: Graphical interface to query and analyse spatial data
Source: http://initd.org/svn/psycopg/geotypes/releases/mezogis-%{version}.tar.gz 
URL: http://www.mezogis.org
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
