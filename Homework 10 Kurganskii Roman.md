##1 Part
    gdisk /dev/sdb
    -o
    -n
    -w
    
    mkswap /dev/sdb2
    swapon /dev/sdb2
    
    [student1@localhost ~]$ sudo !!
    sudo gdisk /dev/sdb
    [sudo] password for student1:
    GPT fdisk (gdisk) version 0.8.10
    
    Partition table scan:
      MBR: protective
      BSD: not present
      APM: not present
      GPT: present
    
    Found valid GPT with protective MBR; using GPT.
    
    Command (? for help): i
    Partition number (1-2): 1
    Partition GUID code: 0FC63DAF-8483-4772-8E79-3D69D8477DE4 (Linux filesystem)
    Partition unique GUID: C2C5E30C-877D-4173-9F37-FE2E045C08D7
    First sector: 2048 (at 1024.0 KiB)
    Last sector: 4196351 (at 2.0 GiB)
    Partition size: 4194304 sectors (2.0 GiB)
    Attribute flags: 0000000000000000
    Partition name: 'Linux filesystem'
    
    Command (? for help): i
    Partition number (1-2): 2
    Partition GUID code: 0657FD6D-A4AB-43C4-84E5-0933C84B4F4F (Linux swap)
    Partition unique GUID: 962FDC51-6575-4AB5-B740-E822C30CEEC0
    First sector: 4196352 (at 2.0 GiB)
    Last sector: 5244927 (at 2.5 GiB)
    Partition size: 1048576 sectors (512.0 MiB)
    Attribute flags: 0000000000000000
    Partition name: 'Linux swap'

![изображение](https://user-images.githubusercontent.com/95036373/147752892-9b6ee5ba-659e-46c6-900a-777308d09be1.png)

      
    [student1@localhost ~]$ lsblk  
    NAME            MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT  
    sda               8:0    0    8G  0 disk  
    ├─sda1            8:1    0    1G  0 part /boot  
    └─sda2            8:2    0    7G  0 part  
      ├─centos-root 253:0    0  6.2G  0 lvm  /  
      └─centos-swap 253:1    0  820M  0 lvm  [SWAP]  
    sdb               8:16   0    5G  0 disk  
    ├─sdb1            8:17   0    2G  0 part /backup  
    └─sdb2            8:18   0  512M  0 part [SWAP]  
    sr0              11:0    1 1024M  0 rom  
      
    #add information about new partitions to fstab  
      
    [student1@localhost ~]$ cat /etc/fstab  
      
    /dev/mapper/centos-root /                       xfs     defaults        0 0  
    UUID=99863c5b-898f-4975-b6e4-b7c12e0e3ff6 /boot                   xfs     defaults        0 0  
    /dev/mapper/centos-swap swap                    swap    defaults        0 0  
    /dev/sdb1 /backup                               xfs     auto            0 0  
    /dev/sdb2 none                                  swap    sw              0 0  
      
      
    ##2 Part  
      
    add new partition  
      
    reboot	  
      
    pvcreate /dev/sdb3	  
      
    [student1@localhost ~]$ sudo !!  
      
    sudo vgdisplay  
      --- Volume group ---  
      VG Name               centos  
      System ID  
      Format                lvm2  
      Metadata Areas        1  
      Metadata Sequence No  3  
      VG Access             read/write  
      VG Status             resizable  
      MAX LV                0  
      Cur LV                2  
      Open LV               2  
      Max PV                0  
      Cur PV                1  
      Act PV                1  
      VG Size               <7.00 GiB  
      PE Size               4.00 MiB  
      Total PE              1791  
      Alloc PE / Size       1791 / <7.00 GiB  
      Free  PE / Size       0 / 0  
      VG UUID               MJE8N6-Pp82-DQdF-dzOH-nd49-bh5j-T55YRs  
      
    vgextend centos /dev/sdb3  
      
    [student1@localhost ~]$ sudo lvextend -L+1G /dev/centos/root  
      Size of logical volume centos/root changed from <6.20 GiB (1586 extents) to <7.20 GiB (1842 extents).  
      Logical volume centos/root successfully resized.  
        
    [student1@localhost ~]$ sudo lvextend -l +100%FREE /dev/centos/root  
      
    # Размер не изменился после ребута  
![изображение](https://user-images.githubusercontent.com/95036373/147752978-d056c39f-d779-4cf1-834a-676777393a57.png)
