def copy_and_convert_to_uppercase(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            with open(output_file, 'w') as outfile:
                # Read the content of the input file
                content = infile.read()
                uppercase_content = content.upper()                
                outfile.write(uppercase_content)
                print("Conversion and copy successful.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
input_file_name = 'input_text_file.txt'
output_file_name = 'output_text_file.txt'
copy_and_convert_to_uppercase(input_file_name, output_file_name)
