#Reverse Words in a Given String
def reverse_words(string):
    words = string.split('.')
    reversed_string = '.'.join(words[::-1])
    return reversed_string

def main():
    S = "i.like.this.program.very.much"
    output = reverse_words(S)
    print(output) 

main()