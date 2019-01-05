# djangonx
A sample django project configured with nginx in a Debian Stretch VM.


### Techs
1. Debian Stretch VM
2. Python/Django
3. nginx

## Project description

### Installed
1. Django
2. SQLite
3. django-allauth


### Features
1. User can register
2. User can login
3. User can view profile
4. User can go to the django admin


### Superuser Credential

```
user: shahjalalh
pass: admin1234
```


## Install the Debian VM and connect with it
First install Debian in the Oracle Virtual Box. Then connect the vm with ssh from host OS. The ssh connection preparation is described in - https://github.com/shahjalalh/ssh-to-debian-vm

Note: Now the VM will act like DigitalOcean droplet. Let's call it **Debian droplet**. :P


## Install Git and Nginx in the Debian droplet
### First install git in the droplet

```
$ su -
# apt-get update
# apt-get install git
```

### Install virtual environment in Python 3
```
$ mkdir workspacepython
$ cd workspacepython/
$
$ pip install virtualenv
-bash: pip: command not found
$ su -
Password: 
# apt-get install python-pip
# exit
$ pip install virtualenv
$ sudo /usr/bin/easy_install virtualenv
```

Or,
Download get-pip.py from https://pip.pypa.io/en/stable/installing/
```
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python get-pip.py
$ python3 get-pip.py
$ su -
Password: 
# /usr/bin/easy_install virtualenv
```

Now we are ready to create the virtual environment

```
$ which python3
/usr/bin/python3
$ 
$ virtualenv -p /usr/bin/python3 py3env
Already using interpreter /usr/bin/python3
Using base prefix '/usr'
New python executable in /home/shahjalal/workspacepython/py3env/bin/python3
Also creating executable in /home/shahjalal/workspacepython/py3env/bin/python
Installing setuptools, pip, wheel...
done.
$ source py3env/bin/activate
(py3env) $ python
Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
(py3env) $
```

### Pull code from git
Our project git repo is https://github.com/shahjalalh/djangonx.git. We need to clone -

```
(py3env) $ git clone https://github.com/shahjalalh/djangonx.git
(py3env) $ cd djangonx/
(py3env) djangonx $ pip install -r requirements.txt
(py3env) djangonx $ python manage.py runserver 0.0.0.0:8000
```
### Create a new port forwarding 
Create a new port forwarding same as https://github.com/shahjalalh/ssh-to-debian-vm, **Step 3: Enable port forwarding**. And restart the server

Name: web
Protocol: TCP
Host IP:
Host Port: 8000
Guest IP:
Guest Port: 8000

Enter into the guest server and run the Django app
```
(py3env) djangonx $ python manage.py runserver 0.0.0.0:8000
```

Now browse http://localhost:8000/ from host OS browser.


