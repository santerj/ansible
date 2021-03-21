Freshly installed Linux again - but now I have to install all my packages and configurations again...
No! Just use this Ansible playbook as an "extra step" after the actual OS installation to automate installation
of all the familiar packages and configurations. Supports the latest Fedora version (hopefully).

Also provided is a Vagrantfile (https://www.vagrantup.com/) to automate the testing part (Ansible currently lacks a no-op mode).

-----

Requirements:
- Fedora 33
- non-root user with sudo permissions
- git


Installation:
  $ git clone https://github.com/santerj/tilde
  $ /bin/sh tilde/ansible/bootstrap.sh


All done!



-----

Testing with Vagrant:
  $ git clone https://github.com/santerj/ansible
  $ cd ansible/wks
  $ vagrant up