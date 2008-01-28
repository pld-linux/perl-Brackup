#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Brackup
Summary:	Brackup - Flexible backup tool.  Slices, dices, encrypts, and sprays across the net.
#Summary(pl.UTF-8):	
Name:		perl-Brackup
Version:	1.06
Release:	1
# same as perl 
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/B/BR/BRADFITZ/Brackup-1.06.tar.gz
# Source0-md5:	23f3a3a20ed5a1ca64626c3b1af30a4b
URL:		http://search.cpan.org/dist/Brackup/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-DBD-SQLite
BuildRequires:	perl-DBI
BuildRequires:	perl-Digest-SHA1
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Backup tool, written in perl, flexible.

# %description -l pl.UTF-8
# TODO

%package Target-Amazon
Summary:	Brackup-Target-Amazon - target for amazon
Group:		Development/Languages/Perl

%description Target-Amazon

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes doc/* TODO
%{perl_vendorlib}/*.pm
%dir %{perl_vendorlib}/Brackup/
%{perl_vendorlib}/Brackup/*.pm
%dir %{perl_vendorlib}/Brackup/Target
%{perl_vendorlib}/Brackup/Target/Filesystem.pm
%dir %{perl_vendorlib}/Brackup/Manual
%{perl_vendorlib}/Brackup/Manual/Overview.pod
%dir %{perl_vendorlib}/Brackup/Dict
%{perl_vendorlib}/Brackup/Dict/*.pm
%{_mandir}/man3/Brackup::Target::Filesystem.3pm*
%{_mandir}/man3/Brackup.3pm*
%{_mandir}/man3/Brackup::Target.3pm*
%{_mandir}/man3/Brackup::Config.3pm*
%{_mandir}/man3/Brackup::DigestCache.3pm*
%{_mandir}/man3/Brackup::InventoryDatabase.3pm*
%{_mandir}/man3/Brackup::Manual::Overview.3pm*
%{_mandir}/man3/Brackup::Root.3pm*
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*

%files Target-Amazon
%defattr(644,root,root,755)
%{perl_vendorlib}/Brackup/Target/Amazon.pm
%{_mandir}/man3/Brackup::Target::Amazon*
