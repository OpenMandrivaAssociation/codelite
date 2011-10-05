%define name	codelite
%define version	3.0.0.5041
%define	release	%mkrel 1

Name:		%{name}
Version:        %{version}
Release:        %{release}
Summary:        A powerful open-source, cross platform code editor for C/C++
License:        GPLv2+
Group:          Development/Other
URL:            http://codelite.sourceforge.net
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Requires: 	wxgtk2.8 xterm
BuildRequires:	wxgtku2.8-devel
BuildRequires:	desktop-file-utils
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
CodeLite uses a sophisticated, yet intuitive interface which allows 
users to easily create, build and debug complex projects.

%prep
%setup -q

%build
%configure2_5x	--plugins-dir=%{_libdir}/%{name} \
		--disable-debian \
		--disable-desktop_icon \
		--disable-make_symlink
%{__make}

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

desktop-file-install --delete-original        \
  --copy-generic-name-to-name                 \
  --add-category="IDE"                        \
  --dir %{buildroot}/%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/codelite.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS LICENSE COPYING 
%{_bindir}/codelite
%{_bindir}/codelite_indexer
%{_bindir}/codelite_cppcheck
%{_bindir}/codelite_fix_files
%{_bindir}/codelite_exec
%{_bindir}/codelite_kill_children
%{_bindir}/codelite_xterm
%dir %{_datadir}/codelite
%{_datadir}/codelite/*
%{_datadir}/applications/codelite.desktop
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*