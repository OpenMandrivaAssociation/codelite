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

