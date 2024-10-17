%define plugin	sysinfo

Summary:	VDR plugin: System information plugin
Name:		vdr-plugin-%plugin
Version:	0.1.0a
Release:	24
Group:		Video
License:	GPL
URL:		https://kikko77.altervista.org/
Source:		vdr-%plugin-%{version}.tar.bz2
Patch0:		01_sysinfo-0.1.0a-fontfix.dpatch
Patch1:		sysinfo-0.1.0a-i18n-1.6.patch
Patch2:		sysinfo-fix-includes.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin show same features of the vdr-box system like :
- kernel version
- cpu type
- cpu frequency
- cpu usage
- cpu free
- total memory
- memory free
- memory usage

%prep
%setup -q -n %plugin-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

install -d -m755 %{buildroot}%{vdr_plugin_cfgdir}/%{plugin}
install -m755 script/sysinfo.sh %{buildroot}%{vdr_plugin_cfgdir}/%{plugin}

install -d -m755 %{buildroot}%{_bindir}

cat > %{buildroot}%{_bindir}/sysinfo.sh <<EOF
#!/bin/sh
VDR_CONFIGDIR="%{vdr_cfgdir}"
[ -e %{_sysconfdir}/sysconfig/vdr ] && . %{_sysconfdir}/sysconfig/vdr
exec \$VDR_CONFIGDIR/plugins/%plugin/sysinfo.sh \$@
EOF
chmod a+x %{buildroot}%{_bindir}/sysinfo.sh

%files -f %plugin.vdr
%doc README HISTORY
%{_bindir}/sysinfo.sh
%{vdr_plugin_cfgdir}/%{plugin}


