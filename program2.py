#- Accept a String input
#- Print the count of words in the String. Space is assumed to be the separator between words
#- Print all numbers that are present in the String and also if they are odd or even. Numbers which are together should be counted as one number.
#
#Eg. If the String input is
#The boy had 2 apples, 23 oranges and 222 grapes.
#then the output should be as below
#Total words - 10
#Even numbers - 2,222
#Odd numbers - 23
word=input('enter string : ')
word=word+' '
sp=0
i=0
count=0
even='Even numbers - '
odd='Odd numbers - '
while i < len(word):
    letter=word[i]
    if letter == ' ':
        count=count+1
        nw=word[sp:i]
        sp=i+1
        if nw.isnumeric():
            n=int(nw)
            if n%2 == 0:
                even=even+str(n)+','
            else:
                odd=odd+str(n)+','

    i=i+1
#        count=count+1
print('Total words - ',count)
print(even)
print(odd)
#for letter in word :
#    try:
#        if int(letter-1)%2 == 0:
#            print
