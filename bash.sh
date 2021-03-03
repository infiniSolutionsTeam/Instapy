#!/bin/bash

echo "Hello! This is Installing instapy and neceesary things."

sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install unzip python3-pip python3-dev build-essential libssl-dev libffi-dev xvfb
sudo apt install python3
sudo apt install -y python-pip
sudo apt install -y python3-pip
sudo pip3 install --upgrade pip
curl -fsSL -o- https://bootstrap.pypa.io/3.5/get-pip.py | python3.5
pip install instapy
pip3 install instapy
sudo apt install -y firefox-geckodriver
sudo pip install -y instapy --ignore-installed

echo "Install Completed"