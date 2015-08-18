#
# spec file for package python-pyOpenSSL
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           python-pyOpenSSL
Version:        0.14.1
Release:        0
Url:            http://launchpad.net/pyopenssl
Summary:        Python wrapper module around the OpenSSL library
License:        Apache-2.0
Group:          Development/Python
Source:         http://pypi.python.org/packages/source/p/pyOpenSSL/pyOpenSSL-%{version}.tar.gz
Source1001: 	python-pyOpenSSL.manifest
BuildRequires:  libopenssl-devel
BuildRequires:  python-devel
BuildRequires:  python-setuptools
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%description
High-level wrapper around a subset of the OpenSSL library, includes
 * SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 * Callbacks written in Python
 * Extensive error-handling mechanism, mirroring OpenSSL's error codes
...  and much more ;)

%prep
%setup -q -n pyOpenSSL-%{version}
cp %{SOURCE1001} .

%build
CFLAGS="%{optflags} -fno-strict-aliasing" python setup.py build

%install
python setup.py install --prefix=%{_prefix} --install-lib=%{python_sitearch} --root=%{buildroot}

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{python_sitearch}/*

%changelog
