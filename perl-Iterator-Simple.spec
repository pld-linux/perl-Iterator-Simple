#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Iterator
%define		pnam	Simple
Summary:	Iterator::Simple Perl module
Summary(pl.UTF-8):	Moduł Perla Iterator::Simple
Name:		perl-Iterator-Simple
Version:	0.07
Release:	1
License:	Perl5
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Iterator/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	66b9356d1f68e6441c6f0e5aa7404946
URL:		https://metacpan.org/release/Iterator-Simple
BuildRequires:	perl-Module-Install
BuildRequires:	perl-devel >= 1:5.10.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iterator::Simple Perl module.

%description -l pl.UTF-8
Moduł Perla Iterator::Simple.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

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
%doc Changes README
%{_mandir}/man3/Iterator::Simple.3pm*
%dir %{perl_vendorlib}/Iterator
%{perl_vendorlib}/Iterator/Simple.pm
