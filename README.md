# zeromq-python-example

A playaround with zmq and python

## listener / publisher example

From http://drumcoder.co.uk/blog/2010/dec/05/simple-zeromq-ubuntu/

	python ./zmq_listener.py
	python ./zmq_publisher.py
	python ./zmq_publisher.py
	
	
## Work Queue Example

From https://github.com/taotetek/blog_examples/blob/master/python_multiprocessing_with_zeromq/workqueue_example.py
	
	./workqueue_example.py
	
## Setup

	## python
	sudo apt-get -y install python-dev
	sudo apt-get -y install python-pip
	 
	## zeromq
	sudo apt-get -y install libzmq-dev
	sudo easy_install pyzmq
	
##Troubleshooting

If you have trouble here are some base dependencies that I find are always needed

	sudo apt-get -y install autoconf automake bison build-essential curl freetds-dev git-core 
	sudo apt-get -y install libc6-dev libcurl4-openssl-dev libncursesw5-dev libreadline-dev libreadline6 libreadline6-dev 
	sudo apt-get -y install libsqlite3-dev libssl-dev libtool libxml2 libxml2-dev libxslt-dev libxslt1-dev libyaml-dev 
	sudo apt-get -y install ncurses-dev openssl rubygems scons sqlite3 subversion zlib1g zlib1g-dev
 
