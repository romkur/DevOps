#1

sudo groupadd -g 4000 sales
sudo useradd -g sales  alice 
sudo useradd -g sales  bob 
sudo useradd -g sales  eve 
sudo passwd alice 
sudo passwd bob 
sudo passwd eve 

chage -M 15 bob



## с политикой экспайра аккаунта для новых пользователей, возможно так chage -E $(date +%F -d "+30 days") alice
##В файле /etc/login.defs поменяем
PASS_MAX_DAYS   30 


##дополнительно
sudo passwd -e  alice 
sudo passwd -e  bob 
sudo passwd -e  eve 

#2

mkdir /home/students/
chmod 770 /home/students/
groupadd students
chown :students /home/students/
useradd lesly -g students
useradd glen -g students
useradd anthony -g students

#3

mkdir -p /share/cases

 touch /share/cases/murders.txt 
 touch /share/cases/moriarty
 groupadd bakerstreet
 groupadd scotlandyard
 useradd watson -g bakerstreet
 useradd holmes -g bakerstreet
 useradd lestrade -g scotlandyard
 useradd gregson -g scotlandyard
 useradd jones -g scotlandyard
  ## можно сразу создать всех через newusers с паролем и группой
 
  sudo chmod 770 /share/cases/
  
   setfacl -m g:scotlandyard:rwx /share/cases
   setfacl -m u:jones:r-x /share/cases
   setfacl -m g:scotlandyard:rwx /share/cases

 
###В итоге 
 [root@localhost cases]# getfacl -e .
# file: .
# owner: root
# group: bakerstreet
user::rwx
user:jones:r-x                  #effective:r-x
group::rwx                      #effective:rwx
group:scotlandyard:rwx          #effective:rwx
mask::rwx
other::---
