import os
import re

def break_text(input_filename, output_filename):
    # Get the absolute path of the script's directory
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Form the absolute paths to the input and output files
    input_path = os.path.join(script_directory, input_filename)
    output_path = os.path.join(script_directory, output_filename)

    # Print the paths for verification
    print(f"Input Path: {input_path}")
    print(f"Output Path: {output_path}")

    # Check if the input file exists
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_filename}' not found.")
        return

    with open(input_path, 'r') as input_file:
        text = input_file.read()

    # Use regular expression to split the text into sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)

    # Break the text into lines where every third sentence starts on a new line
    lines = [sentences[i:i+3] for i in range(0, len(sentences), 3)]

    # Join the lines into a formatted text
    formatted_text = '\n'.join([' '.join(line) for line in lines])

    with open(output_path, 'w') as output_file:
        output_file.write(formatted_text)

# Example usage:
input_filename = 'flag.txt'
output_filename = 'output.txt'
break_text(input_filename, output_filename)
