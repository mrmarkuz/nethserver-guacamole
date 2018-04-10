Summary: NethServer postgresql configuration
Name: nethserver-guacamole
Version: 0.0.0
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
Source1: http://sourceforge.net/projects/guacamoleinstallscript/files/CentOS/guacamole-install-script.sh
BuildArch: noarch

Requires: nethserver-mysql,java-1.7.0-openjdk-devel
Requires: nethserver-base

BuildRequires: perl
BuildRequires: nethserver-devtools 

%description
NethServer guacamole configuration

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
mkdir -p root/opt/guacamole
cp %{SOURCE1} root/opt/guacamole/
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
