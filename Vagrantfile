#!/usr/bin/env ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "ubuntu/trusty64"

  config.vm.define "lb" do |lb|
    lb.vm.network :private_network, ip: "20.0.0.2"
    lb.vm.provision :shell, :path => "devops/lb_provision.sh"
  end

  config.vm.define "appOne" do |appOne|
    appOne.vm.network :private_network, ip: "20.0.0.3"
    appOne.vm.provision :shell, :path => "devops/app_provision.sh"
  end

  config.vm.define "appTwo" do |appTwo|
    appTwo.vm.network :private_network, ip: "20.0.0.4"
    appTwo.vm.provision :shell, :path => "devops/app_provision.sh"
  end

  config.vm.define "consul_server" do |consul_server|
    consul_server.vm.network :private_network, ip: "20.0.0.5"
  end

  # Prevent Ubuntu Precise DNS resolution from mysteriously failing
  # http://askubuntu.com/a/239454
  config.vm.provider "virtualbox" do |vb| 
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end

  # Cache apt-get package downloads to speed things up
  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box
    config.cache.enable :generic, { :cache_dir => "/var/cache/pip" }
  end

end