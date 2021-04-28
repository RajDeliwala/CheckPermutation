'''
Cracking the coding interview
Chapter 1 - Arrays and Strings page 90
Check Permutation
Problem Statement: Given two strings, write a method to decide if one is a permutation of the other
example: "ABC"s permutations will be "ABC", "ACB", "BAC", "BCA", "CBA", "CAB"

Constraits or Questions you need to ask:
- Is this case senstitive?
- What about white spaces in the strings?

Solution notes:
-You can check if the 2 strings on the same length because if they're not then 
it is not possible for them to be permutations of each other
-We don't need every possible permutation, we just need to set both into a similar sorted order
and if they equal then they are permutations
'''
#Imported package to deal with permutations in python
from itertools import permutations


#Solution which is O(N^2) because we are looping 2x for each string
def check_permutation(string, string2):
    #Creating permutations of both
    a=permutations(string)
    b=permutations(string2)

    #looping through the list 
    for x in list(a):
        for y in list(b):
            if ("".join(x) == "".join(y)):
                return True
            else:
                return False


#print(check_permutation("ASHU","ASHU") == True)
#print(check_permutation("ASHU","ASH") == False)
#print(check_permutation("God","dog") == False)

#Lets try a solution where we go for a O(N) approch
#Check if both strings are the same size, if not fail
#Then sort both strings alphabetically and they should equal each other if not fail
def check_permutationSolution(string1, string2):
    if (len(string1) != len(string2)):
        return False

    else:
        a = sorted(string1)
        b = sorted(string2)

        if (a == b):
            return True
        else: 
            return False

print(check_permutationSolution("dog","god") == True)
print(check_permutationSolution("DOG","godd") == False)
print(check_permutationSolution("Bill ","Billy") == False)
                  

