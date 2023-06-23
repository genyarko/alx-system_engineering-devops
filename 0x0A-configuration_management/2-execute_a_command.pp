# This Puppet manifest kills a process named "killmenow"

exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => ['/usr/bin', '/bin'],  # Add additional paths as needed
  refreshonly => true,
}
