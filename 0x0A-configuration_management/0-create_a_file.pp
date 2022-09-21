# Create a file named school in /tmp directory
file { '/tmp/school':
    ensure  => 'present',
    mode    => '0744',
    group   => 'www-data',
    owner   => 'www-data',
    content => 'I love Puppet'
}

