
def fun(input_file):
    try:
        with open(input_file,'r') as f:
            sentence=f.read()
            word=sentence.split()
            num=len(word)
            print("The file contains ",num, "words")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

fun('Countwords.txt')

'''
The file contains  12 words
'''