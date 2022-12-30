# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anderson Wayne Loan 
# Section: 574
# Assignment: 7-2
# Date: 1 10 22
#

word = input("Enter some text:\n")#takes in input
print(f'In leet speak, "{word}" is:',end = ' ')
word.lower()
leetSpeak = {'a':'4','e':'3','o':'0','s':'5','t':'7'}#a,e,o,s,t

for i in range(len(word)):#we're gonna run through the entire input and check for individual letters
        if word[i] == 'a':
            word = word.replace(word[i],leetSpeak['a'])#if the letter matches up we swap it with a number assigned
        elif word[i] == 'e':
            word = word.replace(word[i],leetSpeak['e'])
        elif word[i] == 'o':
            word = word.replace(word[i],leetSpeak['o'])
        elif word[i] == 's':
            word = word.replace(word[i],leetSpeak['s'])
        elif word[i] == 't':
            word = word.replace(word[i],leetSpeak['t'])
print(word,end = ' ')

