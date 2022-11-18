# Minimal bootstrap for RHEL8-compatible OS

Run with:
## `ansible-playbook playbook.yml -i hosts`

Contents:
  - Create admin user + install SSH key
  - Install + update packages
  - Configure wheel group + sudo rules
  - Configure hostname
  - Configure sshd + firewalld

TODO maybe 🤔:
  - fail2ban
  - login-police
  - figure out what to do with selinux