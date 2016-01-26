# Skype bot

This small script uses Skype api and
python library Skype4Py, which is wrapper around this api.

https://pypi.python.org/pypi/Skype4Py/

The script waits for Skype event - 'a new message'
and run to play a music file (using vlc)

----------------------------------------------

#### Requirements
------------
python 2.7

    sudo apt-get install vlc
    sudo pip install Skype4Py

#### Note:

    This script listening messages,which sends Skype.
    The mechanism of transmission of these messages hidden deeply in Linux.
    So the script does not work in a virtual environment (env)
