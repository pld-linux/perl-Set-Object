Summary:	Set-Object perl module
Summary(pl):	Modu� perla Set-Object
Name:		perl-Set-Object
Version:	0.003
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Set/Set-Object-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Set-Object perl module. 

%description -l pl
Modu� perla Set-Object.

%prep
%setup -q -n Set-Object-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Set/Object/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Set/Object
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitearch}/Set/Object.pm

%dir %{perl_sitearch}/auto/Set/Object
%{perl_sitearch}/auto/Set/Object/.packlist
%{perl_sitearch}/auto/Set/Object/autosplit.ix
%{perl_sitearch}/auto/Set/Object/Object.bs
%attr(755,root,root) %{perl_sitearch}/auto/Set/Object/Object.so

%{_mandir}/man3/*
