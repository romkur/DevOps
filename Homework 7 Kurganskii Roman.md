#Task 1

##rpm
yum install sysstat --downloadonly
rpm -qip /var/cache/yum/x86_64/7/base/packages/sysstat-10.1.5-19.el7.x86_64.rpm
![image](https://user-images.githubusercontent.com/95036373/147385244-d0b9fdcb-fabd-41c5-955e-ab6d84faed34.png)
rpm -ql sysstat

##Nginx
[student@localhost ~]$ sudo touch /etc/yum.repos.d/nginx.repo
[sudo] password for student:
[student@localhost ~]$ sudo vi /etc/yum.repos.d/nginx.repo
[student@localhost ~]$ yum repoinfo nginx
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirror.logol.ru
 * extras: mirror.logol.ru
 * updates: centos-mirror.rbc.ru
base                                                     | 3.6 kB     00:00
extras                                                   | 2.9 kB     00:00
nginx                                                    | 2.9 kB     00:00
updates                                                  | 2.9 kB     00:00
nginx/7/x86_64/primary_db                                  |  70 kB   00:00
Repo-id      : nginx/7/x86_64
Repo-name    : nginx repo
Repo-status  : enabled
Repo-revision: 1637076068
Repo-updated : Tue Nov 16 10:21:09 2021
Repo-pkgs    : 256
Repo-size    : 131 M
Repo-baseurl : https://nginx.org/packages/centos/7/x86_64/
Repo-expire  : 21,600 second(s) (last: Sat Dec 25 01:58:07 2021)
  Filter     : read-only:present
Repo-filename: /etc/yum.repos.d/nginx.repo

repolist: 256


[student@localhost ~]$ sudo yum install nginx
[student@localhost ~]$ sudo yum history
[student@localhost ~]$ sudo yum history
Loaded plugins: fastestmirror
ID     | Login user               | Date and time    | Action(s)      | Altered
-------------------------------------------------------------------------------
    10 | student <student>        | 2021-12-25 02:01 | Install        |    1 E<
     9 | student <student>        | 2021-12-24 02:51 | Install        |   29 >
     8 | student <student>        | 2021-12-24 02:27 | Install        |    1
     7 | student <student>        | 2021-12-21 11:10 | Install        |    5
     6 | root <root>              | 2021-12-14 02:00 | I, U           |  106
     5 | student <student>        | 2021-12-09 03:35 | Install        |    1
     4 | student <student>        | 2021-12-08 00:20 | Install        |    1
     3 | student <student>        | 2021-12-07 17:44 | Install        |    1
     2 | student <student>        | 2021-12-07 17:43 | Install        |    2
     1 | System <unset>           | 2021-11-25 12:13 | Install        |  304
history list
[student@localhost ~]$ sudo yum history list all
Loaded plugins: fastestmirror
ID     | Login user               | Date and time    | Action(s)      | Altered
-------------------------------------------------------------------------------
    10 | student <student>        | 2021-12-25 02:01 | Install        |    1 E<
     9 | student <student>        | 2021-12-24 02:51 | Install        |   29 >
     8 | student <student>        | 2021-12-24 02:27 | Install        |    1
     7 | student <student>        | 2021-12-21 11:10 | Install        |    5
     6 | root <root>              | 2021-12-14 02:00 | I, U           |  106
     5 | student <student>        | 2021-12-09 03:35 | Install        |    1
     4 | student <student>        | 2021-12-08 00:20 | Install        |    1
     3 | student <student>        | 2021-12-07 17:44 | Install        |    1
     2 | student <student>        | 2021-12-07 17:43 | Install        |    2
     1 | System <unset>           | 2021-11-25 12:13 | Install        |  304
history list
[student@localhost ~]$ sudo yum history undo 10
Loaded plugins: fastestmirror
Undoing transaction 10, from Sat Dec 25 02:01:50 2021
    Install nginx-1:1.20.2-1.el7.ngx.x86_64 @nginx
Resolving Dependencies
--> Running transaction check
---> Package nginx.x86_64 1:1.20.2-1.el7.ngx will be erased
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================================
 Package           Arch               Version                          Repository          Size
================================================================================================
Removing:
 nginx             x86_64             1:1.20.2-1.el7.ngx               @nginx             2.8 M

Transaction Summary
================================================================================================
Remove  1 Package

Installed size: 2.8 M
Is this ok [y/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Erasing    : 1:nginx-1.20.2-1.el7.ngx.x86_64                                              1/1
  Verifying  : 1:nginx-1.20.2-1.el7.ngx.x86_64                                              1/1

Removed:
  nginx.x86_64 1:1.20.2-1.el7.ngx

Complete!

[student@localhost ~]$ sudo !!
sudo vi /etc/yum.repos.d/nginx.repo
[student@localhost ~]$ yum repoinfo nginx
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirror.logol.ru
 * extras: mirror.logol.ru
 * updates: centos-mirror.rbc.ru
Repo-id      : nginx/7/x86_64
Repo-name    : nginx repo
Repo-status  : disabled
Repo-baseurl : https://nginx.org/packages/centos/7/x86_64/
Repo-expire  : 21,600 second(s) (last: Sat Dec 25 02:01:35 2021)
  Filter     : read-only:present
Repo-filename: /etc/yum.repos.d/nginx.repo

repolist: 0

[student@localhost ~]$ sudo yum erase sysstat
Loaded plugins: fastestmirror
Resolving Dependencies
--> Running transaction check
---> Package sysstat.x86_64 0:10.1.5-19.el7 will be erased
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================================
 Package             Arch               Version                     Repository             Size
================================================================================================
Removing:
 sysstat             x86_64             10.1.5-19.el7               installed             1.1 M

Transaction Summary
================================================================================================
Remove  1 Package

Installed size: 1.1 M
Is this ok [y/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Erasing    : sysstat-10.1.5-19.el7.x86_64                                                 1/1
  Verifying  : sysstat-10.1.5-19.el7.x86_64                                                 1/1

Removed:
  sysstat.x86_64 0:10.1.5-19.el7

Complete!


[student@localhost etc]$ yum -y install epel-release
[student@localhost ~]$ yum repoinfo epel
[student@localhost ~]$ sudo yum repo-pkgs epel list
[student@localhost ~]$ sudo yum install ncdu


#Task 2

[student@localhost ~]$ find . -type f -size -100c


[root@localhost /]# stat . | grep Inode
Device: fd00h/64768d    Inode: 64          Links: 18
##Didn't find information why root has 18 links

[root@localhost /]# ls -lai
total 16
      64 drwxr-xr-x.  18 root root  237 Dec 13 23:47 .
      64 drwxr-xr-x.  18 root root  237 Dec 13 23:47 ..
     120 lrwxrwxrwx.   1 root root    7 Nov 25 12:13 bin -> usr/bin
      64 dr-xr-xr-x.   5 root root 4096 Dec 17 10:40 boot
      
##Inode = 64 
## to information in provided link by comparing file names and inode numbers, the system can make up a tree-structure that the user understands


du is used to estimate file space usage—space used under a particular directory or files on a file system.
 
df is used to display the amount of available disk space for file systems on which the invoking user has appropriate read access.


![image](https://user-images.githubusercontent.com/95036373/147385272-c414cf1a-d661-44fc-9493-c202e407f0fd.png)

