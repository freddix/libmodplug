Summary:	The ModPlug mod file playing library
Name:		libmodplug
Version:	0.8.8.4
Release:	1
License:	Public Domain
Group:		Libraries
Source0:	http://downloads.sourceforge.net/modplug-xmms/%{name}-%{version}.tar.gz
# Source0-md5:	fddc3c704c5489de2a3cf0fedfec59db
URL:		http://modplug-xmms.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ModPlug is the mod file playing library. It can play 22 different mod
formats, including: MOD, S3M, XM, IT, 669, AMF (both of them), AMS,
DBM, DMF, DSM, FAR, MDL, MED, MTM, OKT, PTM, STM, ULT, UMX, MT2, PSM.
Sound quality is slightly better than Mikmod and vastly superior over
Winamp.

%package devel
Summary:	Header files for libmodplug library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for libmodplug library.

%prep
%setup -q

%build
# supplied libtool doesn't support C++ libraries
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libmodplug
%{_pkgconfigdir}/*.pc

