import sys

def copy_file_append(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'rb') as input_file:
            # Read binary data from the file
            binary_data = input_file.read()

            # Append the binary data to the output file
            with open(output_file_path, 'ab') as output_file:
                output_file.write(binary_data)

        print(f"File successfully appended from {input_file_path} to {output_file_path}")

    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    copy_file_append(input_file_path, output_file_path)

