# -*- mode: ruby -*-
# vi: set ft=ruby :


# This is the provision script
$script = <<SCRIPT
echo Provisioning...
# provision script for SchoolZillaDevOpsHomework

# Base requirements
echo Installing base requirements...
apt-get update
apt-get install -y python-dev build-essential python-pip 

# Install libs
echo Installing necessary libraries
pip install bottle
pip install psutil

# Configure 

# Create upstart script so we can restart if rebooted
echo Configuring environment
cp /vagrant/provision/szmon.conf /etc/init/
initctl reload-configuration
service szmon start

SCRIPT



# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 8000, host: 80
  config.vm.provision "shell", inline: $script
end
