Homework Part 1 
===============

Original assignment
-------------------

	You have complete freedom in the tools you want to use to accomplish this task, that includes
	working with a server OS of your choice. Start by building an application that will display
	information about the current machine that the web application is running on, in a webpage that
	can be accessed by an external browser. It should display the following (not limited to):
	
	 - CPU usage
	 - Memory usage
	 - Disk Usage
	 - OS Version

Solution
--------

The [code](source/), which returns the required server information, is written in Python using the [Bottle](http://bottlepy.org/docs/dev/index.html) web micro web framework. Bottle was chosen for its extremely small size.  A cross platform python library called [psutil](https://pypi.python.org/pypi/psutil) was used to retrieve the information from the server. Choosing Python, Bottle and psutil enables this code to be run on Linux, Windows or OSX.

The code is configured to run the web server on port 8000.

The data for the server is returned in both a "human readable" format  and a JSON format. JSON was used as the return format so that it can be easily consumed by any other application. 

When the url is called with no query string parameters ([http://localhost](http://localhost)), the human readable format is displayed.  When the webpage is called with the query string  format=json ([http://localhost?format=json](http://localhost?format=json)), the json data is displayed. 
 

Human readable format from [http://localhost](http://localhost):
![Single Server Human Readable](docs/images/single-server.png)

JSON output format from [http://localhost?format=json](http://localhost?format=json):

	{
	  "disk_usage": 3.1,
	  "cpu_usage": 1.5,
	  "memory_usage": 29.4,
	  "memory_details": {
	    "swap": {
	      "total": 0,
	      "percent": 0.0
	    },
	    "virtual": {
	      "total": 513818624,
	      "percent": 29.4
	    }
	  },
	  "hostname": "vagrant-ubuntu-trusty-64",
	  "os_version": "Linux-3.13.0-36-generic-x86_64-with-Ubuntu-14.04-trusty",
	  "boottime": "2014-10-10 10:46:09",
	  "cpu_details": {
	    "count": 1,
	    "details": [
	      {
	        "cpu_usage": 1.1,
	        "name": 0
	      }
	    ]
	  },
	  "disk_details": {
	    "partition_count": 1,
	    "iostats": {
	      "write_bytes": 405655552,
	      "read_count": 10891,
	      "write_count": 6784,
	      "read_time": 5256,
	      "read_bytes": 271176704,
	      "write_time": 18308
	    },
	    "partitions": [
	      {
	        "device": "/dev/sda1",
	        "mountpoint": "/",
	        "total": 42241163264,
	        "percent": 3.1
	      }
	    ]
	  }
	}
 
NOTE: Due to the simplicity of this code, no tests were written.  