# Web Server.

## Background Context

In this project, some of the tasks will be graded on 2 aspects:

* Is your `web-01` server configured according to requirements?
* Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)?
<br>
For example, if I need to create a file `/tmp/test` containing the string `hello world` and modify the configuration of Nginx to listen on port `8080` instead of `80`, I can use `emacs` on my server to create the file and to modify the Nginx configuration file `/etc/nginx/sites-enabled/default`.

But my answer file would contain:
```
sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu
```
As you can tell, I am not using `emacs` to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an `SRE`, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the `root` user, you do not need to use the `sudo` command.

A good Software Engineer is a `lazy Software Engineer`. 

Tips: to test your answer Bash script, feel free to reproduce the checker environment:

* start an `ubuntu:16.04` Docker container
* run your script on it
* see how it behaves
<br> 
Check out the Docker concept page for more info about how to manipulate containers.

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

* What is the main role of a web server<br>
* What is a child process<br>
* Why web servers usually have a parent process and child processes<br>
* What are the main HTTP requests

### DNS

* What DNS stands for<br>
* What is DNS main role
### DNS Record Types

A<br>
CNAME<br>
TXT<br>
MX

# Tasks
## Transfer a file to your server
Write a Bash script that transfers a file from our client to a server:

Requirements:

* Accepts 4 parameters
The path to the file to be transferred
The IP of the server we want to transfer the file to
The username `scp` connects with
The path to the SSH private key that `scp` uses
* Display `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
* `scp` must transfer the file to the user home directory `~/`
* Strict host key checking must be disabled when using `scp`

Example:

```
sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
sylvain@ubuntu$ 
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
sylvain@ubuntu$
```
In this example, I:

* remotely execute the `ls ~/` command via ssh to see what `~/` contains
* create a file named `some_page.html`
* execute my `0-transfer_file` script
* remotely execute the `ls ~/` command via `ssh` to see that the file `some_page.html` has been successfully transferred
That is one way of publishing your website pages to your server.

## Install nginx web server
Readme:

* -y on apt-get command
Web servers are the piece of software generating and serving HTML pages, let’s install one!

Requirements:

* Install nginx on your `web-01`
* server
* Nginx should be listening on port 80
* When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
* As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
* You can’t use `systemctl` for restarting `nginx`
Server terminal:

```
root@sy-web-01$ ./1-install_nginx_web_server > /dev/null 2>&1
root@sy-web-01$ 
root@sy-web-01$ curl localhost
Hello World!
root@sy-web-01$
```
Local terminal:

```
sylvain@ubuntu$ curl 34.198.248.145/
Hello World!
sylvain@ubuntu$ curl -sI 34.198.248.145/
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 23:43:22 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
Accept-Ranges: bytes

sylvain@ubuntu$
```

In this example `34.198.248.145` is the IP of my `web-01` server. If you want to query the Nginx that is locally installed on your server, you can use `curl 127.0.0.1.`

If things are not going as expected, make sure to check out Nginx logs, they can be found in `/var/log/`.

## Setup a domain name
.TECH Domains is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. We partnered with .TECH Domains so that you can learn about DNS.

.TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your tools space. Feel free to drop a thank you tweet for .TECH Domains.

Provide the domain name in your answer file.

Requirement:

* provide the domain name only (example: `foobar.tech`), no subdomain (example: `www.foobar.tech`)
* configure your DNS records with an A entry so that your root domain points to your `web-01` IP address.
**Warning: the propagation of your records can take time (~1-2 hours)**
* go to `your profile` and enter your domain in the `Project website url` field
Example:

```
sylvain@ubuntu$ cat 2-setup_a_domain_name
myschool.tech
sylvain@ubuntu$
sylvain@ubuntu$ dig myschool.tech

; <<>> DiG 9.10.6 <<>> myschool.tech
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 26785
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;myschool.tech.     IN  A

;; ANSWER SECTION:
myschool.tech.  7199    IN  A   184.72.193.201

;; Query time: 65 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Fri Aug 02 09:44:36 PDT 2019
;; MSG SIZE  rcvd: 65

sylvain@ubuntu$
```
When your domain name is setup, please verify the Registrar here: `https://whois.whoisxmlapi.com/` and you must see in the JSON response: `"registrarName": "Dotserve Inc"`

## Redirection





























