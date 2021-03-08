 # Finding longest word in sentence 
def longestWordLength(string): 
      
    length = 0
      
    for word in string.split(): 
        if(len(word) > length): 
            length = len(word) 
            str1 = word
      
    print(f"Longest word: {str1}\nLength: {length}\n")
  
# counting frequency of characters
def frequency_count(str1):

    all_freq = {} 
  
    for i in str1: 
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1
  
    print ("\nCount of all characters is :\n "+  str(all_freq)) 

#checking if the given string is palindrome or not

def isPalindrome(str1):
    check = str1 == str1[::-1]
    if check:
        print("Yes")
    else:
        print("No")

#displaying index of first appearance of substring
def findSubstring(str1):

    substring = input("\nEnter substring: ")
    index = str1.find(substring)
    print(f"{substring} appeared after position {index}")

# Occurence of each word in a given string
def word_count(str1):
    counts = dict()
    words = str1.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    print("word count:\n",counts)


def switch(str1):
    print("\nWhat function would you like to perform\n1.Display word with longest length\n2.Frequency of characters\n3.Palindrome check\n4.index of first appearance of substring\n5.count of occurance of each word in a given string")

    ch = int(input("\nEnter corresponding number: "))
    if ch == 1:
        longestWordLength(str1)
    elif ch == 2:
        frequency_count(str1)
    elif ch == 3:
        isPalindrome(str1)
    elif ch == 4:
        findSubstring(str1)
    elif ch == 5:
        word_count(str1)
    else :
        print("incorrect number")
    
        
str1 = input("Enter string:\n")
switch(str1)
c= input("Would you like to continue?")
while c == "y" or c == "Y":
    switch(str1)
    c = input("Would you like to continue?")


