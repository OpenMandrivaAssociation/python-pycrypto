%define oname	pycrypto

Summary:	Python interface to various crypto algorithms and protocols
Name:		python-%{oname}
Version:	2.0.1
Release:	%mkrel 8
Source0:	http://www.amk.ca/files/python/crypto/%{oname}-%{version}.tar.gz
Source1:	http://www.amk.ca/files/python/crypto/%{oname}-%{version}.sig
Patch0:		pycrypto-1.9a6-64bit.patch
Patch1:		pycrypto-2.0.1-python2.6.patch
Patch2:		pycrypto-CVE-2009-0544.patch
License:	Public Domain
Group:		Development/Python
URL:		http://www.amk.ca/python/code/crypto.html
BuildRequires:	python-devel >= 2.2
BuildRequires:	gmp-devel
Requires:	python >= 2.2
BuildRoot:	%{_tmppath}/%{oname}-%{version}-%{release}-buildroot
Obsoletes:	pycrypto =< %{version}-%{release}
Provides:	pycrypto = %{version}-%{release}

%description
The Toolkit is a collection of cryptographic algorithms and protocols,
implemented for use from Python. The current release is 1.9alpha6. Among
the contents of the package:

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
%patch0 -p1 -b .64bit
%patch1 -p1 -b .python2.6
%patch2 -p1 -b .CVE-2009-0544

perl -pi -e 's|/usr/local/bin/|%{_bindir}/|' Util/RFC1751.py 

%build
CFLAGS="%{optflags}" python setup.py build
python test.py

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --compile --optimize=2

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README LICENSE README TODO
%{py_platsitedir}/*


