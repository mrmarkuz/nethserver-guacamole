Summary: NethServer postgresql configuration
Name: nethserver-guacamole
Version: 0.0.0
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: nethserver-mysql,java-1.7.0-openjdk-devel
Requires: nethserver-base,nethserver-tomcat,guacd,libguac-client-rdp,libguac-client-ssh,libguac-client-vnc
Requires: wget,pv,dialog,gcc,cairo-devel,libpng-devel,uuid-devel,ffmpeg-devel,freerdp-devel,freerdp-plugins,pango-devel,libssh2-devel,libtelnet-devel,libvncserver-devel,pulseaudio-libs-devel,openssl-devel,libvorbis-devel,libwebp-devel,tomcat,gnu-free-mono-fonts


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
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
