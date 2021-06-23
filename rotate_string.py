def rotate_string(s,rotateBy):
    # we calculate the displacement
    # required for the string and then
    # slice and join the string
    if len(s)==0:
        return
    x=len(s)-rotateBy
    s=s[x:]+s[0:x]
    print "Rotated String is"
    print s

if __name__=="__main__":
    s = input("Enter the string\n")
    rotateBy = input("Enter a rotateby value\n")
    rotate_string(s,rotateBy)