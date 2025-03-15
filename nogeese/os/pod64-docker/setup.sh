#!/usr/bin/sudo bash
cd /etc
sudo echo "" >> pacman.conf
sudo echo "# Nogeese Repositories" >> pacman.conf
sudo echo "[nogeese]" >> pacman.conf
sudo echo "Server = https://raw.githubusercontent.com/nogeese-org/mirror/stable/nogeese/os/pod64-docker"
sudo echo "SigLevel = Optional TrustAll"
