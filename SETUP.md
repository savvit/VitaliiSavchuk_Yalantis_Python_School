# Deployment instructions( on Linux )
## Step 1 — Install Python and pip
To install Python we must first update the local APT repository.
```
sudo apt-get update && sudo apt-get -y upgrade
```
Then we can install Python 3 by using the following command:
```
sudo apt-get install python3
```
Also, you check the Python version by using the following command:
```
python3 -V
```
Now that we have Python 3 installed, we will also need pip in order to install packages from PyPi, Python’s package repository.
```
sudo apt-get install -y python3-pip
```
To verify that pip was successfully installed, run the following command:
```
pip3 -V
```
## Step 2 — Install virtualenv
__virtualenv__ - is a tool for creating isolated Python environments containing their own copy of python ,pip , and their own place to keep libraries installed from PyPI.

To install virtualenv, we will use the __pip3__ command, as shown below:
```
pip3 install virtualenv
```
Once it is installed and you don't have any errors it means you have successfully installed __virtualenv__.
## Step 3 — Install Django
Lets'  create home directory for Django project
```
mkdir django-app
cd django-app
```
Now we inside in `django-app` directory, next create your virtual environment and call it __django_env__:
```
virtualenv django_env
```
Then you need to activate the environment:
```
source django_env/bin/activate
```
If you see a (django_env) at the beginning of the command line, then you know the virtualenv is activated.
Next, we have to clone our project from the repository. Before that I suggest installing the git:
```
sudo apt install git
```
and clone project:
```
https://github.com/savvit/VitaliiSavchuk_Yalantis_Python_School.git
```
After cloning you have to install `requirements.txt`
This file is used for specifying what python packages are required to run the project.
```
pip install -r requirements.txt
```
And now you can safely launch the project with command:
```
./manage.py runserver
```
