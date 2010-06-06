#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Set
%define		pnam	Object
Summary:	Set::Object - set of objects and strings
Summary(pl.UTF-8):	Set::Object - zbiór obiektów i łańcuchów
Name:		perl-Set-Object
Version:	1.27
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Set/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	619697cb17b709f566d4985edc9352cb
URL:		http://search.cpan.org/dist/Set-Object/
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
	CC="%{__cc}" \
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
%{perl_vendorarch}/Set
%dir %{perl_vendorarch}/auto/Set
%dir %{perl_vendorarch}/auto/Set/Object
%{perl_vendorarch}/auto/Set/Object/autosplit.ix
%{perl_vendorarch}/auto/Set/Object/Object.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Set/Object/Object.so
%{_mandir}/man3/*
