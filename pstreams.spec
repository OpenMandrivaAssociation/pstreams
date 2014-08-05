Summary:	POSIX Process Control in C++
Name:		pstreams
Version:	0.8.0
Release:	1
License:	LGPLv3+
Group:		Development/C++
Url:		http://%{name}.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	doxygen
BuildArch:	noarch

%description
PStreams class is like a C++ wrapper for the POSIX.2 functions popen(3) and
pclose(3), using C++ iostreams instead of C's stdio library.

#----------------------------------------------------------------------------

%package devel
Summary:	POSIX Process Control in C++
Group:		Development/C++
BuildArch:	noarch

%description devel
PStreams class is like a C++ wrapper for the POSIX.2 functions popen(3) and
pclose(3), using C++ iostreams instead of C's stdio library.

%files devel
%doc doc/html README AUTHORS ChangeLog
%{_includedir}/pstreams

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%make

%install
%makeinstall

