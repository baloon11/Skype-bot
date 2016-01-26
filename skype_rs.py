# coding: utf-8
import Skype4Py
import os


def Commands(Message, Status):
    if Status == 'RECEIVED':
        os.system(" vlc --volume 1024 /path_to_music_file")

skype = Skype4Py.Skype()
skype.OnMessageStatus = Commands
skype.Attach()
while True:
    pass
