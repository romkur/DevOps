## Boot process
1.
sudo vi /etc/default/grub
set GRUB_DISABLE_RECOVERY=false

sudo grub2-mkconfig -o /boot/grub2/grub.cfg	

sudo reboot


2.
echo 15 > /proc/sys/vm/dirty_ratio
sysctl -p

sudo vi /etc/systemctl.conf 
set vm.dirty_ratio = 15


## Selinux
grubby --update-kernel=ALL --args="selinux=0"

## Firewalls
1.
firewall-cmd --new-zone=ssh-access --permanent
firewall-cmd --zone=ssh-access --add-source=192.168.56.0/24 --permanent
firewall-cmd --zone=ssh-access --add-interface=enp0s3 --permanent
firewall-cmd --zone=ssh-access --add-port=22/tcp --permanent
firewall-cmd --reload

[root@localhost grub2]# firewall-cmd --zone=ssh-access --list-all               ssh-access (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s3
  sources: 192.168.56.0/24
  services:
  ports: 22/tcp
  protocols:
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:

systemctl stop firewalld

2.
sudo iptables -A INPUT -i enp0s3 -p tcp -s 192.168.56.0/24 --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
