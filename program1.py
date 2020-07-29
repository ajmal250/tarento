#Suppose you have a sequence consisting of L’s and M’s where L denotes a descending and M denotes an ascending sequence. Take a sequence as an input and decode it to construct a number without repeated digits.
#(For example:
#MMLLMLML -> 125437698
#MMMM -> 12345
#LLLL-> 54321 )
#read word
word=input("Enter the word :")
#sequence counter asequence for ascending and dsequence for descending
asequence=1
dsequence=len(word)+1
#for checking each letter
for letter in word :
    if letter == 'M' :
        print(asequence)
        asequence=asequence+1
    elif letter == 'L' :
        print(dsequence)
        dsequence=dsequence-1
#for printing remaining sequence
print(dsequence)
