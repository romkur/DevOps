#Task 1

    student@localhost ~]$ sudo ip addr add 192.168.2.3/24 dev enp0s8
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
    2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        inet 10.0.2.15/24 brd 10.0.2.255 scope global noprefixroute dynamic enp0s3
           valid_lft 86175sec preferred_lft 86175sec
    3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        inet 10.0.3.15/24 brd 10.0.3.255 scope global noprefixroute dynamic enp0s8
           valid_lft 86175sec preferred_lft 86175sec
        inet 192.168.2.3/24 scope global enp0s8
           valid_lft forever preferred_lft forever
           
    [student@localhost ~]$ sudo ip addr del 192.168.2.3/24 dev enp0s8
    
    [student@localhost ~]$ ip -4 a
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
    2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        inet 10.0.2.15/24 brd 10.0.2.255 scope global noprefixroute dynamic enp0s3
           valid_lft 86049sec preferred_lft 86049sec
    3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        inet 10.0.3.15/24 brd 10.0.3.255 scope global noprefixroute dynamic enp0s8
           valid_lft 86049sec preferred_lft 86049sec
    [student@localhost network-scripts]$ sudo vi ifcfg-enp0s8


## добавляем в конфиг

    TYPE="Ethernet"
    PROXY_METHOD="none"
    ONBOOT=yes
    BOOTPROTO="none"
    DEFROUTE="yes"
    IPV4_FAILURE_FATAL="no"
    NAME="enp0s8"
    DEVICE="enp0s8"
    PREFIX=24
    IPADDR=192.168.2.3
     
    [student@localhost network-scripts]$ systemctl restart network
    ==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ===
    Authentication is required to manage system services or units.
    Authenticating as: student
    Password:
    ==== AUTHENTICATION COMPLETE ===
    
    [student@localhost network-scripts]$ ip -4 a
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
    2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        inet 10.0.2.15/24 brd 10.0.2.255 scope global noprefixroute dynamic enp0s3
           valid_lft 86397sec preferred_lft 86397sec
    3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        inet 192.168.2.3/24 brd 192.168.2.255 scope global noprefixroute enp0s8
           valid_lft forever preferred_lft forever
    
    
    [student@localhost ~]$ sudo !!
    sudo nmcli dev modify enp0s8 ipv4.addresses 192.168.2.3/24
    
    [student@localhost ~]$ ip -4 a
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
    2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        inet 10.0.2.15/24 brd 10.0.2.255 scope global noprefixroute dynamic enp0s3
           valid_lft 86194sec preferred_lft 86194sec
    3: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        inet 10.0.3.15/24 brd 10.0.3.255 scope global noprefixroute dynamic enp0s8
           valid_lft 84766sec preferred_lft 84766sec
        inet 192.168.2.3/24 brd 192.168.1.255 scope global noprefixroute enp0s8
           valid_lft forever preferred_lft forever
           
    #Task 2
    
    Меняем конфиг для sshd и устанавливаем адрес 192.168.2.3, на виртуальной машине проброс порта с localhost на 192.168.2.3
    
    [student@localhost ~]$ sudo tcpdump -i enp0s8 -w /tmp/packets
    [student@localhost ~]$ tcpdump -r /tmp/packets | less
    
![image](https://user-images.githubusercontent.com/95036373/147507829-ef3e57e5-1e4e-4ce0-ac82-f35efef94253.png)
## Флаг S

#Task 3

![image](https://user-images.githubusercontent.com/95036373/147507665-ef924800-95dc-4961-8ab1-7316208d61d4.png)

## Почему то только флаг R, а не F

#Task 4

[student@localhost ~]$ sudo tcpdump -i any -A port 80 -w /tmp/packets &
[student@localhost ~]$ curl http://info.cern.ch
