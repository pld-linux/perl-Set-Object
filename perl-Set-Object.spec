#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Set
%define	pnam	Object
Summary:	Set::Object Perl module
Summary(cs):	Modul Set::Object pro Perl
Summary(da):	Perlmodul Set::Object
Summary(de):	Set::Object Perl Modul
Summary(es):	Módulo de Perl Set::Object
Summary(fr):	Module Perl Set::Object
Summary(it):	Modulo di Perl Set::Object
Summary(ja):	Set::Object Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Set::Object ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Set::Object
Summary(pl):	Modu³ Perla Set::Object
Summary(pt):	Módulo de Perl Set::Object
Summary(pt_BR):	Módulo Perl Set::Object
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Set::Object
Summary(sv):	Set::Object Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Set::Object
Summary(zh_CN):	Set::Object Perl Ä£¿é
Name:		perl-Set-Object
Version:	1.06
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b2ec55614d9d2396a8a1196cfc7b8328
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Set::Object Perl module implements a Set of objects, that is, a
collection of objects without duplications. It is similar to a
Smalltalk IdentitySet.

%description -l pl
Modu³ Perla Set::Object implementuje zbiór obiektów, tzn. zestaw
obiektów bez duplikatów. Jest on podobny do IdentitySet Smalltalka.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/%{pdir}
%dir %{perl_vendorarch}/auto/%{pdir}
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/autosplit.ix
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/%{pnam}.bs
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/%{pnam}.so
%{_mandir}/man3/*
