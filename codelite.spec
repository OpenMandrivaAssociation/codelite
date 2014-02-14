Summary:	A powerful open-source, cross platform code editor for C/C++
Name:		codelite
Version:	5.4
Release:	2
License:	GPLv2+
Group:		Development/Other
Url:		http://codelite.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}-gtk.src.tar.gz
Source10:	%{name}.rpmlintrc
Patch0:		codelite-5.4-desktop.patch
Patch1:		codelite-5.4-linkage.patch
Patch2:		codelite-5.4-libdir.patch
BuildRequires:	cmake
BuildRequires:	wxgtku3.0-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libssh)
BuildRequires:	pkgconfig(pangoxft)
Requires:	wxgtk3.0
Requires:	xterm

%description
CodeLite uses a sophisticated, yet intuitive interface which allows
users to easily create, build and debug complex projects.

%files -f %{name}.lang
%doc AUTHORS LICENSE COPYING
%{_bindir}/clg++
%{_bindir}/clgcc
%{_bindir}/codelite
%{_bindir}/codelite-clang
%{_bindir}/codelite-make
%{_bindir}/codelite-terminal
%{_bindir}/codelite_indexer
%{_bindir}/codelite_cppcheck
%{_bindir}/codelite_fix_files
%{_bindir}/codelite_exec
%{_bindir}/codelite_kill_children
%{_bindir}/codelite_xterm
%{_bindir}/codelitegcc
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_libdir}/%{name}/

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%cmake \
	-DPREFIX:PATH=%{_prefix} \
	-DCL_INSTALL_LIBDIR=%{_lib}
%make

%install
%makeinstall_std -C build

%find_lang %{name}

# To fix unstripped-binary-or-object
chmod 0755 %{buildroot}%{_libdir}/%{name}/*.so

