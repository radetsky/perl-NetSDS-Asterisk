%define module NetSDS-Asterisk
%define m_distro NetSDS-Asterisk
%define m_name NetSDS::Asterisk
%define m_author_id unknown
%define _enable_test 0
%define debug_package %{nil}

%define pkgname NetSDS-Asterisk

Name: perl-NetSDS-Asterisk
Version: 0.1
Release: 2_centos7

Summary: A general-purpose NetSDS-Asterisk class

License: Artistic
Group: Development/Perl
Url: http://www.pearlpbx.com

Packager: Alex Radetsky <rad@pearlpbx.com>

BuildArch: noarch
Source: %m_distro-%version.tar

Requires: perl-NetSDS 
#Requires: perl-Test-Pod-Coverage 
#Requires: perl-Test-Pod

BuildRequires: perl-devel 
BuildRequires: perl-Module-Build 
#BuildRequires: perl-Test-Pod-Coverage 
#BuildRequires: perl-Test-Pod 
#BuildRequires: perl-NetSDS

%description
This module is meant to be the definitive implementation of NetSDS-Asterisk,

%prep
%setup -q -n %{pkgname}-%{version}
chmod -R u+w %{_builddir}/%{pkgname}-%{version}

%build
grep -rsl '^#!.*perl' . |
grep -v '.bak$' |xargs --no-run-if-empty \
%__perl -MExtUtils::MakeMaker -e 'MY->fixin(@ARGV)'
%{__perl} Build.PL
%{__perl} Build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%{__perl} Build install destdir=%{buildroot}

cmd=/usr/share/spec-helper/compress_files
[ -x $cmd ] || cmd=/usr/lib/rpm/brp-compress
[ -x $cmd ] && $cmd

# SuSE Linux
if [ -e /etc/SuSE-release -o -e /etc/UnitedLinux-release ]
then
    %{__mkdir_p} %{buildroot}/var/adm/perl-modules
    %{__cat} `find %{buildroot} -name "perllocal.pod"`  \
        | %{__sed} -e s+%{buildroot}++g                 \
        > %{buildroot}/var/adm/perl-modules/%{name}
fi

# remove special files
find %{buildroot} -name "perllocal.pod" \
    -o -name ".packlist"                \
    -o -name "*.bs"                     \
    |xargs -i rm -f {}

#
find %{buildroot}%{_prefix}             \
    -type d -depth                      \
    -exec rmdir {} \; 2>/dev/null

%{__perl} -MFile::Find -le '
    find({ wanted => \&wanted, no_chdir => 1}, "%{buildroot}");
    for my $x (sort @dirs, @files) {
        push @ret, $x unless indirs($x);
        }
    print join "\n", sort @ret;

    sub wanted {
        return if /auto$/;

        local $_ = $File::Find::name;
        my $f = $_; s|^\Q%{buildroot}\E||;
        return unless length;
        return $files[@files] = $_ if -f $f;

        $d = $_;
        /\Q$d\E/ && return for reverse sort @INC;
        $d =~ /\Q$_\E/ && return
            for qw|/etc %_prefix/man %_prefix/bin %_prefix/share|;

        $dirs[@dirs] = $_;
        }
    sub indirs {
        my $x = shift;
        $x =~ /^\Q$_\E\// && $x ne $_ && return 1 for @dirs;
        }
    ' > %filelist

[ -z %filelist ] && {
    echo "ERROR: empty %files listing"
    exit -1
    }

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %filelist
%defattr(-,root,root)

%changelog
* Sat Feb 04 2017 Alex Radetsky <rad@pearlpbx.com> 0.1-centos7
- Fixed many bugs. 

* Tue Dec 20 2011 Dmitriy Kruglikov <dkr@netstyle.com.ua> 0.01-alt3
- Fixed spec. Removed unwonted requirements.

* Tue Dec 20 2011 Dmitriy Kruglikov <dkr@netstyle.com.ua> 0.01-alt2
- Rebuild for Test-P6

* Tue Jun 21 2011 Dmitriy Kruglikov <dkr@netstyle.com.ua> 0.01-alt1
- initial build for ALT Linux Sisyphus

