%define	name	svnchecker
%define	version	0.1.2
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Framework for Subversion pre-commit hook scripts
License:    GPL
Group:      Graphical desktop/GNOME
URL:        http://svnchecker.sourceforge.net/
Source:     http://downloads.sourceforge.net/svnchecker/%{name}-%{version}.tar.gz
BuildRequires:  python-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
SVNChecker is a framework for Subversion pre-commit hook scripts. The
SVNChecker handles Subversion (SVN) pre-commit hooks in order to implement
checks of files before they are commited. For example, you can check for the
code style or unit tests.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}
rm -f %{buildroot}%{_prefix}/config/svncheckerconfig.ini

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README svncheckerconfig.ini
%{_bindir}/Main.py
%{python_sitelib}/checks
%{python_sitelib}/handlers
%{python_sitelib}/modules
%{python_sitelib}/*.egg-info

