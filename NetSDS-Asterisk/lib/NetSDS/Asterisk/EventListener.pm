package NetSDS::Asterisk::EventListener;

use strict;
use warnings;

use base 'NetSDS::Asterisk::Manager';

our $VERSION = '0.2';

sub new {

    my ( $class, %params ) = @_;

    my $this = $class->SUPER::new(%params);
    $this->{events}  = 'On';

    return bless $this;
}

sub _getEvent {
    my $this = shift;

    return $this->receive_answer();
  
}

1;

=pod

=head1 SUPPORT

No support is available

=head1 AUTHOR

Copyright 2009-2010 Alex Radetsky <rad@rad.kiev.ua> 

=cut

