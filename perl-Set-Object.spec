#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Set
%define		pnam	Object
Summary:	Set::Object Perl module
Summary(cs.UTF-8):	Modul Set::Object pro Perl
Summary(da.UTF-8):	Perlmodul Set::Object
Summary(de.UTF-8):	Set::Object Perl Modul
Summary(es.UTF-8):	Módulo de Perl Set::Object
Summary(fr.UTF-8):	Module Perl Set::Object
Summary(it.UTF-8):	Modulo di Perl Set::Object
Summary(ja.UTF-8):	Set::Object Perl モジュール
Summary(ko.UTF-8):	Set::Object 펄 모줄
Summary(nb.UTF-8):	Perlmodul Set::Object
Summary(pl.UTF-8):	Moduł Perla Set::Object
Summary(pt.UTF-8):	Módulo de Perl Set::Object
Summary(pt_BR.UTF-8):	Módulo Perl Set::Object
Summary(ru.UTF-8):	Модуль для Perl Set::Object
Summary(sv.UTF-8):	Set::Object Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Set::Object
Summary(zh_CN.UTF-8):	Set::Object Perl 模块
Name:		perl-Set-Object
Version:	1.21
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	db0c657333f65000e1d85ba59dd2320d
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Set::Object Perl module implements a Set of objects, that is, a
collection of objects without duplications. It is similar to a
Smalltalk IdentitySet.

%description -l pl.UTF-8
Moduł Perla Set::Object implementuje zbiór obiektów, tzn. zestaw
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
%doc Changes*
%{perl_vendorarch}/%{pdir}
%dir %{perl_vendorarch}/auto/%{pdir}
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/autosplit.ix
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/%{pnam}.bs
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/%{pnam}.so
%{_mandir}/man3/*
