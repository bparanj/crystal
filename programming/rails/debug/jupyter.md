

```
brew install jupyterlab
```

jupyter lab password: railsdox


ssh -i ~/Downloads/rails-docs.pem ubuntu@34.212.0.156

ssh -i ~/Downloads/rails-docs.pem ubuntu@34.212.0.156 -L 8000:localhost:8181 -N

The f flag runs it in backgraound:
ssh -f -i ~/Downloads/rails-docs.pem ubuntu@34.212.0.156 -L 8000:localhost:8181 -N


nohup jupyter-lab --no-browser --allow-root --port 8181 &

tails nohup.out


ps aux | grep ssh


sudo apt update

sudo apt install git curl libssl-dev libreadline-dev zlib1g-dev autoconf bison build-essential libyaml-dev libreadline-dev libncurses5-dev libffi-dev libgdbm-dev

curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash

echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc

echo 'eval "$(rbenv init -)"' >> ~/.bashrc

source ~/.bashrc

type rbenv

rbenv install -l

rbenv install 3.3.0

rbenv global 3.3.0

ruby -v

echo "gem: --no-document" > ~/.gemrc

gem install cztop rbczmq ffi-rzmq iruby



https://www.digitalocean.com/community/tutorials/how-to-install-ruby-on-rails-with-rbenv-on-ubuntu-22-04

https://medium.com/recursivelabs/ruby-kernel-for-jupyter-notebook-5ecdecd31af3

https://ankane.org/jupyter-rails

ubuntu@ip-172-31-32-88:~$ python3 --version
Python 3.10.12
ubuntu@ip-172-31-32-88:~$ ruby -v
Command 'ruby' not found, but can be installed with:
sudo snap install ruby  # version 3.3.0, or
sudo apt  install ruby  # version 1:3.0~exp1
See 'snap info ruby' for additional versions.
ubuntu@ip-172-31-32-88:~$ sudo apt update
Hit:1 http://us-west-2.ec2.archive.ubuntu.com/ubuntu jammy InRelease
Hit:2 http://us-west-2.ec2.archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:3 http://us-west-2.ec2.archive.ubuntu.com/ubuntu jammy-backports InRelease
Hit:4 http://security.ubuntu.com/ubuntu jammy-security InRelease
Reading package lists... Done                        
Building dependency tree... Done
Reading state information... Done
25 packages can be upgraded. Run 'apt list --upgradable' to see them.
ubuntu@ip-172-31-32-88:~$ sudo apt install git curl libssl-dev libreadline-dev zlib1g-dev autoconf bison build-essential libyaml-dev libreadline-dev libncurses5-dev libffi-dev libgdbm-dev
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
build-essential is already the newest version (12.9ubuntu3).
build-essential set to manually installed.
curl is already the newest version (7.81.0-1ubuntu1.15).
curl set to manually installed.
git is already the newest version (1:2.34.1-1ubuntu1.10).
git set to manually installed.
zlib1g-dev is already the newest version (1:1.2.11.dfsg-2ubuntu9.2).
zlib1g-dev set to manually installed.
Suggested packages:
  autoconf-archive gnu-standards autoconf-doc libtool gettext bison-doc ncurses-doc readline-doc libssl-doc libyaml-doc m4-doc
The following NEW packages will be installed:
  autoconf automake autotools-dev bison libffi-dev libgdbm-dev libncurses-dev libncurses5-dev libreadline-dev libssl-dev libyaml-dev m4
