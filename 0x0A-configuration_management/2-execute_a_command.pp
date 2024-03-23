# execute a pkill command
exec {'killmenow':
    command => '/usr/bin/pkill killmenow'
}
