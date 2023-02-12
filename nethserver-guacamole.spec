Summary: Guacamole for NethServer
Name: nethserver-guacamole
Version: 0.0.1
Release: 6%{?dist}
License: GPL
URL: %{url_prefix}/%{name}
Source0: %{name}-%{version}.tar.gz
Source1: https://apache.org/dyn/closer.cgi?action=download&filename=guacamole/1.4.0/binary/guacamole-1.4.0.war
#Source2: https://github.com/Zer0CoolX/guacamole-customize-loginscreen-extension/blob/master/branding.jar
Source2: https://github.com/Zer0CoolX/guacamole-customize-loginscreen-extension/raw/master/branding.jar
Source3: https://apache.org/dyn/closer.cgi?action=download&filename=guacamole/1.4.0/binary/guacamole-auth-jdbc-1.4.0.tar.gz
Source4: https://apache.org/dyn/closer.cgi?action=download&filename=guacamole/1.4.0/binary/guacamole-auth-ldap-1.4.0.tar.gz
BuildArch: noarch

Requires: nethserver-mysql,java-1.8.0-openjdk-devel,mysql-connector-java
Requires: nethserver-base,tomcat8,guacd,libguac-client-rdp,libguac-client-ssh,libguac-client-vnc,gnu-free-mono-fonts

BuildRequires: perl
BuildRequires: nethserver-devtools

# allow adding jars
%define __jar_repack %{nil}

%description
Apache Guacamole NethServer integration

%pre
%global __os_install_post %{nil}
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
mkdir -p %{buildroot}/var/lib/guacamole/extensions

# copy guacamole web portal
cp -a %{SOURCE1} %{buildroot}/var/lib/guacamole/guacamole.war

# copy extensions
cp -va %{SOURCE2} %{buildroot}/var/lib/guacamole/extensions/

# untar extensions
tar -xzvf %{SOURCE3} -C %{buildroot}/var/lib/guacamole/extensions guacamole-auth-jdbc-1.4.0/mysql/guacamole-auth-jdbc-mysql-1.4.0.jar --strip-components=2
tar -xzvf %{SOURCE4} -C %{buildroot}/var/lib/guacamole/extensions guacamole-auth-ldap-1.4.0/guacamole-auth-ldap-1.4.0.jar --strip-components=1

cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/
cp -a ui/* %{buildroot}/usr/share/cockpit/%{name}/

(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} \
  --file /etc/sudoers.d/50_nsapi_nethserver_guacamole 'attr(0440,root,root)' \
  --file /usr/libexec/nethserver/api/%{name}/read 'attr(775,root,root)' \
  --file /var/lib/guacamole/guacamole.war 'attr(770,tomcat,tomcat)' \
%{buildroot} > %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update
%config(noreplace) /var/lib/guacamole/extensions/branding.jar

%changelog
* Sun Feb 12 2023 Markus Neuberger <info@markusneuberger.at> - 0.0.1-6
- Fix virtualhost access when there is a webserver virtualhost - thanks to Gabor

* Tue Jun 14 2022 Markus Neuberger <info@markusneuberger.at> - 0.0.1-5
- Fix branding overwrite on Update - thanks to Royce

* Sat Jun 04 2022 Markus Neuberger <info@markusneuberger.at> - 0.0.1-4
- Update to 1.4.0

* Tue Feb 23 2021 Markus Neuberger <info@markusneuberger.at> - 0.0.1-3
- Update to 1.3.0
- Add branding.jar extension by Zer0CoolX
- Add guacamole.war and extensions download to spec file
- Fix guacamole diretory deletion for tomcat8

* Sun Jul 26 2020 Markus Neuberger <info@markusneuberger.at> - 0.0.1-2
- Update to 1.2.0
- Update to tomcat 8

* Wed Apr 15 2020 Markus Neuberger <info@markusneuberger.at> - 0.0.1-1
- Add cockpit application
- Update to 1.1.0
- Add fail2ban code
- Add http redirect
- Random password for guacamole mysql user
- Use Centos mysql-connector-java
