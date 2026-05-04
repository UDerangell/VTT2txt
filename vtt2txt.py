import webvtt
import argparse
import sys
import re
from datetime import timedelta

def format_timestamp(timestamp):
    """Convert WebVTT timestamp to a simpler format (MM:SS)"""
    # Parse the timestamp
    hours, minutes, seconds = map(float, timestamp.replace(',', '.').split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    # Format as MM:SS
    mins = int(total_seconds // 60)
    secs = int(total_seconds % 60)
    return f"[{mins:02d}:{secs:02d}]"

def clean_text(text):
    """Clean up the text by removing HTML tags and redundant spaces"""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    # Remove speaker identifiers like "Speaker: " if needed
    # text = re.sub(r'^\s*[A-Za-z]+:\s*', '', text)
    return text.strip()

def vtt_to_transcript(vtt_file, output_file=None, include_timestamps=True, merge_lines=True):
    """Convert VTT file to human readable transcript"""
    try:
        # Parse the VTT file
        captions = webvtt.read(vtt_file)
        
        # Prepare output
        lines = []
        current_text = ""
        last_end_time = None
        
        for caption in captions:
            # Clean the text
            clean_caption = clean_text(caption.text)
            
            # Skip empty captions
            if not clean_caption:
                continue
                
            # Decide whether to start a new paragraph
            if not merge_lines or not current_text or (last_end_time and caption.start > last_end_time + timedelta(seconds=2)):
                if current_text:
                    lines.append(current_text)
                
                if include_timestamps:
                    current_text = f"{format_timestamp(caption.start)} {clean_caption}"
                else:
                    current_text = clean_caption
            else:
                # Continue the current paragraph
                current_text += " " + clean_caption
            
            last_end_time = caption.end
        
        # Add the last paragraph
        if current_text:
            lines.append(current_text)
        
        # Create the final transcript
        transcript = "\n\n".join(lines)
        
        # Output
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(transcript)
            print(f"Transcript saved to {output_file}")
        else:
            print(transcript)
            
        return transcript
        
    except Exception as e:
        print(f"Error processing VTT file: {e}", file=sys.stderr)
        return None

def main():
    parser = argparse.ArgumentParser(description='Convert VTT subtitles to human readable transcript')
    parser.add_argument('input', help='Input VTT file path')
    parser.add_argument('-o', '--output', help='Output transcript file path')
    parser.add_argument('--no-timestamps', action='store_true', help='Exclude timestamps from output')
    parser.add_argument('--no-merge', action='store_true', help='Don\'t merge sequential captions into paragraphs')
    
    args = parser.parse_args()
    
    vtt_to_transcript(
        args.input, 
        args.output, 
        include_timestamps=not args.no_timestamps,
        merge_lines=not args.no_merge
    )

if __name__ == "__main__":
    main()
