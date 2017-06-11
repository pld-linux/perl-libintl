#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	libintl-perl
Summary:	Internationalization library for Perl
Summary(pl.UTF-8):	Biblioteka umiędzynaradawiająca Perla
Name:		perl-libintl
Version:	1.26
Release:	2
License:	LGPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/G/GU/GUIDO/%{pnam}-%{version}.tar.gz
# Source0-md5:	d355998f5f33a6f4202cd7ded7bf052a
URL:		http://search.cpan.org/dist/libintl-perl/
BuildRequires:	gdbm-devel
%{?with_tests:BuildRequires:	glibc-localedb-all}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package is an internationalization library for Perl that aims to
be compatible with the Uniforum message translations system as
implemented for example in GNU gettext.

%description -l pl.UTF-8
Pakiet stanowi bibliotekę umiędzynaradawiającą Perla, która ma na celu
zachowanie zgodności ze standardem Uniforum tłumaczenia komunikatów
zaimplementowanym na przykład w gettexcie GNU.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

# LC_ALL= LANG=... -- workaround for broken (?) gettext
%{?with_tests:LC_ALL= LANG=en_US %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Locale/{gettext_xs,libintlFAQ}.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/libintl-perl/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%dir %{perl_vendorarch}/auto/Locale/gettext_xs
%attr(755,root,root) %{perl_vendorarch}/auto/Locale/gettext_xs/gettext_xs.so
%{perl_vendorlib}/Locale/Messages.pm
%{perl_vendorlib}/Locale/Recode.pm
%{perl_vendorlib}/Locale/RecodeData.pm
%{perl_vendorlib}/Locale/TextDomain.pm
%{perl_vendorlib}/Locale/Util.pm
%{perl_vendorlib}/Locale/gettext_dumb.pm
%{perl_vendorlib}/Locale/gettext_pp.pm
%{perl_vendorlib}/Locale/gettext_xs.pm
%{perl_vendorlib}/Locale/Recode
%{perl_vendorlib}/Locale/RecodeData
%{_mandir}/man3/Locale::Messages.3pm*
%{_mandir}/man3/Locale::Recode*.3pm*
%{_mandir}/man3/Locale::TextDomain.3pm*
%{_mandir}/man3/Locale::Util.3pm*
%{_mandir}/man3/Locale::gettext_dumb.3pm*
%{_mandir}/man3/Locale::gettext_pp.3pm*
%{_mandir}/man3/Locale::gettext_xs.3pm*
%{_mandir}/man3/Locale::libintlFAQ.3pm*
