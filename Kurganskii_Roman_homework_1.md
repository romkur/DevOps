#first task


ls /usr/share/man/man*/*config*

ls /usr/share/man/man{1,7}/*system*


#second task

find /usr/share/man/ -name "*help*"

find /usr/share/man/ -name "conf*"

##В команде find через -exec позволяет удалить файл, менять действия или владельца, получить информацию


#third task

cd /etc

head -n 7 fstab
tail -n 2 fstab
head -n 100 fstab | wc -l
## При большем количестве строк чем в файле отобразит общее кол-во строк в файле

#fourth task
touch file_name{1..3}.md

##А дальше не понял


#fifth task
cd ~
cd ../home/student/
cd /home/student/
cd ./../home/student/
pushd ~


#sixth task
mkdir -p new /home/student/in-process/{tread0,tread1,tread2} processed
touch data{0..9}{0..9}
cp data{00..33} /home/student/in-process/tread0/
cp data{34..66} /home/student/in-process/tread1/
cp data{67..99} /home/student/in-process/tread2/

ls -l /home/student/in-process/tread*
ls /home/student/*process*/*

#!/bin/bash

VAR1=$(find /home/student/new/ -type f | wc -l)
VAR2=$(find /home/student/processed/ -type f | wc -l)

if [ "$VAR1" -eq "$VAR2" ];
then rm -f /home/student/new/*

fi



