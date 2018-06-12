%define _enable_debug_packages %{nil}
%define debug_package %{nil}
# minor not needed. (penguin)
#define minor 314
%define oname OpenFPC

Summary:	OpenFPC is designed to allow a network traffic capture tool
Name:		openfpc
Version:	0.9
Release:	1
License:	GPLv3+
Group:		Monitoring
Url:		http://www.openfpc.org
Source0:	https://github.com/leonward/OpenFPC/archive/%{version}/%{oname}-%{version}.tar.gz
Requires:	apache-mpm-prefork
Requires:	cxtracker
Requires:	daemonlogger
Requires:	libdnet-utils
Requires:	tcpdump
Requires:	tshark
Requires:	wireshark-tools

%description
OpenFPC is designed to allow a network traffic capture tool to scale in both
horizontal, and vertical directions. It is a distributed system linked together
using communication paths and proxies to integrate with common SOC
(Security Operating Center) designs. To help further explain it's method of
deployment and architecture, lets cover some common tasks and see how they
are executed while looking at a simple diagram.

%files
%defattr(0755,root,root)
%{_sysconfdir}/%{name}/
%{_datadir}/%{name}/www/
%{_datadir}/%{name}/cgi-bin/
%{_usr}/lib/perl5/site_perl/OFPC
%{_sysconfdir}/httpd/conf.d/*.apache2.conf
%{_initrddir}/openfpc-cx2db
%{_initrddir}/openfpc-cxtracker
%{_initrddir}/openfpc-daemonlogger
%{_initrddir}/openfpc-queued
%{_bindir}/openfpc
%{_bindir}/openfpc-client
%{_bindir}/openfpc-cx2db
%{_bindir}/openfpc-dbmaint
%{_bindir}/openfpc-password
%{_bindir}/openfpc-queued

%post
echo "Adding openfpc user and group"
adduser --system --user-group --no-create-home --shell /usr/sbin/nologin openfpc

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}

find . -name .svn | xargs rm -rf

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

mv etc/openfpc.cgi.apache2.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/
mv etc/openfpc.gui.apache2.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/
mv etc/*.conf %{buildroot}%{_sysconfdir}/%{name}
mv etc/*.ofpc %{buildroot}%{_sysconfdir}/%{name}
mv www/* %{buildroot}%{_datadir}/%{name}/www
mv cgi-bin/* %{buildroot}%{_datadir}/%{name}/cgi-bin
mv openfpc* %{buildroot}%{_bindir}
mv etc/init.d/* %{buildroot}%{_initrddir}
mv OFPC/* %{buildroot}%{_usr}/lib/perl5/site_perl/OFPC

rm -rf %{buildroot}%{_bindir}/openfpc-install.sh

