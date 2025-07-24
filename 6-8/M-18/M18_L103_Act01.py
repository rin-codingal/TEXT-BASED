#Take input for the student that he can attend the exam or not
medical_cause = input("did you have a medical cause Y or N: ")

#Take input of the attendance
atten = int(input("enter the attendance of the student: "))

if medical_cause.upper() == 'Y': #checking the condition 1
    print ("You are allowed, because you have medical condition")
else :
    if atten >= 75:  #checking the condition 2
        print ("Allowed. Because you don't have medical condition and your attendance is more than 75%")
    else :
        print ("Not allowed. Because you don't have medical condition and your attendance is less than 75%")