#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-setuptools_scm
Version  : 7.1.0
Release  : 128
URL      : https://files.pythonhosted.org/packages/98/12/2c1e579bb968759fc512391473340d0661b1a8c96a59fb7c65b02eec1321/setuptools_scm-7.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/98/12/2c1e579bb968759fc512391473340d0661b1a8c96a59fb7c65b02eec1321/setuptools_scm-7.1.0.tar.gz
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
BuildRequires : pypi(typing_extensions)
BuildRequires : pypi-pip
BuildRequires : pypi-pytest
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
setuptools_scm
==============
``setuptools_scm`` extracts Python package versions from ``git`` or
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
Requires: pypi(typing_extensions)

%description python3
python3 components for the pypi-setuptools_scm package.


%prep
%setup -q -n setuptools_scm-7.1.0
cd %{_builddir}/setuptools_scm-7.1.0
pushd ..
cp -a setuptools_scm-7.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695156307
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pytest --verbose || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-setuptools_scm
cp %{_builddir}/setuptools_scm-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-setuptools_scm/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
