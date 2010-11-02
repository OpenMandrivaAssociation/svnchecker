%define	name	svnchecker
%define	version	0.3
%define	release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Framework for Subversion pre-commit hook scripts
License:    GPL
Group:      Graphical desktop/GNOME
URL:        http://svnchecker.tigris.org/
Source:     http://svnchecker.tigris.org/files/documents/6233/42081/%{name}-%{version}.tar.gz
Patch:      svnchecker-0.2-no-config-file.patch
BuildRequires:  python-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE
%{_bindir}/Main.py
%{python_sitelib}/checks
%{python_sitelib}/handlers
%{python_sitelib}/modules
%{python_sitelib}/*.egg-info

