#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	libintl-perl
Summary:	Internationalization library for Perl
Summary(pl):	Biblioteka umiêdzynaradawiaj±ca Perla
Name:		perl-libintl
Version:	1.11
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/G/GU/GUIDO/%{pnam}-%{version}.tar.gz
# Source0-md5:	091e05542e36f030c785f2919f05b73f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package is an internationalization library for Perl that aims to
be compatible with the Uniforum message translations system as
implemented for example in GNU gettext.

%description -l pl
Pakiet stanowi bibliotekê umiêdzynaradawiaj±c± Perla, która ma na celu
zachowanie zgodno¶ci ze standardem Uniforum t³umaczenia komunikatów
zaimplementowanym na przyk³ad w gettexcie GNU.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	OPTIMIZE="%{rpmcflags}"
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%dir %{perl_vendorarch}/auto/Locale/gettext_xs
%{perl_vendorarch}/auto/Locale/gettext_xs/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Locale/gettext_xs/*.so
%{perl_vendorlib}/Locale/*.pm
%{perl_vendorlib}/Locale/Recode
%{perl_vendorlib}/Locale/RecodeData
%{_mandir}/man3/*
