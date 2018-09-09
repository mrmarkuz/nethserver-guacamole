Summary: Guacamole for NethServer
Name: nethserver-guacamole
Version: 0.0.0
Release: 3%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: nethserver-mysql,java-1.7.0-openjdk-devel
Requires: nethserver-base,nethserver-tomcat,guacd,libguac-client-rdp,libguac-client-ssh,libguac-client-vnc,gnu-free-mono-fonts

BuildRequires: perl
BuildRequires: nethserver-devtools

%description
Apache Guacamole NethServer integration

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
