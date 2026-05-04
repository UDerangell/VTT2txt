./rename_script.sh "$1" > vttfname.txt
newfile=$(cat vttfname.txt)
echo "Renamed file: $newfile"
echo "Running humantr.sh"
./humantr.sh $newfile
