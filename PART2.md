Homework Part 2 
===============

Original assignment
-------------------

	Create a Vagrant file that will “spin” up a server and install your web application. You can use any
	bootstrapping method that you want (Chef, Puppet, Shell Scripts, etc.) but you should only need
	to run one command (vagrant up) to get the server operational. When you navigate to localhost
	on your local machine, it should be pointing to the port this web app is listening to on the guest
	machine.

Solution
--------

The OS chosen for this Vagrant instance is Ubuntu 14.01 LTS. 

The vagrant provisioning mechanism chosen for this solution is "shell" provisioning. While puppet or chef could have also been used, the "shell" provisioning is the most simple and straight forward and fits well with this solution.  

The [Vagrant](Vagrant) file is located in the same folder as this file.

All provisioning takes place in the [provision.sh](provision/provision.sh) file. This file installs the necessary dependencies and libraries to run this solution.

An [upstart script](provision/szmon.conf) (found in the [provision](provision) has been written which will automatically start the server on any reload of the vm (vagrant reload or vagrant halt/vagrant up).

The Vagrant VM is configured to map port 8000 on the guest VM to the host machine on port 80 so that navigating to [http://localhost](http://localhost) on the host machine yields the contents of the page.

The Vagrant VM will boot and host the application found in the [source](source) folder (see [part 1 solution](PART1.md)).

This solution consists of two key parts
 
 - The [Vagrant](VagrantFile) file containing the definition and provisioning script
 - The [provision](provision) folder which contains all files necessary for deploying to the Vagrant VM

The server is completely deployed and started with the **vagrant up** command.