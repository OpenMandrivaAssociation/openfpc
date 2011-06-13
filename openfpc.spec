%define name openfpc
%define version 0.5
%define minor 281

Name: %{name}
Summary: OpenFPC is designed to allow a network traffic capture tool
Version: %{version}
Release: %mkrel 1
License: GPLv3
Group: Monitoring
Source: http://openfpc.googlecode.com/files/%{name}-%{version}-%{minor}.tgz
URL:	http://www.openfpc.org
Requires: cxtracker, daemonlogger, libdnet, tcpdump, date, mergecap, perl, tshark, apache-mpm-prefork
BuildRoot: %_tmppath/%{name}-%{version}-buildroot

%description
OpenFPC is designed to allow a network traffic capture tool to scale in both horizontal, and vertical directions.
It is a distributed system linked together using communication paths and proxies to integrate with 
common SOC (Security Operating Center) designs. To help further explain it's method of deployment and architecture, 
lets cover some common tasks and see how they are executed while looking at a simple diagram.

%prep
%setup -n %{name}-%{version}-%{minor}

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_initrddir}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/www
mkdir -p %{buildroot}%{_datadir}/%{name}/cgi-bin
mkdir -p %{buildroot}%{_usr}/lib/perl5/site_perl/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/

mv etc/*.conf %{buildroot}%{_sysconfdir}/%{name}
mv etc/*.ofpc %{buildroot}%{_sysconfdir}/%{name}
mv www/* %{buildroot}%{_datadir}/%{name}/www
mv cgi-bin/* %{buildroot}%{_datadir}/%{name}/cgi-bin
mv openfpc* %{buildroot}%{_bindir}
mv etc/init.d/* %{buildroot}%{_initrddir}
mv OFPC/* %{buildroot}%{_usr}/lib/perl5/site_perl/%{name}
mv etc/openfpc.apache2.site %{buildroot}%{_sysconfdir}/httpd/conf.d/

rm -rf %{buildroot}%{_bindir}/openfpc-install.sh

%post 
adduser --quiet --system --group --no-create-home --shell /usr/sbin/nologin openfpc

%files
%defattr(0755,root,root)
%{_sysconfdir}/%{name}/
%{_datadir}/%{name}/www/
%{_datadir}/%{name}/cgi-bin/
%{_usr}/lib/perl5/site_perl/%{name}
%{_sysconfdir}/httpd/conf.d/openfpc.apache2.site
%{_initrddir}/openfpc-cx2db
%{_initrddir}/openfpc-cxtracker
%{_initrddir}/openfpc-daemonlogger
%{_initrddir}/openfpc-queued
%{_bindir}/openfpc
%{_bindir}/openfpc-client
%{_bindir}/openfpc-cx2db
%{_bindir}/openfpc-dbmaint
%{_bindir}/openfpc-queued


%clean
rm -rf $RPM_BUILD_ROOT
