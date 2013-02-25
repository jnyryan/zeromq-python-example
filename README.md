zeromq-python-example
=====================

A playaround with zmq and python

# Usage

	python ./zmq_listener.py
	
	run as many publishers as you want
	python ./zmq_publisher.py
	python ./zmq_publisher.py
	
# Setup

	## python
	sudo apt-get -y install python-dev
	sudo apt-get -y install python-pip
	 
	## zeromq
	sudo apt-get -y install libzmq-dev
	sudo easy_install pyzmq
	
if you have trouble here are some base dependencies that I find are always needed
# These are my basic installs that i use for day to day development
sudo apt-get -y install autoconf automake bison build-essential curl freetds-dev git-core 
sudo apt-get -y install libc6-dev libcurl4-openssl-dev libncursesw5-dev libreadline-dev libreadline6 libreadline6-dev 
sudo apt-get -y install libsqlite3-dev libssl-dev libtool libxml2 libxml2-dev libxslt-dev libxslt1-dev libyaml-dev 
sudo apt-get -y install ncurses-dev openssl rubygems scons sqlite3 subversion zlib1g zlib1g-dev 
