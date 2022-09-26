%global _cmake_skip_rpath %{nil}

Summary:	A powerful open-source, cross platform code editor for C/C++
Name:		codelite
Version:	16.0.0
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		https://codelite.org/
Source0:	https://github.com/eranif/codelite/archive/refs/tags/%{version}.tar.gz
Source10:	%{name}.rpmlintrc
Patch0:		codelite-5.4-desktop.patch
Patch1:		codelite-16.0-compile.patch
Patch2:		codelite-5.4-libdir.patch
BuildRequires:	cmake ninja
BuildRequires:	wxgtku3.2-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libssh)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(atk)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
Requires:	xterm

%description
CodeLite uses a sophisticated, yet intuitive interface which allows
users to easily create, build and debug complex projects.

%files -f %{name}.lang
%doc AUTHORS LICENSE COPYING
%{_bindir}/codelite
%{_bindir}/codelite-make
%{_bindir}/codelite-terminal
%{_bindir}/codelite_cppcheck
%{_bindir}/codelite_fix_files
%{_bindir}/codelite_exec
%{_bindir}/codelite_kill_children
%{_bindir}/codelite_xterm
%{_bindir}/codelite-cc
%{_bindir}/codelite-ctags
%{_bindir}/codelite-echo
%{_bindir}/codelite-lldb
%{_bindir}/codelite-lsp-helper
%{_bindir}/codelite-remote
%{_bindir}/codelite_open_helper.py
%{_bindir}/ctagsd
%{_bindir}/ctagsd-tests
%{_datadir}/icons/hicolor/*/apps/codelite.png
%{_mandir}/man1/codelite-make.1*
%{_mandir}/man1/codelite.1*
%{_mandir}/man1/codelite_fix_files.1*
%{_mandir}/man1/codelite_open_helper.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_libdir}/%{name}/

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake \
	-DPREFIX:PATH=%{_prefix} \
	-DCL_INSTALL_LIBDIR=%{_lib} \
	-DCMAKE_SKIP_RPATH:BOOL=OFF \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name}

# To fix unstripped-binary-or-object
chmod 0755 %{buildroot}%{_libdir}/%{name}/*.so
