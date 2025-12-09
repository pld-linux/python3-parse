#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	parse() - the opposite of format()
Summary(pl.UTF-8):	parse() - odwrotność format()
Name:		python3-parse
Version:	1.20.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/parse/
Source0:	https://files.pythonhosted.org/packages/source/p/parse/parse-%{version}.tar.gz
# Source0-md5:	129951f4c2cece0ca6df437b522391e3
URL:		https://pypi.org/project/parse/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools >= 1:61.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parse strings using a specification based on the Python format()
syntax.

%description -l pl.UTF-8
Rozkład łańcuchów znaków przy użyciu specyfikacji opartej na składni
pythonowej metody format().

%prep
%setup -q -n parse-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/parse.py
%{py3_sitescriptdir}/__pycache__/parse.cpython-*.py[co]
%{py3_sitescriptdir}/parse-%{version}.dist-info
