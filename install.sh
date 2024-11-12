#! /bin/bash

# Install the required support programs
pip install gTTS requests
pip install pydub
pip install DateTime
apt-get install ffmpeg -y
apt-get install libavcodec-unstripped-52 libavdevice-unstripped-52 -y
