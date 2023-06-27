class nginx {
  package { 'nginx':
    ensure => installed,
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => '# Redirect /redirect_me to a different page
                server {
                  listen 80 default_server;
                  listen [::]:80 default_server;

                  root /var/www/html;
                  index index.html;

                  server_name _;

                  location = /redirect_me {
                    return 301 https://example.com/newpage;
                  }

                  location / {
                    try_files $uri $uri/ =404;
                  }
                }',
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure  => 'link',
    target  => '/etc/nginx/sites-available/default',
    require => File['/etc/nginx/sites-available/default'],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    require   => Package['nginx'],
    subscribe => [File['/etc/nginx/sites-available/default'], File['/etc/nginx/sites-enabled/default']],
  }
}

class { 'nginx': }
