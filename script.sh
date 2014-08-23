echo "Hello External Script"

#Create alias to ls so that it's easier to read the directories
#echo 'alias ls="ls -GFh"' >> .bash_profile

#Install setuptools easy packaging and installation facilities
echo "Installing setuptools"
echo " "
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | sudo python

#Install pip, the tool for installing and managing Python packages
echo "Installing pip"
echo " "
sudo easy_install pip

#Install Virtualenv, providing the ability to create virtual Python environments that
#don't interfere wih each other or the main Python installation. 
echo "Installing virtualenv"
echo " "
sudo pip install virtualenv

#Install sqlite3
echo "Installing sqlite3"
echo "  "
sudo apt-get install sqlite3

