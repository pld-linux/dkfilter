# TODO:
# - init script, whole service stuff
#
%include	/usr/lib/rpm/macros.perl
Summary:	dkfilter - an SMTP-proxy designed for Postfix
Summary(pl):	dkfilter - proxy SMTP zaprojektowane dla Postfiksa
Name:		dkfilter
Version:	0.9
Release:	0.8
License:	GPL v2
Group:		Daemons
Source0:	http://jason.long.name/dkfilter/%{name}-%{version}.tar.gz
# Source0-md5:	3100af34fd00df4d80f07d3533cdf0eb
Patch0:		%{name}-perllib.patch
URL:		http://jason.long.name/dkfilter/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dkfilter is an SMTP-proxy designed for Postfix. It implements
DomainKeys message signing and verification. It comprises two separate
filters, an "outbound" filter for signing outgoing email, and an
"inbound" filter for verifying signatures of incoming email. The
filters can operate as either Before-Queue or After-Queue Postfix
content filters.

%description -l pl
dkfilter to proxy SMTP zaprojektowane dla Postfiksa. Implementuje
podpisywanie i weryfikacjê wiadomo¶ci DomainKeys. Zawiera dwa
oddzielne filtry, filtr "outbound" do podpisywania poczty
wychodz±cej oraz filtr "inbound" do weryfikacji podpisów poczty
przychodz±cej. Filtry mog± pracowaæ w filtrach zawarto¶ci Postfiksa
Before-Queue (przed kolejk±) lub After-Queue (za kolejk±).

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--libdir=%{perl_vendorlib}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog Mail-DomainKeys.README NEWS smtpprox* TODO
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/*.pm
%dir %{perl_vendorlib}/MSDW
%dir %{perl_vendorlib}/MSDW/SMTP
%{perl_vendorlib}/MSDW/SMTP/*.pm
%{perl_vendorlib}/Mail/*.pm
%dir %{perl_vendorlib}/Mail/DKIM
%{perl_vendorlib}/Mail/DKIM/*.pm
%dir %{perl_vendorlib}/Mail/DKIM/Algorithm
%{perl_vendorlib}/Mail/DKIM/Algorithm/*.pm
%dir %{perl_vendorlib}/Mail/DKIM/Canonicalization
%{perl_vendorlib}/Mail/DKIM/Canonicalization/*.pm
%dir %{perl_vendorlib}/Mail/DomainKeys
%{perl_vendorlib}/Mail/DomainKeys/*.pm
%dir %{perl_vendorlib}/Mail/DomainKeys/Key
%{perl_vendorlib}/Mail/DomainKeys/Key/*.pm
