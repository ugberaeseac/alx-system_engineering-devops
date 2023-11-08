# Fix Apache returning 500 Server error
# use tmux to run strace in one window and curl in another one

exec {'debug-apache':
	command	=> 'sed -i "s/.phpp/php/g" /var/www/html/wp-settings.php',
	path 	=> '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
