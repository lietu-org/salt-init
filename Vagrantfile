# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    config.vm.box = "chef/centos-7.0"
    #config.vm.box = "ubuntu/trusty64"


    config.vm.boot_timeout = 30

    config.ssh.forward_agent = true

    # Define the vm
    vm_name = "lstest"
    config.vm.define :lstest do |lstest|
        lstest.vm.hostname = vm_name

        lstest.vm.synced_folder ".",           "/src/"

        lstest.vm.provider "virtualbox" do |v|
            v.name = vm_name
            v.customize ["modifyvm", :id, "--memory", "256"]
        end
    end
end
