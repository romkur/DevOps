#Task 1.1
![image](https://user-images.githubusercontent.com/95036373/147124920-611c23c4-b448-4ba9-8f15-1eea7a0b3f3d.png)
#Task1.2
[student@localhost .ssh]$ mkdir folder
[student@localhost .ssh]$ ssh-keygen -f ~/.ssh/folder/hw-5.key
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/student/.ssh/folder/hw-5.key.
Your public key has been saved in /home/student/.ssh/folder/hw-5.key.pub.
The key fingerprint is:
SHA256:XiRcIfR1NnQu0DM0CkWCCLk4mn3N7DNFrH5nyuOVCUk student@localhost.localdomain
The key's randomart image is:
+---[RSA 2048]----+
| .o oo.=+=+B .|
| . ...+ + =+= |
| . . .E o . .o.|
| o . .o+ . |
| + . + oS . |
|o . . =..o o |
| . o .. + |
| =.o.o |
| =+= |
+----[SHA256]-----+
#Task 1.3
ssh-copy-id -i ~/.ssh/folder/hw-5.key.pub Roman_Kurganskii@18.221.144.175
#Task 1.4 

ssh -i ~/.ssh/folder/hw-5.key.pub Roman_Kurganskii@18.221.144.175

#Task 1.5
[student@localhost .ssh]$ cat config
Host    remotehost
        HostName 18.221.144.175
        Port 22
        User Roman_Kurganskii
        IdentityFile ~/.ssh/folder/hw-5.key
#Task 1.6
ssh to **remotehost**
curl **webserver** from **remotehost**

#Task 1.7

sudo ssh -L 80:172.31.45.237:80 -N -f Roman_Kurganskii@18.221.144.175

#Task 1.8

curl localhost from **localhost** ##port has been forwarded in previous step

#Task 2.1

timedatectl set-timezone America/Havana ## set timezone
timedatectl ##check current time

#Task 2.2

journalctl _UID=81 —since "50 min ago"

#Task 2.3

sudo vi /etc/rsyslog.d/auth-errors.conf 

##Write in file 

security.alert /var/log/auth-errors
security.emerg /var/log/auth-errors
auth.alert /var/log/auth-errors
auth.emerg /var/log/auth-errors
_______________________________________

systemctl restart rsyslog

logger -p 'auth.emerg' 'test message
