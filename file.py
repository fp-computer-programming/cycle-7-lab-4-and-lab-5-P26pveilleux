
#Create a Python file named lab_7-4.py

#*** You must write a comment for every chunk of code you write from now on along with your author tag***

#Copy your lab 7-2 code into the file
#Add 4 test cases to the end of the file, with comments
#Ensure your lab runs accurately

def find_sum(num1,num2):
    num_sum = num1 +num2
    return num_sum

print(find_sum(111,222) == 33)
print(find_sum(1,7) == 3)
print(find_sum(1.5,1.5) == 3)
print(find_sum(1000,1000) == 2000)


#________________________________________________________________________________

#Create a Python file named lab_7-5.py


#Copy the code from your labs 6-5 through 6-8
#Turn each of the programs into a function
#Add 4 test cases to the functions
#Ensure your code runs accurately


def hilo(list):
    i = 1
    re = [list[0],list[0]]
    while i < len(list):
        if list[i] > re[0]:
            re[0] = list[0]
        if list[i] < re[1]:
            re[1] = list[1]
        i += 1
    return re if len(list) >= 2 else "error"

print(hilo([1,2,3,4,5]) == [5,1])
print(hilo([1]) == "error")
print(hilo([5,6,7,8]) == [8,5])
print(hilo([2,7,6,3]) == [7,2])
                        
