Name:           perl-CGI-Session
Version:        4.35
Release:        5%{?dist}.goose.1
Summary:        Persistent session data in CGI applications
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CGI-Session/
Source0:        http://www.cpan.org/modules/by-module/CGI/CGI-Session-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:	perl(FreezeThaw), perl(ExtUtils::MakeMaker), perl(Test::More)
BuildRequires:	perl-CPAN

%description
CGI-Session is a Perl5 library that provides an easy, reliable and modular
session management system across HTTP requests. Persistency is a key
feature for such applications as shopping carts, login/authentication
routines, and application that need to carry data across HTTP requests.
CGI::Session does that and many more.

%prep
%setup -q -n CGI-Session-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
chmod 644 examples/*

%install
rm -rf %{buildroot}

make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jan 6 2012 Ivan Makfinsky <makfinsky@gooseproject.org> - 4.35-5.goose.1
- Added perl-CPAN as a buildrequires

* Fri Apr 30 2010 Marcela Mašláňová <mmaslano@redhat.com> - 4.35-5
- add package into RHEL-6
- Resolves: rhbz#463667

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 4.35-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug  1 2008 Andreas Thienemann <athienem@redhat.com> 4.35-1
- update to current 4.35, 4.31 release was broken.

* Fri Aug  1 2008 Andreas Thienemann <athienem@redhat.com> 4.31-1
- update to 4.31

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4.20-4
- rebuild for new perl

* Sun Jan 27 2008 Andreas Thienemann <andreas@bawue.net> 4.20-3
- Added Test::More to the BuildReqs

* Sat Mar 17 2007 Andreas Thienemann <andreas@bawue.net> 4.20-2
- Fixed perl-devel req

* Sat Mar 10 2007 Andreas Thienemann <andreas@bawue.net> 4.20-1
- Cleaned up for FE
- Specfile autogenerated by cpanspec 1.69.1.
