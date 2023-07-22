#!/bin/bash

echo "=================================================APT UPDATE START"
sudo sed -i "s/http:\/\/security.ubuntu.com/https:\/\/mirror.kakao.com/g" /etc/apt/sources.list
sudo sed -i "s/http:\/\/kr.archive.ubuntu.com/https:\/\/mirror.kakao.com/g" /etc/apt/sources.list
sudo apt-get update
sudo apt-get install -y net-tools

echo "=================================================APT UPDATE END"



echo "=================================================ZSH START"
sudo apt-get install -y curl zsh

sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
echo "=================================================ZSH END"
