Summary: Guacamole for NethServer
Name: nethserver-guacamole
Version: 0.0.1
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: x86_64

Requires: nethserver-mysql,java-1.8.0-openjdk-devel
#Requires: nethserver-base,nethserver-tomcat,guacd,libguac-client-rdp,libguac-client-ssh,libguac-client-vnc,gnu-free-mono-fonts
Requires: nethserver-base,nethserver-tomcat,gnu-free-mono-fonts


BuildRequires: perl
BuildRequires: nethserver-devtools

%description
Apache Guacamole NethServer integration

%pre
if ! getent passwd guacd >/dev/null; then
   # Add the guacd user
   useradd -r -U -s /sbin/nologin -d /var/lib/nethserver/guacd guacd
fi

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
mkdir -p %{buildroot}/var/lib/nethserver/mattermost
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Mon Apr 13 2020 Markus Neuberger <info@markusneuberger.at> - 0.0.1-1
- Add cockpit application
- Update to 1.1.0
- Add fail2ban code

