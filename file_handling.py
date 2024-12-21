def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def main():
    try:
        input_filename = input("Enter the filename to read: ")
        # Read the content from the file
        content = read_file(input_filename)
        
        # Modify the content (convert to uppercase as an example)
        modified_content = content.upper()
        
        # Write the modified content to a new file
        output_filename = "modified_" + input_filename
        write_file(output_filename, modified_content)
        
        print(f"Modified content has been written to {output_filename}")
        
    except FileNotFoundError:
        print(f"The file '{input_filename}' does not exist.")
    except IOError:
        print(f"An error occurred while reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
