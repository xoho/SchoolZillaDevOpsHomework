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

JSON is used as the return format so that it can be easily consumed by any other application.  The data returned by this application via a web call has the following structure (and example data):

    {
      "disk_usage": 3.1,
      "cpu_usage": 0.7,
      "memory_usage": 25.7,
      "memory_details": {
        "swap": {
          "total": 0,
          "percent": 0.0
        },
        "virtual": {
          "total": 513818624,
          "percent": 25.7
        }
      },
      "os_version": "linux2",
      "cpu_details": {
        "count": 1,
        "details": [
          0.7
        ]
      },
      "disk_details": {
        "partition_count": 1,
        "iostats": {
          "write_bytes": 657858560,
          "read_count": 7045,
          "write_count": 1531,
          "read_time": 4528,
          "read_bytes": 198636544,
          "write_time": 2180
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
 