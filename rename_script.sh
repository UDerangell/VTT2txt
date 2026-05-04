#!/bin/bash

# Function to display usage information
show_usage() {
    echo "Usage: $0 <filename>"
    echo "Example: $0 'My File (2) - Special!.txt'"
    echo "This script replaces spaces and special characters with underscores"
    echo "while maintaining the original filename length."
}

# Check if argument is provided
if [ $# -ne 1 ]; then
    show_usage
    exit 1
fi

# Store the original filename
original_file="$1"

# Check if the file exists
if [ ! -e "$original_file" ]; then
    echo "Error: File '$original_file' does not exist."
    exit 1
fi

# Extract file extension (if present)
filename=$(basename -- "$original_file")
extension=""
if [[ "$filename" == *.* ]]; then
    extension=".${filename##*.}"
    filename="${filename%.*}"
fi

# Replace spaces and special characters with underscores in the filename part only
clean_filename=$(echo "$filename" | tr ' !@#$%^&*()[]{}=+;:",.<>/?\|~`' '_')

# Reconstruct the full new name with preserved extension
new_name="${clean_filename}${extension}"

# Rename the file
if [ "$original_file" != "$new_name" ]; then
    mv "$original_file" "$new_name"
    echo "$clean_filename"
else
    echo "No need to rename. File doesn't contain spaces or special characters."
fi

exit 0
