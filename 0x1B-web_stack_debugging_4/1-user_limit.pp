# 1-user_limit.pp

# Change open file limits for the holberton user
exec { 'set_holberton_ulimit':
  command => 'sudo su -c "ulimit -n 4096" holberton',
  path    => '/usr/bin:/usr/sbin:/bin',
}

# Allow holberton user to login and access files without errors
file { '/etc/security/limits.d/holberton.conf':
  ensure  => 'present',
  content => "holberton hard nofile 4096\nholberton soft nofile 4096\n",
}

# Ensure the holberton user can login without shell restrictions
user { 'holberton':
  shell   => '/bin/bash',
  require => File['/etc/security/limits.d/holberton.conf'],
}
