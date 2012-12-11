
%define plugin	sysinfo
%define name	vdr-plugin-%plugin
%define version	0.1.0a
%define rel	21

Summary:	VDR plugin: System information plugin
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://kikko77.altervista.org/
Source:		vdr-%plugin-%version.tar.bz2
Patch0:		01_sysinfo-0.1.0a-fontfix.dpatch
Patch1:		sysinfo-0.1.0a-i18n-1.6.patch
Patch2:		sysinfo-fix-includes.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
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
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%vdr_plugin_prep

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


%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.0a-21mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 0.1.0a-20mdv2009.1
+ Revision: 359783
- fix includes (fix-includes.patch)
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.1.0a-19mdv2009.0
+ Revision: 197985
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.1.0a-18mdv2009.0
+ Revision: 197730
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- adapt for font changes of VDR 1.6 (P0 from e-tobi)
- fix description

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.1.0a-17mdv2008.1
+ Revision: 145210
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0a-16mdv2008.1
+ Revision: 103220
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0a-15mdv2008.0
+ Revision: 50054
- rebuild for new vdr

* Fri Jun 22 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0a-14mdv2008.0
+ Revision: 42701
- rebuild due to buildsystem failure
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.1.0a-12mdv2008.0
+ Revision: 22708
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0a-11mdv2007.0
+ Revision: 90977
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0a-10mdv2007.1
+ Revision: 74088
- rebuild for new vdr
- Import vdr-plugin-sysinfo

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0a-9mdv2007.0
- rebuild for new vdr

* Fri Aug 25 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0a-8mdv2007.0
- fix missing escaping

* Fri Aug 25 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0a-7mdv2007.0
- fix mangled line

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0a-6mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0a-5mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0a-4mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0a-3mdv2007.0
- use _ prefix for system path macros

* Mon Jun 05 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0a-2mdv2007.0
- rebuild for new vdr

* Sat Jun 03 2006 Anssi Hannula <anssi@mandriva.org> 0.1.0a-1mdv2007.0
- initial Mandriva release

