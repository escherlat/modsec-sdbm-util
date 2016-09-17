Name: ea-apache24-modsec-sdbm-util
Version: 0.0.1
Summary: ModSecurity utility to manage the ip.pag file
Release: 1%{?dist}
License: Apache License, Version 2.0
Group: System Environment/Daemons
URL: https://github.com/SpiderLabs/modsec-sdbm-util
Source: https://github.com/SpiderLabs/modsec-sdbm-util/modsec-sdbm-util-0.0.1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: ea-apr
BuildRequires: ea-apr-util
BuildRequires: ea-apr-devel
BuildRequires: ea-apr-util-devel
Requires: ea-apache24-mod_security2

%description
Utility to manipulate SDBM files used by ModSecurity. With that utility it is possible to _shrink_ SDBM databases. It is also possible to list the SDBM contents with filters such as: expired or invalid items only.

%prep
%setup -n modsec-sdbm-util-%{version}
./autogen.sh

%build
%configure --with-apr=/opt/cpanel/ea-apr15 --with-apu=/opt/cpanel/ea-apr15
make

%install
%{__rm} -rf %{buildroot}
%make_install

%clean
%{__rm} -rf %{buildroot}

%files
%{_bindir}/modsec-sdbm-util

%changelog
* Thu Sep 15 2016 Kenneth Power <kenneth.power@gmail.com> - 0.0.1
- Initial spec file creation.
EOF
