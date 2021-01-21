Vagrant.configure("2") do |config|
  config.vm.box = "fedora/33-cloud-base"
  config.vm.box_version = "33.20201019.0"
  config.vm.hostname = "ansibletest.box"

  config.vm.provider :libvirt do |libvirt|
    libvirt.cpus = 1
    libvirt.memory = 1024
  end

  config.vm.provision "ansible" do |ansible|
    ansible.become_user = "root"
    ansible.verbose = "vvv"
    ansible.playbook = "playbook.yaml"
  end

end