0 upgraded, 12 newly installed, 0 to remove and 25 not upgraded.
Need to get 5051 kB of archives.
After this operation, 23.2 MB of additional disk space will be used.
Get:1 http://us-west-2.ec2.archive.ubuntu.com/ubuntu jammy/main amd64 m4 amd64 1.4.18-5ubuntu2 [199 kB]
Get:2 http://us-west-2.ec2.archive.ubuntu.com/ubuntu jammy/main amd64 autoconf all 2.71-2 [338 kB]
Get:3 http://us-west-2.ec2.archive.ubuntu.com/ubuntu jammy/main amd64 autotools-dev all 20220109.1 [44.9 kB]
Get:4 http://us-west-2.ec2.archive.ubuntu.com/ubuntu jammy/main amd64 automake all 1:1.16.5-1.3 [558 kB]
Get:5 http://us-west-2.ec2.archive.ubuntu.com/ubuntu jammy/main amd64 bison amd64 2:3.8.2+dfsg-1build1 [748 kB]
Get:6 http://us-west-2.ec2.archive.ubuntu.com/ubuntu jammy/main amd64 libgdbm-dev amd64 1.23-1 [117 kB]
Get:7 http://us-west-2.ec2.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libncurses-dev amd64 6.3-2ubuntu0.1 [381 kB]
Get:8 http://us-west-2.ec2.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libncurses5-dev amd64 6.3-2ubuntu0.1 [790 B]
Get:9 http://us-west-2.ec2.archive.ubuntu.com/ubuntu jammy/main amd64 libreadline-dev amd64 8.1.2-1 [166 kB]
Get:10 http://us-west-2.ec2.archive.ubuntu.com/ubuntu jammy-updates/main amd64 libssl-dev amd64 3.0.2-0ubuntu1.12 [2373 kB]
Get:11 http://us-west-2.ec2.archive.ubuntu.com/ubuntu jammy/main amd64 libffi-dev amd64 3.4.2-4 [63.7 kB]
Get:12 http://us-west-2.ec2.archive.ubuntu.com/ubuntu jammy/main amd64 libyaml-dev amd64 0.2.2-1build2 [62.8 kB]
Fetched 5051 kB in 0s (16.7 MB/s)       
Selecting previously unselected package m4.
(Reading database ... 71601 files and directories currently installed.)
Preparing to unpack .../00-m4_1.4.18-5ubuntu2_amd64.deb ...
Unpacking m4 (1.4.18-5ubuntu2) ...
Selecting previously unselected package autoconf.
Preparing to unpack .../01-autoconf_2.71-2_all.deb ...
Unpacking autoconf (2.71-2) ...
Selecting previously unselected package autotools-dev.
Preparing to unpack .../02-autotools-dev_20220109.1_all.deb ...
Unpacking autotools-dev (20220109.1) ...
Selecting previously unselected package automake.
Preparing to unpack .../03-automake_1%3a1.16.5-1.3_all.deb ...
Unpacking automake (1:1.16.5-1.3) ...
Selecting previously unselected package bison.
Preparing to unpack .../04-bison_2%3a3.8.2+dfsg-1build1_amd64.deb ...
Unpacking bison (2:3.8.2+dfsg-1build1) ...
Selecting previously unselected package libgdbm-dev:amd64.
Preparing to unpack .../05-libgdbm-dev_1.23-1_amd64.deb ...
Unpacking libgdbm-dev:amd64 (1.23-1) ...
Selecting previously unselected package libncurses-dev:amd64.
Preparing to unpack .../06-libncurses-dev_6.3-2ubuntu0.1_amd64.deb ...
Unpacking libncurses-dev:amd64 (6.3-2ubuntu0.1) ...
Selecting previously unselected package libncurses5-dev:amd64.
Preparing to unpack .../07-libncurses5-dev_6.3-2ubuntu0.1_amd64.deb ...
Unpacking libncurses5-dev:amd64 (6.3-2ubuntu0.1) ...
Selecting previously unselected package libreadline-dev:amd64.
Preparing to unpack .../08-libreadline-dev_8.1.2-1_amd64.deb ...
Unpacking libreadline-dev:amd64 (8.1.2-1) ...
Selecting previously unselected package libssl-dev:amd64.
Preparing to unpack .../09-libssl-dev_3.0.2-0ubuntu1.12_amd64.deb ...
Unpacking libssl-dev:amd64 (3.0.2-0ubuntu1.12) ...
Selecting previously unselected package libffi-dev:amd64.
Preparing to unpack .../10-libffi-dev_3.4.2-4_amd64.deb ...
Unpacking libffi-dev:amd64 (3.4.2-4) ...
Selecting previously unselected package libyaml-dev:amd64.
Preparing to unpack .../11-libyaml-dev_0.2.2-1build2_amd64.deb ...
Unpacking libyaml-dev:amd64 (0.2.2-1build2) ...
Setting up libncurses-dev:amd64 (6.3-2ubuntu0.1) ...
Setting up libyaml-dev:amd64 (0.2.2-1build2) ...
Setting up m4 (1.4.18-5ubuntu2) ...
Setting up libreadline-dev:amd64 (8.1.2-1) ...
Setting up libffi-dev:amd64 (3.4.2-4) ...
Setting up autotools-dev (20220109.1) ...
Setting up libssl-dev:amd64 (3.0.2-0ubuntu1.12) ...
Setting up autoconf (2.71-2) ...
Setting up libncurses5-dev:amd64 (6.3-2ubuntu0.1) ...
Setting up bison (2:3.8.2+dfsg-1build1) ...
update-alternatives: using /usr/bin/bison.yacc to provide /usr/bin/yacc (yacc) in auto mode
Setting up libgdbm-dev:amd64 (1.23-1) ...
Setting up automake (1:1.16.5-1.3) ...
update-alternatives: using /usr/bin/automake-1.16 to provide /usr/bin/automake (automake) in auto mode
Processing triggers for install-info (6.8-4build1) ...
Processing triggers for man-db (2.10.2-1) ...
Scanning processes...                                                                                                                                                                              
Scanning candidates...                                                                                                                                                                             
Scanning linux images...                                                                                                                                                                           

