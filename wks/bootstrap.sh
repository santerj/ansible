echo "Installing Ansible..."
sudo dnf install ansible -y
echo "Installing required Ansible packages..."
ansible-galaxy collection install community.general
echo "Beginning playbook run..."
ansible-playbook ansible/wks/playbook.yaml --ask-become-pass || echo "Cleaning up..." && rm -rf ansible && echo "All done! New shell available at next login."
