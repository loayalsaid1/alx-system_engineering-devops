# Edit the limit of the files open by nginx

exec { 'fix--for-nginx':
        command => '/bin/sed -i "s/15/2000/" /etc/default/nginx;\
        /usr/sbin/service nginx restart',
}
