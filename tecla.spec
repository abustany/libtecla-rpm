Name:		tecla
Version:	1.6.3
Release:	2%{?dist}
Summary:	Tecla provides interactive command line editing facilities.

Group:		System Environment/Libraries
License:	MIT
URL:		http://www.astro.caltech.edu/~mcs/tecla/index.html
Source0:	http://www.astro.caltech.edu/~mcs/tecla/libtecla-%{version}.tar.gz
Patch0:		configure-build-id.patch
Patch1:		Makefile-rules-no-rpath.patch

BuildRequires:	gcc
BuildRequires:	ncurses-devel
Requires:	ncurses-libs

%description
The tecla library provides UNIX and LINUX programs with interactive command
line editing facilities, similar to those of the UNIX tcsh shell. In addition
to simple command-line editing, it supports recall of previously entered
command lines, TAB completion of file names or other tokens, and in-line
wild-card expansion of filenames. The internal functions which perform
file-name completion and wild-card expansion are also available externally for
optional use by programs.


%package devel
Summary:	Files needed to develop programs which use the tecla library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: ncurses-devel


%description devel
The tecla library provides UNIX and LINUX programs with interactive command
line editing facilities, similar to those of the UNIX tcsh shell. If you want
to develop programs that will use the tecla library, you need to have the
tecla-devel package installed. You also need to have the tecla package
installed.


%package static
Summary: Static libraries for the tecla library
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}


%description static
The tecla-static package contains the static version of the tecla library.

%prep
%setup -q -n libtecla
%patch0 -p0
%patch1 -p0


%build
%configure
make %{?_smp_mflags}


%install
%make_install LIBDIR=$RPM_BUILD_ROOT%{_libdir} INCDIR=$RPM_BUILD_ROOT%{_includedir} MANDIR=$RPM_BUILD_ROOT%{_mandir} BINDIR=$RPM_BUILD_ROOT%{_bindir}


%files
%defattr(-,root,root,-)
%doc CHANGES README RELEASE.NOTES
%license LICENSE.TERMS
%{_bindir}/enhance
%{_mandir}/*/*
%{_libdir}/libtecla.so.*
%{_libdir}/libtecla_r.so.*


%files devel
%{_includedir}/libtecla.h
%{_libdir}/libtecla.so
%{_libdir}/libtecla_r.so


%files static
%{_libdir}/libtecla.a
%{_libdir}/libtecla_r.a


%changelog
* Mon Dec 03 2018 Adrien Bustany <adrien@bustany.org> - 1.6.3-3
- Include gcc in BuildRequires, since Fedora 29 removed it from buildroot.

* Mon Sep 19 2016 Jeremy Lin <jeremy.lin@gmail.com> - 1.6.3-2
- Include `enhance` utility
- Minimize build dependencies

* Fri Jan 29 2016 Adrien Bustany <adrien@bustany.org> 1.6.3-1
- Initial packaging
