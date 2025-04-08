
# 17 TP PKI

Choix: déploiement de VM Ubuntu 24.04

VM Image location:
C:\Users\%USERNAME%\OneDrive\Documents\Virtual Machines\Ubuntu 64-bit

## Check Wifi connection


```bash
sudo nano /etc/network/interfaces 

# then make sure this line is in that file :
iface eth0 inet dhcp


sudo apt update
sudo apt upgrade

ifconfig
sudo apt install net-tools

ping -c3 -I eth0 www.google.com

```


## Install VMWare Tools

Read:
- [https://knowledge.broadcom.com/external/article?legacyId=1014294](https://knowledge.broadcom.com/external/article?legacyId=1014294)
- [https://knowledge.broadcom.com/external/article?legacyId=2073803](https://knowledge.broadcom.com/external/article?legacyId=2073803)
- [https://github.com/vmware/open-vm-tools/blob/master/README.md](https://github.com/vmware/open-vm-tools/blob/master/README.md)
- []()

```bash
sudo apt install autoconf
autoreconf -i
./configure
make
sudo make install
sudo ldconfig

./configure --enable-servicediscovery
./configure --enable-salt-minion
./configure --enable-containerinfo=no
./configure --enable-containerinfo=yes
./configure --help

```

```console
xxx
```

```bash
man openssl-x509

uname -a
```

```console
xxx
```



```bash
xxx
```

```console
xxx
```


```bash
xxx
```

```console
xxx
```


```bash
xxx
```

```console
xxx
```


```bash
xxx
```

```console
xxx
```


```bash
xxx
```

```console
xxx
```


```bash
xxx
```

```console
xxx
```


