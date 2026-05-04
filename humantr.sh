sed -E 's/<[^>]*>//g' $1.vtt | grep -v "^WEBVTT" | grep -v "^$" | grep -v "^[[:space:]]*$" | grep -v "[0-9]:[0-9][0-9]:[0-9][0-9]" > $1.tx1
python3 -m venv captions
source captions/bin/activate
python3 remove_duplicate_lines.py $1.tx1 $1.txt
deactivate
rm -f $1.tx1
