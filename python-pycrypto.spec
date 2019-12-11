%define oname	pycrypto

Summary:	Python interface to various crypto algorithms and protocols
Name:		python-%{oname}
Version:	2.6.1
Release:	4
License:	Public Domain
Group:		Development/Python
Url:		http://www.pycrypto.org
Source0:	http://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/%{oname}-%{version}.tar.gz
Source1:	http://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/%{oname}-%{version}.tar.gz.asc
Patch1:		pycrypto-2.6-link.patch
BuildRequires:	gmp-devel
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)
Requires:	python >= 3.0
Provides:	pycrypto = %{version}-%{release}

%description
The Toolkit is a collection of cryptographic algorithms and protocols,
implemented for use from Python. Among the contents of the package:

 * Hash functions: MD2, MD4, RIPEMD.
 * Block encryption algorithms: AES, ARC2, Blowfish, CAST, DES, Triple-
   DES, IDEA, RC5.
 * Stream encryption algorithms: ARC4, simple XOR.
 * Public-key algorithms: RSA, DSA, ElGamal, qNEW.
 * Protocols: All-or-nothing transforms, chaffing/winnowing.
 * Miscellaneous: RFC1751 module for converting 128-key keys into a set
   of English words, primality testing.
 * Some demo programs (currently all quite old and outdated).

%package -n python2-%{oname}
Summary:	Python 2.x interface to various crypto algorithms and protocols
Group:		Development/Python
Requires:	python2

%description -n python2-%{oname}
The Toolkit is a collection of cryptographic algorithms and protocols,
implemented for use from Python. Among the contents of the package:

 * Hash functions: MD2, MD4, RIPEMD.
 * Block encryption algorithms: AES, ARC2, Blowfish, CAST, DES, Triple-
   DES, IDEA, RC5.
 * Stream encryption algorithms: ARC4, simple XOR.
 * Public-key algorithms: RSA, DSA, ElGamal, qNEW.
 * Protocols: All-or-nothing transforms, chaffing/winnowing.
 * Miscellaneous: RFC1751 module for converting 128-key keys into a set
   of English words, primality testing.
 * Some demo programs (currently all quite old and outdated).

%prep
%setup -qn %{oname}-%{version}
%patch1 -p0 -b .link

# Make debuginfo files readable
find . -name "*.c" -o -name "*.h" |xargs chmod 0644

mkdir python2
mv `ls |grep -v python2` python2
cp -a python2 python3

%build
%setup_compile_flags
cd python2
CFLAGS="%{optflags}" python2 setup.py build

cd ../python3
CFLAGS="%{optflags}" python3 setup.py build

%install
cd python2
python2 setup.py install --root=%{buildroot} --compile --optimize=2

cd ../python3
python3 setup.py install --root=%{buildroot} --compile --optimize=2

%files -n python2-%{oname}
%doc python2/ChangeLog python2/README python2/COPYRIGHT python2/TODO
%{py2_platsitedir}/*

%files
%doc python3/ChangeLog python3/README python3/COPYRIGHT python3/TODO
%{py3_platsitedir}/*
