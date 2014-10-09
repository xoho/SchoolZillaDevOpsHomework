Solution for Part 1 and 2 
=========================

Since the two parts of the homework are intertwined, the solution for both parts is expressed in this document.

The OS chosen for this solution is Ubuntu 14.01. However, this solution was designed to work on nearly any operating system including Windows.

The vagrant provisioning mechanism chosen for this solution is "shell" provisioning. While puppet or chef could have also been used, the "shell" provisioning is the most simple and straight forward and fits well with this solution.  Additionally, due to the simplicity of the solution, all provisioning details are included in the main Vagrant file using the variable assignment feature of vagrant shell provisioning.  The Vagrant file is located in the same folder as this file.

The code which returns the pertinent server information is written in Python using the [Bottle](http://bottlepy.org/docs/dev/index.html) web micro web framework. Bottle was chosen for its extremely small size.

The web server runs on port 8000 in the vagrant vm and is exposed, per request to the host machine on port 80.

An upstart script has been written which will automatically start the server on any reload of the vm.

There are two folders associated with this solution:

 - [provision](provision) - contains all files necessary for provisioning
 - [source](source) - contains all files necessary to run the application

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