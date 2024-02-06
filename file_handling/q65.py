
# # File line order reverse:

# with open('file2.txt','r') as f: # another question 
#     l=f.readlines()
#     with open('file3.txt','w') as file:
#         l.reverse()
#         file.writelines(l)

# # File content reverse:

# with open('file2.txt','r') as f: # correct approach
#     l=f.read()
#     l=l[::-1]
#     print(l)
#     with open('file4.txt','w') as file:
#         file.write(l)


def reverse_and_store(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            with open(output_file, 'w') as file:
                # Read the content of the input file
                l = f.read()

                # Reverse the content
                l = l[::-1]

                # Write the reversed content to the output file
                file.write(l)

                print("Reverse and store successful.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
input_file_name = 'file2.txt'
output_file_name = 'file4.txt'
reverse_and_store(input_file_name, output_file_name)

'''
eejrettahC nawmsihcrA
 ma I
iH
'''