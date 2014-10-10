# provision script for SchoolZillaDevOpsHomework

echo Provisioning...

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

