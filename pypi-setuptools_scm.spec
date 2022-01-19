#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-setuptools_scm
Version  : 6.4.2
Release  : 112
URL      : https://files.pythonhosted.org/packages/4a/18/477d3d9eb2f88230ff2a41de9d8ffa3554b706352787d289f57f76bfba0b/setuptools_scm-6.4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/4a/18/477d3d9eb2f88230ff2a41de9d8ffa3554b706352787d289f57f76bfba0b/setuptools_scm-6.4.2.tar.gz
Summary  : the blessed package to manage your versions by scm tags
Group    : Development/Tools
License  : MIT
Requires: pypi-setuptools_scm-license = %{version}-%{release}
Requires: pypi-setuptools_scm-python = %{version}-%{release}
Requires: pypi-setuptools_scm-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : git
BuildRequires : mercurial
BuildRequires : pypi(lz4)
BuildRequires : pypi(packaging)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(tomli)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pip
BuildRequires : pypi-pytest
BuildRequires : pypi-virtualenv

%description
setuptools_scm
==============
``setuptools_scm`` extract Python package versions from ``git`` or
``hg`` metadata instead of declaring them as the version argument
or in a SCM managed file.

%package license
Summary: license components for the pypi-setuptools_scm package.
Group: Default

%description license
license components for the pypi-setuptools_scm package.


%package python
Summary: python components for the pypi-setuptools_scm package.
Group: Default
Requires: pypi-setuptools_scm-python3 = %{version}-%{release}

%description python
python components for the pypi-setuptools_scm package.


%package python3
Summary: python3 components for the pypi-setuptools_scm package.
Group: Default
Requires: python3-core
Provides: pypi(setuptools_scm)
Requires: pypi(packaging)
Requires: pypi(setuptools)
Requires: pypi(tomli)

%description python3
python3 components for the pypi-setuptools_scm package.


%prep
%setup -q -n setuptools_scm-6.4.2
cd %{_builddir}/setuptools_scm-6.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642608108
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pytest --verbose || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-setuptools_scm
cp %{_builddir}/setuptools_scm-6.4.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-setuptools_scm/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-setuptools_scm/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
