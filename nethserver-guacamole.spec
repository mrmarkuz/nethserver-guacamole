Summary: Guacamole for NethServer
Name: nethserver-guacamole
Version: 0.0.0
Release: 4%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: nethserver-mysql,java-1.8.0-openjdk-devel
#Requires: nethserver-base,nethserver-tomcat,guacd,libguac-client-rdp,libguac-client-ssh,libguac-client-vnc,gnu-free-mono-fonts
Requires: nethserver-base,nethserver-tomcat,guacd,libguac-client-rdp,libguac-client-ssh,libguac-client-vnc,gnu-free-mono-fonts


BuildRequires: perl
BuildRequires: nethserver-devtools

%description
Apache Guacamole NethServer integration

%pre
if ! getent passwd guacd >/dev/null; then
   # Add the "mattermost" user
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
