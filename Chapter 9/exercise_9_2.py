"""
. In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that
does not contain the letter “e.” Since “e” is the most common letter in English, that’s not easy to
do.
In fact, it is difficult to construct a solitary thought without using that most common symbol. It is
slow going at first, but with caution and hours of training you can gradually gain facility.
All right, I’ll stop now.
Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in
it.
Modify your program from the previous section to print only the words that have no “e” and compute the percentage of the words in the list have no “e.”

"""

fin = open("./Exercise1.py")

def has_no_e():
    total_count = 0
    no_e_count = 0

    for line in fin:
        word = line.strip()
        if "e" not in word:
            no_e_count += 1
            print(word)
        total_count += 1

    no_e_percentage = float(no_e_count) / total_count * 100
    return no_e_percentage
print(has_no_e())
