# Postmortem

![Debugging](https://miro.medium.com/max/800/0*kHoWD7gJ0PC9GmBK.jpg)

## Issue Summary

The wordpress page was down after uploading to the web server from Thursday, February 17, 2022, 12:00 AM GMT+1 to Thursday, February 17, 2022, 12:30 AM GMT+1. After this problem, 30% of users were affected. The problem was caused by a misconfiguration in the wp-settings.php file.

## Timeline

* The DevOps Junior engineer upgraded the web server on February 17, 2022, at 12:00 AM GMT+1.
* 12:05 AM GMT+1 - The WordPress site was down, according to the DevOps Junior engineer.
* 12:07 AM GMT+1 - The web server fault was identified as "500 Internal Server Error" by the DevOps Junior engineer.
* 12:10 AM GMT+1 - The DevOps Junior engineer began troubleshooting the web server, assuming that the issue was caused by a missing file.
* 12:15 AM GMT+1 - After double-checking that all files were there in the `/var/www/html/` folder, the DevOps Junior Engineer concluded the issue was with the import and utilized the built-in debugging tool `strace.`
* 12:17 AM GMT+1 - With the ```ps aux``` command, the DevOps Junior engineer looked for the process ID of `www-data.`
* 12:19 AM GMT+1 - `curl 127.0.0.1` was used by the DevOps Junior engineer to test the `www-data` process.
* 12:25 AM GMT+1 - When importing the `/var/www/html/wp-includes/class-wp-locale.phpp` file into the `/var/www/html/wp-settings.php` file, the DevOps Junior engineer discovered an issue.
* 12:28 AM GMT+1 - The DevOps Junior engineer changed the import name `class-wp-locale.phpp` to `class-wp-locale.php` in the file `/var/www/html/wp-settings.php`.
* 12:30 AM GMT+1 - The problem was addressed once the DevOps Junior engineer retested the web server with `curl 127.0.0.1`.

## Root cause and resolution

When the DevOps Junior engineer tried to update the wordpress site, he accidentally inserted an additional "p" letter at the end of the "class-wp-locale.php" file, changing the name to "class-wp-locale.phpp." As a result, the system failed when the "class-wp-locale.phpp" file was imported into /var/www/html/wp-settings.php since the file did not exist.

To resolve the issue, the engineer used `strace` to examine the ongoing process (ps aux) and troubleshoot the www-data process (strace www-data). "/var/www/html/wp-includes/class-wp-locale.phpp ENOENT (No such file or directory)" is the message he read after examing it. The DevOps Junior engineer saw that the file's name was incorrect, so he opened the "/var/www/html/wp-settings.php" file, searched for "class-wp-locale.phpp," deleted the additional "p," and saved the modifications.

## Corrective and preventative measures

To avoid this mistake, update the permissions of the `/var/www/html/wp-settings.php` file to only allow the DevOps Senior engineer to work on it, and do not allow the Junior engineers to deploy the project.

Follow the methods below to deal with this type of problem:

* Make sure the server is up and running by sending a request to it. curl 127.0.0.1 is an example.
* Verify that all of the relevant processes (mysql, nginx, apache, PHP) are running. `ps aux`, for example.
* When a request comes in, debug the web server process. `strace PHP` is an example.
* Read each message on the screen.
* Solve the issue.
 
