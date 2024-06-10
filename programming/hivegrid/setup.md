## Framework Laptop

- 64 GB memory
- 1 TB hard disk
- HDMI port is capable of driving a Dell Ultrasharp 49 Curved Monitor.

### Issues

- VS code GUI looks big. Crashes if a big project is opened. 
- Sublime Text freezes the machine and had to be rebooted. 

### OS

```
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.4 LTS
Release:	22.04
Codename:	jammy
```

Only wget is installed by default.

## Install Curl

```
sudo apt update
sudo apt upgrade
sudo apt install curl
```

## Install Git 

Look at the latest version of Git on its home page. Replace the version in the curl command:

```
sudo apt update
sudo apt install libz-dev libssl-dev libcurl4-gnutls-dev libexpat1-dev gettext cmake gcc
curl -o git.tar.gz https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.44.0.tar.gz
```

Note, selecting 'zlib1g-dev' instead of 'libz-dev'

The following NEW packages will be installed:
  binutils binutils-common binutils-x86-64-linux-gnu cmake cmake-data dh-elpa-helper gcc gcc-11 gettext libasan6
  libbinutils libc-dev-bin libc-devtools libc6-dev libcc1-0 libcrypt-dev libctf-nobfd0 libctf0
  libcurl4-gnutls-dev libexpat1-dev libgcc-11-dev libitm1 libjsoncpp25 liblsan0 libnsl-dev libquadmath0 librhash0
  libssl-dev libtirpc-dev libtsan0 libubsan1 linux-libc-dev make manpages-dev rpcsvc-proto zlib1g-dev

```
tar -zxf git.tar.gz
make prefix=/usr/local all
sudo make prefix=/usr/local install
exec bash
git --version
```

```
git config --global user.name "Your Name"
git config --global user.email "youremail@domain.com"
```

BIOS update for Ubuntu is not installed yet. It is confusing whether it is available or not from framework website.
