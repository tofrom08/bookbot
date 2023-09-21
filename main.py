
def words_count(file_name):
    with open(file_name) as f:
        file_contents = f.read()
        words = 0
        lines1 = file_contents.split()
        words += len(lines1)
        print (f"{words} words found in the document")
        


words_count("books/frankenstein.txt")


def letters_count(file_name):
    with open(file_name) as f:
        file_contents = f.read()
        Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in Alphabet:
            print (f"The {i} character was found {str(file_contents.count(i))} times")
            

letters_count("books/frankenstein.txt")
