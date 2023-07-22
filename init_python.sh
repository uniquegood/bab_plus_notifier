#!/bin/zsh

echo "=================================================ADD PYTHON START"

sudo apt-get upgrade python3
sudo apt install python3-pip

pip3 install -r requirements.txt

echo "=================================================ADD PYTHON END"
