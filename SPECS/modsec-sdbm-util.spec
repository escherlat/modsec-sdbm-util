Name: ea-apache24-modsec-sdbm-util
Version: 20160915
Summary: ModSecurity utility to manage the ip.pag file
%define release_prefix 5
Release: %{release_prefix}%{?dist}.escherlat
License: Apache License, Version 2.0
Group: System Environment/Daemons
URL: https://github.com/SpiderLabs/modsec-sdbm-util
Source: https://github.com/SpiderLabs/modsec-sdbm-util/modsec-sdbm-util-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: ea-apr
BuildRequires: ea-apr-util
BuildRequires: ea-apr-devel
BuildRequires: ea-apr-util-devel
Requires: ea-apache24-mod_security2

%description
Utility to manipulate SDBM files used by ModSecurity. With that utility it is possible to _shrink_ SDBM databases. It is also possible to list the SDBM contents with filters such as: expired or invalid items only.

%prep
%setup -q -n modsec-sdbm-util
./autogen.sh

%build
%configure --with-apr=/opt/cpanel/ea-apr15 --with-apu=/opt/cpanel/ea-apr15
make

%install
%{__rm} -rf %{buildroot}
%make_install
%{__install} -Dp -m0750 clean_secdatadir %{buildroot}%{_bindir}/clean_secdatadir

%post
/usr/local/cpanel/bin/manage_hooks add script %{_bindir}/clean_secdatadir --category=System --event=upcp --stage=post

%clean
%{__rm} -rf %{buildroot}

%files
%{_bindir}/clean_secdatadir
%{_bindir}/modsec-sdbm-util

%changelog
* Fri Sep 16 2016 Kenneth Power <kenneth.power@gmail.com> - 20160915-3
- Removed use of vars in the perl script
* Fri Sep 16 2016 Kenneth Power <kenneth.power@gmail.com> - 20160915-3
- Fixed perl script to pass strict

* Fri Sep 16 2016 Kenneth Power <kenneth.power@gmail.com> - 2016092
- Added perl script and hook registration

* Thu Sep 15 2016 Kenneth Power <kenneth.power@gmail.com> - 20160915-1
- Initial spec file creation.
EOF
