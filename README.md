P2Pool - Harambecoin
=========================
Straighforward fork of p2pool with harambecoin network info added. Instructions
are also provided in this readme for using p2pool specifically for harambecoin.

*NOTE*
Right now the subsidy function uses a quick and dirty hack to just set the 
value equal to the initial reward. This should work, however, after block
29200 the first subsidy change occurs and all p2pool nodes will need to be 
updated with the actual subsidy function (which will hopefully be availible by
then).

Requirements:
-------------------------
Generic:
* Bitcoin >=0.11.1
* Python >=2.6
* Twisted >=10.0.0
* python-argparse (for Python =2.6)

Linux:
* sudo apt-get install python-zope.interface python-twisted python-twisted-web
* sudo apt-get install python-argparse # if on Python 2.6

Windows:
* Install Python 2.7: http://www.python.org/getit/
* Install Twisted: http://twistedmatrix.com/trac/wiki/Downloads
* Install Zope.Interface: http://pypi.python.org/pypi/zope.interface/3.8.0
* Install python win32 api: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
* Install python win32 api wmi wrapper: https://pypi.python.org/pypi/WMI/#downloads
* Unzip the files into C:\Python27\Lib\site-packages

In order to run P2Pool with the Harambecoin network, you would need to build and
install the ltc_scrypt module that includes the scrypt proof of work code that 
Harambecoin uses for hashes.

Linux:

    cd litecoin_scrypt
    sudo python setup.py install

Windows (mingw):
* Install MinGW: http://www.mingw.org/wiki/Getting_Started
* Install Python 2.7: http://www.python.org/getit/

In bash type this:

    cd litecoin_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install

Windows (Microsoft Visual C++)
* Open visual studio console

In bash type this:

    SET VS90COMNTOOLS=%VS110COMNTOOLS%	           # For visual c++ 2012
    SET VS90COMNTOOLS=%VS100COMNTOOLS%             # For visual c++ 2010
    cd litecoin_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install
	
If you run into an error with unrecognized command line option '-mno-cygwin', 
see this:
http://stackoverflow.com/questions/6034390/compiling-with-cython-and-mingw-produces-gcc-error-unrecognized-command-line-o

Running P2Pool:
-------------------------
To use P2Pool, you must be running your own local harambecoind with server=1 
enabled in your .conf file or with the -server flag. Also make sure that you 
have all dependencies installed including compiling the ltc_scrypt module (see
requirements section). Launch p2pool with the following

	python run_p2pool.py --net harambecoin -a <HARAMBECOINADDRESS>

Run your miner program, connecting to 127.0.0.1 on port 53000 with any
username and password.

For additional options or to try and troubleshoot any errors you may be 
encounter, run:

    python run_p2pool.py --help

You can view statistics from your node by opening 127.0.0.1:53000 in a web 
browser.

Sponsors:
-------------------------

Thanks to:
* The Bitcoin Foundation for its generous support of P2Pool
* The Litecoin Project for its generous donations to P2Pool
 
License:
-------------------------

[Available here](COPYING)


