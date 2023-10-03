word1 = input("Please input word 1")
word2 = input("Please input word 2")

word3 = word1[0:2] + word2[2:]
word4 = word2[0:2] + word1[2:]
print(word4,word3,sep=" ")
