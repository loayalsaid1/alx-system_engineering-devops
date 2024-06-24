# Change user limit of file descriptors for holberton
exec {'change-os-configuration-for-holberton-user':
    command => '/bin/sed "s/nofile [0-9]*/nofile 100/g" -i /etc/security/limits.conf',
}
