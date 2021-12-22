#1 Task

[student@localhost ~]$ sleep 30000 &
[1] 24175
[student@localhost ~]$ sleep 10000 &
[2] 24176
[student@localhost ~]$ sleep 15000 &
[3] 24177
[student@localhost ~]$ kill -19 %3
[student@localhost ~]$ fg %2
sleep 10000
^Z
[2]+  Stopped                 sleep 10000
[student@localhost ~]$ kill -s STOP %1
[student@localhost ~]$ jobs
[1]+  Stopped                 sleep 30000
[2]-  Stopped                 sleep 10000
[3]   Stopped                 sleep 15000

[student@localhost ~]$ kill -9 %1

[1]+  Stopped                 sleep 30000
[student@localhost ~]$ jobs
[1]+  Terminated              sleep 30000
[2]-  Stopped                 sleep 10000
[3]   Stopped                 sleep 15000

[student@localhost ~]$ bg %2
[student@localhost ~]$ kill -18 %3
[student@localhost ~]$ ps aux | grep sleep | grep -v 'grep'
student  24176  0.0  0.0 108056   360 pts/1    S    11:48   0:00 sleep 10000
student  24177  0.0  0.0 108056   360 pts/1    S    11:48   0:00 sleep 15000
[student@localhost ~]$ kill -9 24176 ## Можно через top
[student@localhost ~]$ kill -9 %3
[2]-  Killed                  sleep 10000


#2 Task
##Создаем юниты и таймер в директории /etc/systemd/system:

[Unit]
Description=Daemon1

[Service]
Type=simple
ExecStart=/usr/sbin/script1.sh
Restart=always

[Install]
WantedBy=multi-user.target
______________________________

[Unit]
Description=Daemon2
After=test1.service
Requires=test1.service

[Service]
Type=one-shot
ExecStart=/usr/sbin/script2.sh
Restart=no

[Install]
WantedBy=multi-user.target
______________________________
[Unit]
Description=Test Timer
Requires=test2.service

[Timer]
Unit=test2.service
OnCalendar=2019-01-01 00:00:00

[Install]
WantedBy=timers.target
______________________________
[student@localhost system]$ systemctl enable --now test.timer
[student@localhost system]$ systemctl enable --now test1.service
[student@localhost system]$ systemctl enable --now test2.service
##Сервисы стартовали и выполнились
[student@localhost system]$ systemctl stop test.timer
[student@localhost system]$ systemctl stop test1.service
[student@localhost system]$ systemctl stop test2.service

#3 Task

sudo vi /usr/sbin/anac.sh

##Добавить в анакронтаб: 
sudo vi /usr/sbin/anac.sh
chmod +x /usr/sbin/anac.sh
2       0       anac.sh                 /usr/sbin/anac.sh
__________________________________________________________
##для выполнения скрипта важно для какого юзера сделан крон и куда будет писать скрипт
sudo vi /usr/sbin/cron.sh
chmod +x /usr/sbin/cron.sh
su
crontab -e
@reboot sleep 60 && /usr/sbin/cron.sh

##4 Task
 ps aux | grep sleep
student   1584  0.0  0.0 108056   360 pts/0    S    10:52   0:00 sleep 10000
student   1611  0.0  0.0 112812   980 pts/0    R+   10:57   0:00 grep --color=auto sleep
[student@localhost opt]$ lsof -p 1584
COMMAND  PID    USER   FD   TYPE DEVICE  SIZE/OFF     NODE NAME
sleep   1584 student  cwd    DIR  253,0        19  4194844 /opt
sleep   1584 student  rtd    DIR  253,0       237       64 /
sleep   1584 student  txt    REG  253,0     33128 12746479 /usr/bin/sleep
sleep   1584 student  mem    REG  253,0 106176928 12588008 /usr/lib/locale/locale-archive
sleep   1584 student  mem    REG  253,0   2156592    36486 /usr/lib64/libc-2.17.so
sleep   1584 student  mem    REG  253,0    163312    21272 /usr/lib64/ld-2.17.so
sleep   1584 student    0u   CHR  136,0       0t0        3 /dev/pts/0
sleep   1584 student    1w   REG  253,0         0 13018418 /home/student/lsof1
sleep   1584 student    2w   REG  253,0         0 13018419 /home/student/lsof2
#также lsof -c sleep
#по FD видно что /dev/pts/0 открыт для чтения и записи

sudo lsof -i tcp
