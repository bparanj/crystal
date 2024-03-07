## Minimal Package Dependencies

Installing Postgresql server and Ruby from source.

```
sudo apt-get update && sudo apt-get upgrade -y

sudo apt update
sudo apt install postgresql

gem update --system 3.5.6
sudo gem update --system 3.5.6

sudo apt-get install build-essential
sudo apt install git autoconf bison build-essential libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm6 libgdbm-dev libdb-dev -y
wget https://cache.ruby-lang.org/pub/ruby/3.3/ruby-3.3.0.tar.gz
tar -xzvf ruby-3.3.0.tar.gz 
cd ruby-3.3.0/
./configure
make
sudo make install
ruby -v
gem env

sudo gem install rails
sudo apt install libpq-dev
gem install pg
rails new myapp --database=postgresql
```

Verify package installation:

```
dpkg -l libpq-dev
```