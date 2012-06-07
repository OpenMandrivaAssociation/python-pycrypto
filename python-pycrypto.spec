%define oname	pycrypto

Summary:	Python interface to various crypto algorithms and protocols
Name:		python-%{oname}
Version:	2.6
Release:	1
Source0:	http://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/%{oname}-%{version}.tar.gz
Source1:	http://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/%{oname}-%{version}.tar.gz.asc
Patch1:		pycrypto-2.3-link.patch
License:	Public Domain
Group:		Development/Python
URL:		http://www.pycrypto.org
BuildRequires:	python-devel >= 2.2
BuildRequires:	gmp-devel
Requires:	python >= 2.2
BuildRoot:	%{_tmppath}/%{oname}-%{version}-%{release}-buildroot
Obsoletes:	pycrypto =< %{version}-%{release}
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

%prep
%setup -q -n %{oname}-%{version}
%patch1 -p0 -b .link

perl -pi -e 's|/usr/local/bin/|%{_bindir}/|' Util/RFC1751.py 

%build
CFLAGS="%{optflags}" python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --compile --optimize=2

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README COPYRIGHT TODO
%{py_platsitedir}/*


