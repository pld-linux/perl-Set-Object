%include	/usr/lib/rpm/macros.perl
%define		pdir	Set
%define		pnam	Object
Summary:	Set::Object Perl module
Summary(cs):	Modul Set::Object pro Perl
Summary(da):	Perlmodul Set::Object
Summary(de):	Set::Object Perl Modul
Summary(es):	M�dulo de Perl Set::Object
Summary(fr):	Module Perl Set::Object
Summary(it):	Modulo di Perl Set::Object
Summary(ja):	Set::Object Perl �⥸�塼��
Summary(ko):	Set::Object �� ����
Summary(no):	Perlmodul Set::Object
Summary(pl):	Modu� Perla Set::Object
Summary(pt):	M�dulo de Perl Set::Object
Summary(pt_BR):	M�dulo Perl Set::Object
Summary(ru):	������ ��� Perl Set::Object
Summary(sv):	Set::Object Perlmodul
Summary(uk):	������ ��� Perl Set::Object
Summary(zh_CN):	Set::Object Perl ģ��
Name:		perl-Set-Object
Version:	1.02
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set::Object perl module.

%description -l cs
Modul Set::Object pro Perl.

%description -l da
Perlmodul Set::Object.

%description -l de
Set::Object Perl Modul.

%description -l es
M�dulo de Perl Set::Object.

%description -l fr
Module Perl Set::Object.

%description -l it
Modulo di Perl Set::Object.

%description -l ja
Set::Object Perl �⥸�塼��

%description -l ko
Set::Object �� ����.

%description -l no
Perlmodul Set::Object.

%description -l pl
Modu� perla Set::Object.

%description -l pt
M�dulo de Perl Set::Object.

%description -l pt_BR
M�dulo Perl Set::Object.

%description -l ru
������ ��� Perl Set::Object.

%description -l sv
Set::Object Perlmodul.

%description -l uk
������ ��� Perl Set::Object.

%description -l zh_CN
Set::Object Perl ģ��

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Set
#%{perl_sitearch}/Set/Object.pm
%dir %{perl_sitearch}/auto/Set
%dir %{perl_sitearch}/auto/Set/Object
%{perl_sitearch}/auto/Set/Object/Object.bs
%attr(755,root,root) %{perl_sitearch}/auto/Set/Object/Object.so
%{_mandir}/man3/*
