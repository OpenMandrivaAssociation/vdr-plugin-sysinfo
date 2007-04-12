
%define plugin	sysinfo
%define name	vdr-plugin-%plugin
%define version	0.1.0a
%define rel	11

Summary:	VDR plugin: System information plugin
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://kikko77.altervista.org/
Source:		vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
This plugin show same features of the vdr-box system like :
-kernel version
-cpu type
-cpu frequency
-cpu usage
-cpu free
-total memory
-memory free
-memory usage

%prep
%setup -q -n %plugin-%version

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}/%{plugin}
install -m755 script/sysinfo.sh %{buildroot}%{_vdr_plugin_cfgdir}/%{plugin}

install -d -m755 %{buildroot}%{_bindir}

cat > %{buildroot}%{_bindir}/sysinfo.sh <<EOF
#!/bin/sh
VDR_CONFIGDIR="%{_vdr_cfgdir}"
[ -e %{_sysconfdir}/sysconfig/vdr ] && . %{_sysconfdir}/sysconfig/vdr
exec \$VDR_CONFIGDIR/plugins/%plugin/sysinfo.sh \$@
EOF
chmod a+x %{buildroot}%{_bindir}/sysinfo.sh

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%{_bindir}/sysinfo.sh
%{_vdr_plugin_cfgdir}/%{plugin}


