# Fix a typo in wp-settings.php file
exec {'fix-wordpress':
    command => '/bin/sed -i "s/phpp/php/" /var/www/html/wp-settings.php'
}
