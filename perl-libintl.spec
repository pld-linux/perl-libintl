#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	libintl-perl
Summary:	Internationalization library for Perl
Summary(pl):	Biblioteka umi�dzynaradawiaj�ca Perla
Name:		perl-libintl
Version:	1.16
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/G/GU/GUIDO/%{pnam}-%{version}.tar.gz
# Source0-md5:	7dfcd9ac3a4ff41038a2c67a733d42b9
Patch0:		%{name}-kill_libiconv.patch
%{?with_tests:BuildRequires:	glibc-localedb-all}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package is an internationalization library for Perl that aims to
be compatible with the Uniforum message translations system as
implemented for example in GNU gettext.

%description -l pl
Pakiet stanowi bibliotek� umi�dzynaradawiaj�c� Perla, kt�ra ma na celu
zachowanie zgodno�ci ze standardem Uniforum t�umaczenia komunikat�w
zaimplementowanym na przyk�ad w gettexcie GNU.

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	OPTIMIZE="%{rpmcflags}"
%{__make}

# LC_ALL= LANG=... -- workaround for broken (?) gettext
%{?with_tests:LC_ALL= LANG=en_US %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BULD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BULD_ROOT%{perl_vendorarch}/auto/libintl-perl/.packlist
rm -f $RPM_BULD_ROOT%{perl_vendorlib}/Locale/gettext_xs.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%dir %{perl_vendorarch}/auto/Locale/gettext_xs
%attr(755,root,root) %{perl_vendorarch}/auto/Locale/gettext_xs/*.so
%{perl_vendorarch}/auto/Locale/gettext_xs/gettext_xs.bs
%{perl_vendorlib}/Locale/*.pm
%{perl_vendorlib}/Locale/Recode
%{perl_vendorlib}/Locale/RecodeData
%{_mandir}/man3/*
