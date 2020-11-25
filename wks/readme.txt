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
- automate custom .zshrc + fix oh-my-zsh
- dnf install fedora-workstation-repositories  (https://fedoraproject.org/wiki/Workstation/Third_Party_Software_Repositories)
- git config (email)
- dl+mv icon pack, font
- wget vscode + do dnf install + cleanup

automate this piece of tunketing for vagrant:
  - dnf install qemu-kvm libvirt libquestfs-tools virt-install rsync vagrant
  - systemctl enable --now libvirtd

- open firewalld for kdeconnect?
- install conda? (regarding .zshrc)
  - ~/bin/conda -> ~/anaconda3/bin/conda SYMLINK!!
- install google cloud cli?

automate motd (maybe better for server playbook)
- dnf install figlet
  - sudo bash -c  "figlet $(hostname) > /etc/motd"
- dnf remove fidget

possible automation process for spotify-tui + spotifyd
- wget https://github.com/Spotifyd/spotifyd/releases/download/v0.2.24/spotifyd-linux-slim.tar.gz
  - (check sha512)
  - tar -xzvf && mv to ~/bin
  - service https://www.rockyourcode.com/spotify-in-the-terminal-with-spotify-tui-and-spotifyd/
  - sudo dnf copr enable atim/spotify-tui -y
  - sudo dnf install spotify-tui
  - cleanup tar.gz
  - leave config manual for now
