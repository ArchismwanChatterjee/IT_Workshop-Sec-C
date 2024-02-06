def copy(input_file, output_file):
    try:
        with open(input_file, 'rb') as infile:
            with open(output_file, 'wb') as outfile:
                first_100_bytes = infile.read(100)                
                outfile.write(first_100_bytes)
                print("Copy successful.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
input_file_name = 'input_binary_file.bin'
output_file_name = 'output_binary_file.bin'
copy(input_file_name, output_file_name)
