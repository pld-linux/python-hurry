# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		hurry
%define		egg_name	hurry
%define		pypi_name	hurry
Summary:	Hurry! helps you run your routine commands and scripts faster
Name:		python-%{pypi_name}
Version:	1.0
Release:	1
License:	???
Group:		Libraries/Python
Source0:	https://pypi.debian.net/%{pypi_name}/hurry-%{version}.tar.gz
# Source0-md5:	a140ee4961cd656708c402a47c56251b
URL:		https://pypi.org/project/hurry/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hurry! helps you run your routine commands and scripts faster.

%package -n python3-%{pypi_name}
Summary:	Hurry! helps you run your routine commands and scripts faster
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{pypi_name}
Hurry! helps you run your routine commands and scripts faster.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

# when files are installed in other way that standard 'setup.py
# they need to be (re-)compiled
# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/hurry
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
