# data-analysis
A collection of data analysis projects

## Framework

* Python for data acquisition and analysis
* Tablular data:
    
* Static:
    * matplotlib
* Interactive:
    * Flask for running data API & static content
    * D3.js, dc.js for visualisation
    * bower.js for package management
    * requirejs for dependency injection

## Setup

https://askubuntu.com/questions/244641/how-to-set-up-and-use-a-virtual-python-environment-in-ubuntu

  sudo apt-get install python3 python3-pip python3-virtualenv virtualenvwrapper
  echo "source /usr/share/virtualenvwrapper/virtualenvwrapper.sh" >> ~/.
  export WORKON_HOME=~/.virtualenvs
  mkdir $WORKON_HOME
  echo "export WORKON_HOME=$WORKON_HOME" >> ~/.zshrc
  echo "export PIP_VIRTUALENV_BASE=$WORKON_HOME" >> ~/.zshrc
  source ~/.zshrc

  mkvirtualenv -p /usr/bin/python3 test

  pip install -r requirements_dev.txt
  
