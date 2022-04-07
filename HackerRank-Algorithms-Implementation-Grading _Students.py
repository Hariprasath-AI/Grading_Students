def gradingStudents(grades):
    # Using for loop to check n numbers of elements/grades to process
    for i in range(0, len(grades)):
        # Storing a element in the variable 'val'
        # Storing a reminder value of dividing 'val' by 5 in the variable 'rem'
        val = grades[i]
        rem = val % 5

        # If our reminder value is greater than or equal to 3 and less than or equal to 5.
        # We have change the grades to next multiple of 5. Only when the grades are greater than or equal to 40 and less than or equal to 100 
        if rem >= 3 and rem <= 5:
            val = val - rem + 5
            if val >= 40 and val <= 100: 
                grades[i] = val
                
    # To print all the grades in new line    
    print(*grades, sep = "\n")

if __name__ == "__main__":
    # Get value n value from user i.e., number of items/elements
    n = int(input())

    # Create an empty array
    grades = []
    
    # Get n number of elements from the user and store it in the array 'grades'
    for i in range(0, n):
        val = int(input())
        grades.append(val)
    
    # Calling the 'gradingStudents' function and passing 'grades' as arguments to get the output
    gradingStudents(grades)