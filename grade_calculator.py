stu_grade = int(input("What percentage of questions did you answer correctly? "))


if stu_grade >= 90:
    print(str(stu_grade) + "% correct means you got an A!")
else:
    if stu_grade >= 80:
        print(str(stu_grade) + "% correct means you got an B!")
    else:
        if stu_grade >= 70:
            print(str(stu_grade) + "% correct means you got an C...")
        else:
            if stu_grade >= 60:
                print(str(stu_grade) + "% correct means you got an D...not good...")
            else:
                print("Your failed!")
        