Running kernel seems to be up-to-date.

Restarting services...
Service restarts being deferred:
 /etc/needrestart/restart.d/dbus.service
 systemctl restart getty@tty1.service
 systemctl restart networkd-dispatcher.service
 systemctl restart systemd-logind.service
 systemctl restart unattended-upgrades.service
 systemctl restart user@1000.service

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
ubuntu@ip-172-31-32-88:~$ curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash
Installing rbenv with git...
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint:   git config --global init.defaultBranch <name>
hint: 
hint: Names  chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint:   git branch -m <name>
Initialized empty Git repository in /home/ubuntu/.rbenv/.git/
Updating origin
remote: Enumerating objects: 3252, done.
remote: Counting objects: 100% (409/409), done.
remote: Compressing objects: 100% (215/215), done.
remote: Total 3252 (delta 224), reused 316 (delta 180), pack-reused 2843
Receiving objects: 100% (3252/3252), 656.40 KiB | 6.08 MiB/s, done.
Resolving deltas: 100% (2012/2012), done.
From https://github.com/rbenv/rbenv
 * [new branch]      master     -> origin/master
 * [new tag]         v0.1.0     -> v0.1.0
 * [new tag]         v0.1.1     -> v0.1.1
 * [new tag]         v0.1.2     -> v0.1.2
 * [new tag]         v0.2.0     -> v0.2.0
 * [new tag]         v0.2.1     -> v0.2.1
 * [new tag]         v0.3.0     -> v0.3.0
 * [new tag]         v0.4.0     -> v0.4.0
 * [new tag]         v1.0.0     -> v1.0.0
 * [new tag]         v1.1.0     -> v1.1.0
 * [new tag]         v1.1.1     -> v1.1.1
 * [new tag]         v1.1.2     -> v1.1.2
 * [new tag]         v1.2.0     -> v1.2.0
Branch 'master' set up to track remote branch 'master' from 'origin'.
Already on 'master'

Installing ruby-build with git...
Cloning into '/home/ubuntu/.rbenv/plugins/ruby-build'...
remote: Enumerating objects: 15830, done.
remote: Counting objects: 100% (3964/3964), done.
remote: Compressing objects: 100% (300/300), done.
remote: Total 15830 (delta 3809), reused 3750 (delta 3657), pack-reused 11866
Receiving objects: 100% (15830/15830), 3.07 MiB | 24.21 MiB/s, done.
Resolving deltas: 100% (11315/11315), done.

All done!
Note that this installer does NOT edit your shell configuration files:
1. Run `~/.rbenv/bin/rbenv init' to view instructions on how to configure rbenv for your shell.
2. Launch a new terminal window after editing shell configuration files.
3. (Optional) Run the doctor command to verify the installation:
   wget -q "https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-doctor" -O- | bash

ubuntu@ip-172-31-32-88:~$ echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
ubuntu@ip-172-31-32-88:~$ echo 'eval "$(rbenv init -)"' >> ~/.bashrc
ubuntu@ip-172-31-32-88:~$ source ~/.bashrc 
ubuntu@ip-172-31-32-88:~$ type rbenv
rbenv is a function
rbenv () 
{ 
    local command;
    command="${1:-}";
    if [ "$#" -gt 0 ]; then
        shift;
    fi;
    case "$command" in 
        rehash | shell)
            eval "$(rbenv "sh-$command" "$@")"
        ;;
        *)
            command rbenv "$command" "$@"
        ;;
    esac
}
ubuntu@ip-172-31-32-88:~$ rbenv install -l
3.0.6
3.1.4
3.2.2
3.3.0
jruby-9.4.5.0
mruby-3.2.0
picoruby-3.0.0
truffleruby-23.1.1
truffleruby+graalvm-23.1.1

Only latest stable releases for each Ruby implementation are shown.
Use `rbenv install --list-all' to show all local versions.
ubuntu@ip-172-31-32-88:~$ rbenv install 3.3.0
==> Downloading ruby-3.3.0.tar.gz...
-> curl -q -fL -o ruby-3.3.0.tar.gz https://cache.ruby-lang.org/pub/ruby/3.3/ruby-3.3.0.tar.gz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 21.0M  100 21.0M    0     0  25.0M      0 --:--:-- --:--:-- --:--:-- 24.9M
==> Installing ruby-3.3.0...
-> ./configure "--prefix=$HOME/.rbenv/versions/3.3.0" --enable-shared --with-ext=openssl,psych,+
-> make -j 2

