Name:		codelite
Version:	3.5.5375
Release:	%mkrel 1
Summary:	A powerful open-source, cross platform code editor for C/C++
License:	GPLv2+
Group:		Development/Other
URL:		http://codelite.sourceforge.net
Source:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}-gtk.src.tar.gz
Patch0:		codelite-3.5.5375-link.patch
BuildRequires:	wxgtku2.8-devel
BuildRequires:	desktop-file-utils
Requires:	wxgtk2.8
Requires:	xterm


%description
CodeLite uses a sophisticated, yet intuitive interface which allows 
users to easily create, build and debug complex projects.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x	--plugins-dir=%{_libdir}/%{name} \
		--disable-debian \
		--disable-desktop_icon \
		--disable-make_symlink
%__make

%install
%__rm -rf %{buildroot}
%makeinstall_std

desktop-file-install --delete-original        \
  --copy-generic-name-to-name                 \
  --add-category="IDE"                        \
  --dir %{buildroot}/%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/codelite.desktop

%clean
%__rm -rf %{buildroot}

%files
%doc AUTHORS LICENSE COPYING
%{_bindir}/codelite
%{_bindir}/codelite_indexer
%{_bindir}/codelite_cppcheck
%{_bindir}/codelite_fix_files
%{_bindir}/codelite_exec
%{_bindir}/codelite_kill_children
%{_bindir}/codelite_xterm
%{_datadir}/codelite
%{_datadir}/applications/codelite.desktop
%{_libdir}/%{name}



%changelog
* Tue Mar 13 2012 Andrey Bondrov <abondrov@mandriva.org> 3.5.5375-1mdv2011.0
+ Revision: 784503
- New version 3.5.5375

* Wed Oct 05 2011 Andrey Bondrov <abondrov@mandriva.org> 3.0.0.5041-1
+ Revision: 703068
- New version: 3.0.0.5041

* Sun Dec 05 2010 Yuri Myasoedov <omerta13@mandriva.org> 2.8.0.4537-1mdv2011.0
+ Revision: 610614
- New version 2.8.0.4537

* Sun Sep 05 2010 Yuri Myasoedov <omerta13@mandriva.org> 2.7.0.4375-1mdv2011.0
+ Revision: 576060
- New version 2.7.0.4368

* Wed Aug 11 2010 Yuri Myasoedov <omerta13@mandriva.org> 2.6.0.4189-1mdv2011.0
+ Revision: 569106
- initial


