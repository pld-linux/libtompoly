Summary:	LibTomPoly - library providing polynomial basis arithmetic
Summary(pl.UTF-8):	LibTomPoly - biblioteka arytmetyki na wielomianach
Name:		libtompoly
Version:	0.04
Release:	1
License:	Public Domain
Group:		Libraries
Source0:	http://libtom.org/files/ltp-%{version}.tar.bz2
# Source0-md5:	2e7883f758773223df656bd53fb4e4e0
Patch0:		%{name}-make.patch
URL:		http://libtom.org/?page=features&whatfile=ltp
BuildRequires:	libtommath-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
LibTomPoly is a public domain open source library to provide
polynomial basis arithmetic. It uses the public domain library
LibTomMath for the integer arithmetic and extends the functonality to
provide polynomial arithmetic.

%description -l pl.UTF-8
LibTomPoly to mająca otwarte źródła (na zasadzie public domain)
biblioteka arytmetyki na bazie wielomianów. Wykorzystuje wydaną na
tych samych zasadach bibliotekę LibTomMath do arytmetyki
całkowitoliczbowej i rozszerza funkcjonalność o arytmetykę
wielomianów.

%package devel
Summary:	Header files for LibTomPoly library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LibTomPoly
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libtommath-devel

%description devel
Header files for LibTomPoly library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki LibTomPoly.

%package static
Summary:	Static LibTomPoly library
Summary(pl.UTF-8):	Statyczna biblioteka LibTomPoly
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LibTomPoly library.

%description static -l pl.UTF-8
Statyczna biblioteka LibTomPoly.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags}" \
%{__make} \
	GCC="%{__cc}" \
	LIBPATH=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBPATH=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE changes.txt
%attr(755,root,root) %{_libdir}/libtompoly.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtompoly.so.0

%files devel
%defattr(644,root,root,755)
%doc pb.pdf
%attr(755,root,root) %{_libdir}/libtompoly.so
%{_libdir}/libtompoly.la
%{_includedir}/tompoly.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libtompoly.a
