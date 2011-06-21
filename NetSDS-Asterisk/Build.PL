#!/usr/bin/env perl

=head1 NAME

Build.PL - Build script generator for NetSDS core libraries

=head1 SYNOPSIS

 perl Build.PL
 ./Build
 ./Build test
 ./Build install

=cut

use strict;
use warnings 'all';

use Module::Build;

my $build = Module::Build->new(
	module_name        => 'NetSDS::Asterisk',
	dist_name          => 'NetSDS-Asterisk',
	dist_abstract      => 'Asterisk bindings for the NetSDS platform',
	create_makefile_pl => 'traditional',
	dist_author        => 'Net.Style Development Team <info@netstyle.com.ua>',
	create_readme      => 1,
	license            => 'gpl',
	build_requires     => {
		'Test::More'          => '0',
		'Test::Pod'           => '0',
		'Test::Pod::Coverage' => '0',
		'Module::Build'       => '0',
	},
	requires => {
		'perl'           => '5.008',
		'version'        => '0.700',
		'NetSDS'         => '1.400',
		'Data::Dumper'   => '2.000',
		'NetSDS::Logger' => '1.400',
	},
	recommends   => {},
	script_files => {},
);

$build->create_build_script;

__END__

=head1 AUTHOR

Michael Bochkaryov <misha@rattler.kiev.ua>

=cut
