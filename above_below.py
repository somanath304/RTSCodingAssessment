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