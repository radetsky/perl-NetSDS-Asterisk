%define module NetSDS-Asterisk
%define m_distro NetSDS-Asterisk
%define m_name NetSDS::Asterisk
%define m_author_id unknown
%define _enable_test 1

Name: perl-NetSDS-Asterisk
Version: 0.01
Release: alt2

Summary: A general-purpose NetSDS-Asterisk class

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Dmitriy Kruglikov <dkr@netstyle.com.ua>

BuildArch: noarch
Source: %m_distro-%version.tar

Requires: perl-NetSDS 
Requires: perl-Test-Pod-Coverage 
Requires: perl-Test-Pod

BuildRequires: perl-devel 
BuildRequires: perl-Module-Build 
BuildRequires: perl-Test-Pod-Coverage 
BuildRequires: perl-Test-Pod 
BuildRequires: perl-NetSDS

%description
This module is meant to be the definitive implementation of NetSDS-Asterisk,

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/NetSDS/*

%changelog
* Tue Dec 20 2011 Dmitriy Kruglikov <dkr@netstyle.com.ua> 0.01-alt2
- Rebuild for Test-P6

* Tue Jun 21 2011 Dmitriy Kruglikov <dkr@netstyle.com.ua> 0.01-alt1
- initial build for ALT Linux Sisyphus

