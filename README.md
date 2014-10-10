SchoolZilla DevOps Homework
===========================

Prepared by [Eric Hoxworth](mailto:eric.hoxworth@gmail.com)


Original Homework Assignment
----------------------------

Imagine you’re building the beginnings of an internal Schoolzilla administration tool that will be
leveraged to assist with the monitoring and management of our web application. The first thing
you decide to do is to build a really simple web application that displays information about the
server that it is running on. This web application will need to be running on all of our servers so
we will need to template and automate the building / configuration of the web application.
Because of this requirement, you have decided to use Vagrant as a part of your development
process. Vagrant is a tool for automating the creation of virtual machines on your local computer.
It integrates with a hypervisor (e.g. VirtualBox) and can bootstrap a new development server just
by running a single command.

**Part 1**

You have complete freedom in the tools you want to use to accomplish this task, that includes
working with a server OS of your choice. Start by building an application that will display
information about the current machine that the web application is running on, in a webpage that
can be accessed by an external browser. It should display the following (not limited to):

 - CPU usage
 - Memory usage
 - Disk Usage
 - OS Version

see [**Solution to Part 1**](PART1.md)


**Part 2**

Create a Vagrant file that will “spin” up a server and install your web application. You can use any
bootstrapping method that you want (Chef, Puppet, Shell Scripts, etc.) but you should only need
to run one command (vagrant up) to get the server operational. When you navigate to localhost
on your local machine, it should be pointing to the port this web app is listening to on the guest
machine.

see [**Solution to Part 2**](PART2.md)


**Part 3**

Assume that this is just the beginning. We would like to build up this tool to help with many tasks
such as:

 - Local health checks
 - Service Orchestration
 - System Task Management
 - Automated Release Deployment

How might we address the following:

 - From a high level view, what might this look like? What are the pieces involved and how
do they all fit together?
 - If there are ‘agents’ installed on all of our servers, how might we go about creating an
admin interface that will let us to manage all of these agents?

see [**Solution to Part 3**](PART3.md)

Deliverables
------------

 - A [Git repo](https://github.com/xoho/SchoolZillaDevOpsHomework) that contains the web application and vagrant resources required to spin up a
virtual machine.
 - A [document](PART3.md) addressing future plans for Schoolzilla’s admin tool.