#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Set
%define		pnam	Object
Summary:	Set::Object Perl module
Summary(cs):	Modul Set::Object pro Perl
Summary(da):	Perlmodul Set::Object
Summary(de):	Set::Object Perl Modul
Summary(es):	Módulo de Perl Set::Object
Summary(fr):	Module Perl Set::Object
Summary(it):	Modulo di Perl Set::Object
Summary(ja):	Set::Object Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Set::Object ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Set::Object
Summary(pl):	Modu³ Perla Set::Object
Summary(pt):	Módulo de Perl Set::Object
Summary(pt_BR):	Módulo Perl Set::Object
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Set::Object
Summary(sv):	Set::Object Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Set::Object
Summary(zh_CN):	Set::Object Perl Ä£¿é
Name:		perl-Set-Object
Version:	1.02
Release:	7
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
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
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitearch}/Set
%dir %{perl_sitearch}/auto/Set
%dir %{perl_sitearch}/auto/Set/Object
%{perl_sitearch}/auto/Set/Object/autosplit.ix
%{perl_sitearch}/auto/Set/Object/Object.bs
%attr(755,root,root) %{perl_sitearch}/auto/Set/Object/Object.so
%{_mandir}/man3/*
