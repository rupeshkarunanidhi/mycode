#!/usr/bin/python3
import random

def main():

    wordbank= ["indentation", "spaces"] 
    tlgstudents= ["Linda", "Michael", "Rupesh", "Samuel", "Zachary"]
    wordbank.append(4)
    print(wordbank)

    #print ("Enter a number from 0 to 14 ...")
    num = random.randint(0,len(tlgstudents))
    print("Randomly chosen number " + str(num))

    student_name = tlgstudents[num]
    print(student_name)

    print(student_name + " always uses " + str(wordbank[-1]) +" " + wordbank[1]+ " to indent.")




if __name__ == "__main__":
    main()
