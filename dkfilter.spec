# TODO:
# - init script, whole service stuff
# - files section....
#
%include	/usr/lib/rpm/macros.perl
Summary:	dkfilter is an SMTP-proxy designed for Postfix
Name:		dkfilter
Version:	0.9
Release:	0.3
License:	GPL v2
Group:		Daemons
Source0:	http://jason.long.name/dkfilter/%{name}-%{version}.tar.gz
# Source0-md5:	3100af34fd00df4d80f07d3533cdf0eb
Patch0:		%{name}-perllib.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
URL:		http://jason.long.name/dkfilter/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dkfilter is an SMTP-proxy designed for Postfix. It implements
DomainKeys message signing and verification. It comprises two separate
filters, an "outbound" filter for signing outgoing email, and an
"inbound" filter for verifying signatures of incoming email. The
filters can operate as either Before-Queue or After-Queue Postfix
content filters.

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
#/etc/rc.d/init.d/dkfilter
#%{_prefix}/local/dkfilter/dkfilter.in
#%{_prefix}/local/dkfilter/dkfilter.out
#%{_prefix}/local/dkfilter/DKMessage.pm
#%{_prefix}/local/dkfilter/Mail/DomainKeys/Key/Public.pm
#%{_prefix}/local/dkfilter/Mail/DomainKeys/Key/Private.pm
#%{_prefix}/local/dkfilter/Mail/DomainKeys/Policy.pm
#%{_prefix}/local/dkfilter/Mail/DomainKeys/Key.pm
#%{_prefix}/local/dkfilter/Mail/DomainKeys/Signature.pm
#%{_prefix}/local/dkfilter/Mail/DomainKeys/Header.pm
#%{_prefix}/local/dkfilter/Mail/DomainKeys/Message.pm
#%{_prefix}/local/dkfilter/Mail/DomainKeys.pm
#%{_prefix}/local/dkfilter/MSDW/SMTP/Client.pm
#%{_prefix}/local/dkfilter/MSDW/SMTP/Server.pm
