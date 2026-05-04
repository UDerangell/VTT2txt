#!/bin/bash

# Script to list all .vtt files and wrap each line in quotes

# Define the output file
OUTPUT_FILE="vttlist.sh"

# List all .vtt files to the text file
echo "Listing all .vtt files..."
ls *.vtt > "$OUTPUT_FILE" 2>/dev/null

# Check if any .vtt files were found
if [ ! -s "$OUTPUT_FILE" ]; then
    echo "No .vtt files found in the current directory."
    exit 1
fi

echo "Found .vtt files, saved to $OUTPUT_FILE"

# Create a temporary file for editing
TEMP_FILE=$(mktemp)

# Read each line from the original file and wrap it in quotes with ./vtt.sh prefix
while IFS= read -r line; do
    echo "./vtt.sh \"$line\"" >> "$TEMP_FILE"
done < "$OUTPUT_FILE"

# Replace the original file with the quoted version
mv "$TEMP_FILE" "$OUTPUT_FILE"

echo "Successfully added ./vtt.sh prefix and wrapped each filename in quotes in $OUTPUT_FILE"
#echo "Contents of $OUTPUT_FILE:"
#cat "$OUTPUT_FILE"

# Make the output file executable
chmod u+x "$OUTPUT_FILE"
