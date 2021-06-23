# 1 Print the number of integers in an array that are above the given input and the number that are below, 
# e.g. for the array [1, 5, 2, 1, 10] with input 6, print “above: 1, below: 4”.

def above_below(arr,num):
    if len(arr)==0:
        print("array size is 0")
        return
    above=0
    below=0
    # iterating over the array and using a conditional block and check the above and below count
    for i in arr:
        if i>num:
            above+=1
        else:
            below+=1
    print("above :",above)
    print("below :",below)

if __name__=="__main__":

    arr = input("Enter your array\n")
    num = input(" Enter a value to be compared\n")
    above_below(arr,num)
