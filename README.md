# VTT2txt
bulk convert VTT files to readable text files

These scripts can be used to convert a directory that contains VTT files to readable text files.

VTT files can be downloaded from Youtube videos using the YT-DLP package. (https://github.com/yt-dlp/yt-dlp)
This is done by adding the command line option: --write-auto-subs
If you just want to download VTT files without the associated video/audio, use the option: --skip-download
You may also need to use this option to authenticate to Youtube: --cookies-from-browser chrome

To use the scripts in this repository:

1. First, install the webvtt-py library:
pip install webvtt-py

2. Create a virtual environment for the Python script

