# Puppet manifest to fix Apache 500 error
# Ensure that the missing file is present
file { '/path/to/missing/file':
  ensure => present,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0644',
}
