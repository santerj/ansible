Install programs and configure shell+home with a little help from Ansible.

Requirements:
- Fedora 33
- non-root user with sudo permissions
- git


Installation:
  $ git clone https://github.com/santerj/tilde
  $ /bin/sh tilde/ansible/bootstrap.sh


All done!




---
Testing with Vagrant:
  $ git clone https://github.com/santerj/ansible
  $ cd ansible/wks
  $ git checkout devel
  $ vagrant up


TODO:
- update PATH to include ~/bin
- set editor as vim
- enable correction in oh-my-zsh
- git config
- dl+mv icon pack, font
- wget vscode + do dnf install
- open firewalld for kdeconnect?
- automate this piece of tunketing for vagrant:
  - dnf install qemu-kvm libvirt libquestfs-tools virt-install rsync vagrant
  - systemctl enable --now libvirtd