-> make install
==> Installed ruby-3.3.0 to /home/ubuntu/.rbenv/versions/3.3.0

NOTE: to activate this Ruby version as the new default, run: rbenv global 3.3.0
ubuntu@ip-172-31-32-88:~$ 
ubuntu@ip-172-31-32-88:~$ rbenv global 3.3.0
ubuntu@ip-172-31-32-88:~$ ruby -v
ruby 3.3.0 (2023-12-25 revision 5124f9ac75) [x86_64-linux]
ubuntu@ip-172-31-32-88:~$ echo "gem: --no-document" > ~/.gemrc
ubuntu@ip-172-31-32-88:~$ gem install cztop rbczmq ffi-rzmq iruby
Fetching cztop-1.0.0.gem
Fetching ffi-1.16.3.gem
Fetching czmq-ffi-gen-1.0.0.gem
Building native extensions. This could take a while...
Successfully installed ffi-1.16.3
Successfully installed czmq-ffi-gen-1.0.0
Successfully installed cztop-1.0.0
Fetching rbczmq-1.7.9.gem
Building native extensions. This could take a while...
ERROR:  Error installing rbczmq:
        ERROR: Failed to build gem native extension.

    current directory: /home/ubuntu/.rbenv/versions/3.3.0/lib/ruby/gems/3.3.0/gems/rbczmq-1.7.9/ext/rbczmq
/home/ubuntu/.rbenv/versions/3.3.0/bin/ruby extconf.rb
"./autogen.sh"
autogen.sh: error: could not find libtool.  libtool is required to run autogen.sh.
ZeroMQ autogen failed!
*** extconf.rb failed ***
Could not create Makefile due to some reason, probably lack of necessary
libraries and/or headers.  Check the mkmf.log file for more details.  You may
need configuration options.

Provided configuration options:
        --with-opt-dir
        --without-opt-dir
        --with-opt-include=${opt-dir}/include
        --without-opt-include
        --with-opt-lib=${opt-dir}/lib
        --without-opt-lib
        --with-make-prog
        --without-make-prog
        --srcdir=.
        --curdir
        --ruby=/home/ubuntu/.rbenv/versions/3.3.0/bin/$(RUBY_BASE_NAME)
        --with-system-libs
        --without-system-libs

extconf failed, exit code 1

Gem files will remain installed in /home/ubuntu/.rbenv/versions/3.3.0/lib/ruby/gems/3.3.0/gems/rbczmq-1.7.9 for inspection.
Results logged to /home/ubuntu/.rbenv/versions/3.3.0/lib/ruby/gems/3.3.0/extensions/x86_64-linux/3.3.0/rbczmq-1.7.9/gem_make.out
Fetching ffi-rzmq-2.0.7.gem
Fetching ffi-rzmq-core-1.0.7.gem
Successfully installed ffi-rzmq-core-1.0.7
Successfully installed ffi-rzmq-2.0.7
Fetching iruby-0.7.4.gem
Fetching native-package-installer-1.1.9.gem
Fetching multi_json-1.15.0.gem
Fetching mime-types-data-3.2023.1205.gem
Fetching mime-types-3.5.1.gem
Fetching data_uri-0.1.0.gem
Successfully installed native-package-installer-1.1.9
Successfully installed multi_json-1.15.0
Successfully installed mime-types-data-3.2023.1205
Successfully installed mime-types-3.5.1
Successfully installed data_uri-0.1.0
Building native extensions. This could take a while...
Successfully installed iruby-0.7.4
11 gems installed
ubuntu@ip-172-31-32-88:~$ iruby register — force
ubuntu@ip-172-31-32-88:~$ 

