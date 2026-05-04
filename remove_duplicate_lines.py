#!/usr/bin/env python3
"""
Script to remove consecutive duplicate lines from a text file.
Usage: python remove_duplicate_lines.py input_file output_file
"""

import sys

def remove_consecutive_duplicates(input_file, output_file):
    """
    Read lines from input_file and write to output_file, skipping lines
    that are identical to the previous line.
    
    Args:
        input_file (str): Path to the input file
        output_file (str): Path to the output file
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as in_f:
            with open(output_file, 'w', encoding='utf-8') as out_f:
                previous_line = None
                for line in in_f:
                    # Only write the line if it's different from the previous one
                    if line != previous_line:
                        out_f.write(line)
                    previous_line = line
        print(f"Processing complete. Output written to {output_file}")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied when accessing file.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def main():
    # Check command line arguments
    if len(sys.argv) != 3:
        print("Usage: python remove_duplicate_lines.py input_file output_file")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    remove_consecutive_duplicates(input_file, output_file)

if __name__ == "__main__":
    main()
