#/bin/bash

echo "Updating system"
apt-get -qq update
apt-get -yqqf upgrade

# Git
command -v git > /dev/null
if [ $? -ne 0 ]; then
    echo "Installing Git"
    apt-get -yqq install git
fi

# Python Pip
command -v pip > /dev/null
if [ $? -ne 0 ]; then
    echo "Installing python-pip"
    apt-get -yqq install python-pip
fi