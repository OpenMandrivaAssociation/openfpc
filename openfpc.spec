%define name openfpc
%define version 0.6
%define minor 314

Name: %{name}
Summary: OpenFPC is designed to allow a network traffic capture tool
Version: %{version}
Release: %mkrel 1
License: GPLv3
Group: Monitoring
Source: http://openfpc.googlecode.com/files/%{name}-%{version}-%{minor}.tgz
URL:	http://www.openfpc.org
#Requires: cxtracker, daemonlogger, libdnet, tcpdump, date, mergecap, perl, tshark, apache-mpm-prefork
Requires: cxtracker, daemonlogger, libdnet, tcpdump, wireshark-tools, perl, tshark, apache-mpm-prefork
BuildRoot: %_tmppath/%{name}-%{version}-buildroot

%description
OpenFPC is designed to allow a network traffic capture tool to scale in both horizontal, and vertical directions.
It is a distributed system linked together using communication paths and proxies to integrate with 
common SOC (Security Operating Center) designs. To help further explain it's method of deployment and architecture, 
lets cover some common tasks and see how they are executed while looking at a simple diagram.

%prep
%setup -q -n %{name}-%{version}-%{minor}

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_initrddir}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/www
mkdir -p %{buildroot}%{_datadir}/%{name}/cgi-bin

#/usr/lib/perl5/vendor_perl/5.12.3/OFPC
mkdir -p %{buildroot}%{_usr}/lib/perl5/site_perl/OFPC
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/

mv etc/*.conf %{buildroot}%{_sysconfdir}/%{name}
mv etc/*.ofpc %{buildroot}%{_sysconfdir}/%{name}
mv www/* %{buildroot}%{_datadir}/%{name}/www
mv cgi-bin/* %{buildroot}%{_datadir}/%{name}/cgi-bin
mv openfpc* %{buildroot}%{_bindir}
mv etc/init.d/* %{buildroot}%{_initrddir}
mv OFPC/* %{buildroot}%{_usr}/lib/perl5/site_perl/OFPC
mv etc/openfpc.apache2.site %{buildroot}%{_sysconfdir}/httpd/conf.d/

rm -rf %{buildroot}%{_bindir}/openfpc-install.sh

%post 
echo "Adding openfpc user and group"
adduser --system --user-group --no-create-home --shell /usr/sbin/nologin openfpc

%files
%defattr(0755,root,root)
%{_sysconfdir}/%{name}/
%{_datadir}/%{name}/www/
%{_datadir}/%{name}/cgi-bin/
%{_usr}/lib/perl5/site_perl/OFPC
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


%changelog
* Wed Sep 21 2011 Alexander Barakin <abarakin@mandriva.org> 0.6-1mdv2012.0
+ Revision: 700684
- imported package openfpc

* Mon Jun 13 2011 Leonardo Coelho <leonardoc@mandriva.com> 0.5-1
+ Revision: 684495
- first mdv version
- Created package structure for openfpc.

