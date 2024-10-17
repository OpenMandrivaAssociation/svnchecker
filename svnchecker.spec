# This is a very old program, it's e3asier to drop it than debug if smth goes wrong
%define debug_package %{nil}

Name:		svnchecker
Version:	0.3
Release:	6
Summary:    Framework for Subversion pre-commit hook scripts
License:    GPL
Group:      Graphical desktop/GNOME
URL:        https://svnchecker.tigris.org/
Source:     http://svnchecker.tigris.org/files/documents/6233/42081/%{name}-%{version}.tar.gz
Patch:      svnchecker-0.2-no-config-file.patch
BuildRequires:  python-devel

%description
SVNChecker is a framework for Subversion pre-commit hook scripts. The
SVNChecker handles Subversion (SVN) pre-commit hooks in order to implement
checks of files before they are commited. For example, you can check for the
code style or unit tests.

%prep
%setup -q
%patch -p 1

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc README LICENSE
%{_bindir}/Main.py
%{python_sitelib}/checks
%{python_sitelib}/handlers
%{python_sitelib}/modules
%{python_sitelib}/*.egg-info
