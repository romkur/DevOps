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
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"><html><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
                <title>Apache HTTP Server Test Page powered by CentOS</title>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

    <!-- Bootstrap -->
    <link href="/noindex/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="noindex/css/open-sans.css" type="text/css" />

<style type="text/css"><!--

body {
  font-family: "Open Sans", Helvetica, sans-serif;
  font-weight: 100;
  color: #ccc;
  background: rgba(10, 24, 55, 1);
  font-size: 16px;
}

h2, h3, h4 {
  font-weight: 200;
}

h2 {
  font-size: 28px;
}

.jumbotron {
  margin-bottom: 0;
  color: #333;
  background: rgb(212,212,221); /* Old browsers */
  background: radial-gradient(ellipse at center top, rgba(255,255,255,1) 0%,rgba(174,174,183,1) 100%); /* W3C */
}

.jumbotron h1 {
  font-size: 128px;
  font-weight: 700;
  color: white;
  text-shadow: 0px 2px 0px #abc,
               0px 4px 10px rgba(0,0,0,0.15),
               0px 5px 2px rgba(0,0,0,0.1),
               0px 6px 30px rgba(0,0,0,0.1);
}

.jumbotron p {
  font-size: 28px;
  font-weight: 100;
}

.main {
   background: white;
   color: #234;
   border-top: 1px solid rgba(0,0,0,0.12);
   padding-top: 30px;
   padding-bottom: 40px;
}

.footer {
   border-top: 1px solid rgba(255,255,255,0.2);
   padding-top: 30px;
}

    --></style>
</head>
<body>
  <div class="jumbotron text-center">
    <div class="container">
          <h1>Hello!</h1>
                <p class="lead">You are here because you're probably a DevOps courses member. In that case you should open <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"> THIS LINK </a></p>
                </div>
  </div>
</body></html>

#Task 1.7

sudo ssh -L 80:172.31.45.237:80 -N -f Roman_Kurganskii@18.221.144.175

#Task 1.8

curl localhost from **localhost** ##port has been forwarded in previous step

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"><html><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
                <title>Apache HTTP Server Test Page powered by CentOS</title>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

    <!-- Bootstrap -->
    <link href="/noindex/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="noindex/css/open-sans.css" type="text/css" />

<style type="text/css"><!--

body {
  font-family: "Open Sans", Helvetica, sans-serif;
  font-weight: 100;
  color: #ccc;
  background: rgba(10, 24, 55, 1);
  font-size: 16px;
}

h2, h3, h4 {
  font-weight: 200;
}

h2 {
  font-size: 28px;
}

.jumbotron {
  margin-bottom: 0;
  color: #333;
  background: rgb(212,212,221); /* Old browsers */
  background: radial-gradient(ellipse at center top, rgba(255,255,255,1) 0%,rgba(174,174,183,1) 100%); /* W3C */
}

.jumbotron h1 {
  font-size: 128px;
  font-weight: 700;
  color: white;
  text-shadow: 0px 2px 0px #abc,
               0px 4px 10px rgba(0,0,0,0.15),
               0px 5px 2px rgba(0,0,0,0.1),
               0px 6px 30px rgba(0,0,0,0.1);
}

.jumbotron p {
  font-size: 28px;
  font-weight: 100;
}

.main {
   background: white;
   color: #234;
   border-top: 1px solid rgba(0,0,0,0.12);
   padding-top: 30px;
   padding-bottom: 40px;
}

.footer {
   border-top: 1px solid rgba(255,255,255,0.2);
   padding-top: 30px;
}

    --></style>
</head>
<body>
  <div class="jumbotron text-center">
    <div class="container">
          <h1>Hello!</h1>
                <p class="lead">You are here because you're probably a DevOps courses member. In that case you should open <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"> THIS LINK </a></p>
                </div>
  </div>
</body></html>

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
