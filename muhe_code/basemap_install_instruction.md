## Installation
basemap and GEOS (Geometry Engine - Open Source) library are required for showing features on the map, the package (basemap-1.0.7.tar.gz) is already downloaded in the folder **resource**.
The below instructions come from:              
http://matplotlib.org/basemap/users/installing.html
### step 1
If numpy 1.0.0 or later, python 2.4 or later, matplotlib 1.0.0 or later are installed, go to     step2, otherwise install them
### step 2
Untar the basemap-1.0.7.tar.gz file in the folder *resource*, and and cd to the **basemap-1.0.7** directory
### step 3
**1 If you already have GEOS library on your system**, just set the environment variable GEOS_DIR to point to the location of libgeos_c and geos_c.h (if libgeos_c is in /usr/local/lib and geos_c.h is in /usr/local/include, set GEOS_DIR to /usr/local). Then go to next step. 

**2 If you don’t have it**, you can build it from the source code included with basemap by using following commands in the ubuntu command line:
* cd to the geos-3.3.3 directory
```sh
$ cd geos-3.3.3
```
* setting environment variable GEOS_DIR and Install the GEOS library
```sh
$ export GEOS_DIR= /home/ds-ga-1007  
#It is your home directory, I recommend this.
#If any permission wrong happens, use sudo su to get the super user authority, or get root authority
$ ./configure --prefix=$GEOS_DIR
#I recommend you to get super user authority here
$ sudo su #then enter the password
$ make; make install
```
`to be modified:it will take you several several minutes to finish this, you will see balala`
### step 4
cd back to the top level basemap directory (basemap-1.0.7) and run the usual **python setup.py install**. Check your installation by running **from mpl_toolkits.basemap import Basemap** at the python prompt.
```sh
$ cd basemap-1.0.7
#make sure you have super user authority 
$ sudo su
$ python setup.py install
$ python
$ from mpl_toolkits.basemap import Basemap
```
`to be modified:it will take you several several minutes to finish this,there may be some warnings and errors, but will not affect the function`

