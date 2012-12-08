%define oname	pycrypto

Summary:	Python interface to various crypto algorithms and protocols
Name:		python-%{oname}
Version:	2.3
Release:	%mkrel 4
Source0:	http://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/%{oname}-%{version}.tar.gz
Source1:	http://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/%{oname}-%{version}.tar.gz.asc
Patch0:		pycrypto-2.1.0-64bit.patch
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
%patch0 -p0 -b .64bit
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




%changelog
* Tue Feb 21 2012 abf
- The release updated by ABF

* Thu May 05 2011 Funda Wang <fwang@mandriva.org> 2.3-3mdv2011.0
+ Revision: 669075
- fix linkage

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Mon Nov 01 2010 Jani Välimaa <wally@mandriva.org> 2.3-2mdv2011.0
+ Revision: 591709
- rebuild for python 2.7

* Sun Sep 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.3-1mdv2011.0
+ Revision: 577728
- update to new version 2.3

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.2-1mdv2011.0
+ Revision: 569671
- update to new version 2.2

  + Crispin Boylan <crisb@mandriva.org>
    - Fix description

* Fri Feb 12 2010 Crispin Boylan <crisb@mandriva.org> 2.1.0-1mdv2010.1
+ Revision: 505117
- New release
- Remove applied patches
- Rediff patch1

* Mon Mar 09 2009 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-8mdv2009.1
+ Revision: 353219
- P2: security fix for CVE-2009-0544

* Tue Feb 17 2009 Crispin Boylan <crisb@mandriva.org> 2.0.1-7mdv2009.1
+ Revision: 341346
- Patch1: Fix python2.6 deprecation warnings

* Thu Jan 29 2009 Lev Givon <lev@mandriva.org> 2.0.1-6mdv2009.1
+ Revision: 335379
- Obsolete current release of pycrypto.

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 2.0.1-5mdv2009.1
+ Revision: 318613
- rebuild for python 2.6

* Tue Sep 09 2008 Adam Williamson <awilliamson@mandriva.org> 2.0.1-4mdv2009.0
+ Revision: 282882
- import python-pycrypto


