%define	pdir	Set
%define	pnam	Object
%include	/usr/lib/rpm/macros.perl
Summary:	Set-Object perl module
Summary(pl):	Modu³ perla Set-Object
Name:		perl-Set-Object
Version:	1.02
Release:	4

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set-Object perl module.

%description -l pl
Modu³ perla Set-Object.

%prep
%setup -q -n Set-Object-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Set/Object.pm
%dir %{perl_sitearch}/auto/Set/Object
%{perl_sitearch}/auto/Set/Object/autosplit.ix
%{perl_sitearch}/auto/Set/Object/Object.bs
%attr(755,root,root) %{perl_sitearch}/auto/Set/Object/Object.so
%{_mandir}/man3/*
