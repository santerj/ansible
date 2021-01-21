TODO:
(create user rpm package?)
- useradd santeri, set password from vault
- install rsa.pub in ~/.ssh/authorized_keys & chown santeri:santeri & chmod 644
- mod /etc/ssh/sshd_config - disable root login, enable passwordless login
- create wheel & ensure passwordless sudo
- add user to sudo
- install figlet, create hostname motd, uninstall figlet
- install .zshrc

- update packages
- install bpytop
- install docker/podman
- ensure docker/podman on boot
