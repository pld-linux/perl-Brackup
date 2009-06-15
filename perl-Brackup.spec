#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Brackup
Summary:	Brackup - flexible backup tool: slices, dices, encrypts, and sprays across the net
Summary(pl.UTF-8):	Brackup - elastyczne narzędzie backupowe: rozdziela, szyfruje i rozprzestrzenia po sieci
Name:		perl-Brackup
Version:	1.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/B/BR/BRADFITZ/%{pdir}-%{version}.tar.gz
# Source0-md5:	5eaf819f91843d47fdbf300f4d31bbf8
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
Brackup is a backup tool, written in Perl, flexible. It slices, dices,
encrypts and sprays across the net.

%description -l pl.UTF-8
Brackup to elastyczne narzędzie do tworzenia kopii zapasowych napisane
w Perlu. Rozdziela, szyfruje i rozprzestrzenia dane po sieci.

%package Target-Amazon
Summary:	Brackup-Target-Amazon - target for amazon
Summary(pl.UTF-8):	Brackup-Target-Amazon - obsługa amazona
Group:		Development/Languages/Perl

%description Target-Amazon
Brackup-Target-Amazon - target for amazon.

%description Target-Amazon -l pl.UTF-8
Brackup-Target-Amazon - obsługa amazona.

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
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/*.pm
%dir %{perl_vendorlib}/Brackup
%{perl_vendorlib}/Brackup/*.pm
%dir %{perl_vendorlib}/Brackup/Chunker
%{perl_vendorlib}/Brackup/Chunker/Default.pm
%{perl_vendorlib}/Brackup/Chunker/MP3.pm
%dir %{perl_vendorlib}/Brackup/Target
%{perl_vendorlib}/Brackup/Target/CloudFiles.pm
%{perl_vendorlib}/Brackup/Target/Filebased.pm
%{perl_vendorlib}/Brackup/Target/Filesystem.pm
%{perl_vendorlib}/Brackup/Target/Ftp.pm
%{perl_vendorlib}/Brackup/Target/Sftp.pm
%dir %{perl_vendorlib}/Brackup/Manual
%{perl_vendorlib}/Brackup/Manual/Overview.pod
%dir %{perl_vendorlib}/Brackup/Dict
%{perl_vendorlib}/Brackup/Dict/*.pm
%{_mandir}/man1/*
%{_mandir}/man3/Brackup::Target::Filesystem.3pm*
%{_mandir}/man3/Brackup.3pm*
%{_mandir}/man3/Brackup::Target.3pm*
%{_mandir}/man3/Brackup::Config.3pm*
%{_mandir}/man3/Brackup::DigestCache.3pm*
%{_mandir}/man3/Brackup::InventoryDatabase.3pm*
%{_mandir}/man3/Brackup::Manual::Overview.3pm*
%{_mandir}/man3/Brackup::Root.3pm*
%{_mandir}/man3/Brackup::Chunker::MP3.3pm*
%{_mandir}/man3/Brackup::Mount.3pm*
%{_mandir}/man3/Brackup::Target::CloudFiles.3pm*
%{_mandir}/man3/Brackup::Target::Ftp.3pm*
%{_mandir}/man3/Brackup::Target::Sftp.3pm*

%files Target-Amazon
%defattr(644,root,root,755)
%{perl_vendorlib}/Brackup/Target/Amazon.pm
%{_mandir}/man3/Brackup::Target::Amazon*
