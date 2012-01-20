#!/usr/bin/perl -w
use strict;
use warnings;
use WWW::Mechanize;
use Net::INET6Glue::INET_is_INET6;                          #ipv6 支持

my $mech = WWW::Mechanize->new( autocheck => 1 );
my $lzt_file;

open(lzt_file,">cache/xdpd.html");

# first, we should login
$mech->get('https://github.com/login');

$mech->submit_form(
    fields   => {
        login => 'user@gmail.com', # your email, google account
        password => 'passwd', # your password, please not be 'yyy'
    }
);

$mech->get('https://github.com/organizations/xdlinux');
#$mech->follow_link( n => 1);                                 #如果ipv6 的话 这个就不需要了。

print lzt_file ($mech->content);

close(lzt_file);
