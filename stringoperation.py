
#function for counting the number of vowels
def countOfVowels(string):
    """asciival=[]
    for i in range(98,123,1):
        if(i==101 or i==105 or i==111 or i==117):
            pass
        else:
            asciival.append(i)
    print(asciival)"""
    print ("vowels are: ",end=" "),
    global cnt
    for vowels in "aeiou":
        #checking the vowels in string
        if vowels in string:
            print (vowels,end=" ")
            cnt+=1  #incrementing the count when vowels is equal to string
    print ("\ncount of vowels :"+str(cnt))

def countOfConsonants(string):
    print("Consonants are :",end=" ")
    global cnt
    cnt=0
    for consonants in "bcdfghjklmnpqrstvwxyz":
        if consonants in string:
             print (consonants,end=" ")
             cnt+=1
    print ("\ncount of Consonants :"+str(cnt))

def reverseOfString(string):
    global strlen
    reversedString="" #variable to copy the new reversed string
    i=strlen
    while i>0:    #starting from the last index
        i-=1
        #copying the string from the last index to the 0th index in reversedString
        reversedString+=string[i]
    print("reversed String: "+reversedString)

def swapCase(string):
    global strlen
    temp=list(string)   #converting string into a list and storing in temporary variable
    alternate_case=[] #copying the swapped case string into a new list
    for i in range(0,strlen,1):
        if(i%2 == 0):#change it to (i%2)!=0) to start with 1st index instead of 0th index
            #ORD is for getting the ascii value of value stored at i'th index in temp variable
            if(ord(temp[i])==32):
                #check for spaces in the string to ignore while swaping the cases
                pass
            elif(ord(temp[i])>=96 and ord(temp[i])<=122):
                alternate_case.append(chr(ord(temp[i])-32))
            elif(ord(temp[i])>=65 and ord(temp[i])<=90):
                #CHR is for converting the ascii code to character
                alternate_case.append(chr(ord(temp[i])+32))
            else:
                alternate_case.append(temp[i])
        else:
            alternate_case.append(temp[i])
    i=0
    print("Swap Case: ",end=" ")
    for i in alternate_case:
        print(i,end="")
    print("")
#main code block
strlen=0
cnt=0
string=input("Enter a string: ")
print("")
print("You Entered: "+string)
for i in string:
    strlen+=1;
if(strlen<21):
    countOfVowels(string)
    countOfConsonants(string)
    reverseOfString(string)
    swapCase(string)
else:
    print("error in input(string length is more than 20)")
