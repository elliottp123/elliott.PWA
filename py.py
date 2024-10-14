import sys

def convert_quotes(input_text):
    return input_text.replace('"', "'")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Read from file if filename is provided as argument
        filename = sys.argv[1]
        try:
            with open(filename, 'r') as file:
                input_text = file.read()
            output_text = convert_quotes(input_text)
            print(output_text)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        # Read from standard input if no filename is provided
        print("Enter your text (press Ctrl+D on Unix or Ctrl+Z on Windows to finish):")
        input_text = sys.stdin.read()
        output_text = convert_quotes(input_text)
        print("\nConverted text:")
        print(output_text)