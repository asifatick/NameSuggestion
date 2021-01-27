import sys

words = "aWESOME is cODING".split(" ")
print(words)
wa=""
for w in range(len(words),0,-1):
    print(w)
    wa += words[w-1].swapcase() +" "
print(wa)
