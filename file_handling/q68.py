def copy_without_comments(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            with open(output_file, 'w') as outfile:
                lines = infile.readlines()

                for line in lines:
                    if not line.strip().startswith('#'):
                        outfile.write(line)
                
                print("Copy without comments successful.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

input_file_name = 'input_script.py'
output_file_name = 'output_script.py'
copy_without_comments(input_file_name, output_file_name)
