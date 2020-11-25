Automate installation of useful programs and configuration of home directory + shell.
Useful for fresh OS installations - familiar programs are installed and configured with minimal
extra work!


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
  $ git checkout dev
  $ vagrant up


TODO:
- dnf install figlet
  - sudo bash -c  "figlet $(hostname) > /etc/motd"
- automate .zshrc
- dnf install fedora-workstation-repositories  (https://fedoraproject.org/wiki/Workstation/Third_Party_Software_Repositories)
- git config (email)
- dl+mv icon pack, font
- wget vscode + do dnf install
- open firewalld for kdeconnect?
- install conda? (regarding .zshrc)
- automate this piece of tunketing for vagrant:
  - dnf install qemu-kvm libvirt libquestfs-tools virt-install rsync vagrant
  - systemctl enable --now libvirtd
