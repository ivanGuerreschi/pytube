# pytube
Python program to download videos and audios from YouTube

## Install Ubuntu dependencies
sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0

## Create venv
python3 -m venv venv

## Activate venv
. venv/bin/activate

## Install PyGObject
pip3 install PyGObject youtube-dl

## Run
python pytube.py
