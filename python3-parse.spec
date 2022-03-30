#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	parse() - the opposite of format()
Summary(pl.UTF-8):	parse() - odwrotność format()
Name:		python3-parse
Version:	1.19.0
Release:	5
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/parse/
Source0:	https://files.pythonhosted.org/packages/source/p/parse/parse-%{version}.tar.gz
# Source0-md5:	15e1e590c964254ac5fbea308a6ec6d4
URL:		https://pypi.org/project/parse/
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
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
%py3_build

%if %{with tests}
%{__python3} test_parse.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/parse.py
%{py3_sitescriptdir}/__pycache__/parse.cpython-*.py[co]
%{py3_sitescriptdir}/parse-%{version}-py*.egg-info
