'''
Programmer: Raj Shah
Description: Program will output the last palindrome of length 3 in a user entered sentence.
Version: 1.0
Date: July 20, 2022

Algorithm:
create function, palindrome with parameter, s

    for all characters of s,
        if i is not a letter, it will be replaced by " "

    create list, l, which splits s into different words wherever " " occurs

    for all list items of the reverse of l,
        if the length of j is less than 3, continue to the next iteration of the loop

        while the length of j is greater than 3, remove the first and last character of j

        if j is equal to the reverse of j, return j in the function

create infinite loop
    assign s to user input and make it lowercase
    assign variable result to the function, palindrome
    if result has no value, display that there is no palindrome of length 3
    otherwise, display the value of result
    

Pre-condition: a set of string inputs
Post-condition: a set string outputs
'''
def palindrome(s):

    for i in s:
        if not i.isalpha():    # check if i is not a letter and replace it with " "
            s = s.replace(i, " ", 1)
                
    l = s.split(" ")    # create a list with each word as a seperate list item
    
    for j in l[::-1]:    # read each list item from right to left
        if len(j) < 3:   # if the word is less than 3 characters, continue to the next iteration
            continue
        
        while len(j) > 3:   # if the word is more than 3 characters, remove the first and last character
            j = j[1:-1]
            
        if j == j[::-1]:    
            return j
            
while True:
    s = input("Enter a string: ").lower()   
    result = palindrome(s)
    if result == None:
        print("No Palindrome of length 3")   # if the function does not return anything, print the following message
    else:
        print(result)

    
            
            
