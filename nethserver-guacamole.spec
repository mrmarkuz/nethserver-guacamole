Summary: Guacamole for NethServer
Name: nethserver-guacamole
Version: 0.0.1
Release: 2%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: nethserver-mysql,java-1.8.0-openjdk-devel,mysql-connector-java
Requires: nethserver-base,tomcat8,guacd,libguac-client-rdp,libguac-client-ssh,libguac-client-vnc,gnu-free-mono-fonts

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

mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/%{name}/

cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/
cp -a ui/* %{buildroot}/usr/share/cockpit/%{name}/

(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} \
  --file /etc/sudoers.d/50_nsapi_nethserver_guacamole 'attr(0440,root,root)' \
  --file /usr/libexec/nethserver/api/%{name}/read 'attr(775,root,root)' \
%{buildroot} > %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Sun Jul 26 2020 Markus Neuberger <info@markusneuberger.at> - 0.0.1-2
- Update to 1.2.0

* Wed Apr 15 2020 Markus Neuberger <info@markusneuberger.at> - 0.0.1-1
- Add cockpit application
- Update to 1.1.0
- Add fail2ban code
- Add http redirect
- Random password for guacamole mysql user
- Use Centos mysql-connector-java
