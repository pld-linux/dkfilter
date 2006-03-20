%define name dkfilter
%define ver  0.5
%define rel  1

Summary:   dkfilter is an SMTP-proxy designed for Postfix
Name:      %{name}
Version:   %{ver}
Release:   %{rel}.ckfr.rh3
Copyright: GPL
Vendor:    Jason Long <jlong@messiah.edu>
Url:       http://jason.long.name/dkfilter/
Packager:  Carlos Rivera <crivera@checkfree.com>
Group:     System Utils
Source:    %{name}.tgz
BuildRoot: /var/tmp/%{name}-%{ver}-build

%description
dkfilter is an SMTP-proxy designed for Postfix. It implements DomainKeys message signing and verification. It comprises two separate filters, an "outbound" filter for signing outgoing email, and an "inbound" filter for verifying signatures of incoming email. The filters can operate as either Before-Queue or After-Queue Postfix content filters.

%prep

%build

%install
mkdir -p ${RPM_BUILD_ROOT}/tmp
tar  -zxvf %{SOURCE0} -C ${RPM_BUILD_ROOT}/

%clean

%files
%defattr(755,root,root)
/etc/rc.d/init.d/dkfilter
/usr/local/dkfilter/dkfilter.in
/usr/local/dkfilter/dkfilter.out
/usr/local/dkfilter/DKMessage.pm
/usr/local/dkfilter/Mail/DomainKeys/Key/Public.pm
/usr/local/dkfilter/Mail/DomainKeys/Key/Private.pm
/usr/local/dkfilter/Mail/DomainKeys/Policy.pm
/usr/local/dkfilter/Mail/DomainKeys/Key.pm
/usr/local/dkfilter/Mail/DomainKeys/Signature.pm
/usr/local/dkfilter/Mail/DomainKeys/Header.pm
/usr/local/dkfilter/Mail/DomainKeys/Message.pm
/usr/local/dkfilter/Mail/DomainKeys.pm
/usr/local/dkfilter/MSDW/SMTP/Client.pm
/usr/local/dkfilter/MSDW/SMTP/Server.pm

%post
chkconfig dkfilter on

%pre

%postun

%changelog
* Mon May 02 2005 Carlos Rivera <crivera@checkfree.com>
 - created spec file and packaged program
 - modified init script
