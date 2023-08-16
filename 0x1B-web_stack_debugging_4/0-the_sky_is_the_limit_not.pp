file { '/etc/default/nginx':
  ensure => present,
  replace => true,
  content => "ULIMIT=\"-n 4096\"\n",
  notify => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
  require => File['/etc/default/nginx'],
}
