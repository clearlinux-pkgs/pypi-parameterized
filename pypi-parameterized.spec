#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-parameterized
Version  : 0.9.0
Release  : 4
URL      : https://files.pythonhosted.org/packages/ea/49/00c0c0cc24ff4266025a53e41336b79adaa5a4ebfad214f433d623f9865e/parameterized-0.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ea/49/00c0c0cc24ff4266025a53e41336b79adaa5a4ebfad214f433d623f9865e/parameterized-0.9.0.tar.gz
Summary  : Parameterized testing with any Python test framework
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-parameterized-license = %{version}-%{release}
Requires: pypi-parameterized-python = %{version}-%{release}
Requires: pypi-parameterized-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Parameterized testing with any Python test framework
====================================================

%package license
Summary: license components for the pypi-parameterized package.
Group: Default

%description license
license components for the pypi-parameterized package.


%package python
Summary: python components for the pypi-parameterized package.
Group: Default
Requires: pypi-parameterized-python3 = %{version}-%{release}

%description python
python components for the pypi-parameterized package.


%package python3
Summary: python3 components for the pypi-parameterized package.
Group: Default
Requires: python3-core
Provides: pypi(parameterized)

%description python3
python3 components for the pypi-parameterized package.


%prep
%setup -q -n parameterized-0.9.0
cd %{_builddir}/parameterized-0.9.0
pushd ..
cp -a parameterized-0.9.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679938739
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-parameterized
cp %{_builddir}/parameterized-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-parameterized/008678381123c1decf0bbdd31dc138f250517a46 || :
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
/usr/share/package-licenses/pypi-parameterized/008678381123c1decf0bbdd31dc138f250517a46

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
