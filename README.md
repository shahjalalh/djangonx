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
First install git in the droplet

```
shahjalal@shahjalal:~$ su -
root@shahjalal:~# apt-get update
root@shahjalal:~# apt-get install git
```

