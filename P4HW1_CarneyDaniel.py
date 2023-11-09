# CTI-110
# P4HW1 - Score List
# Daniel Carney
# 2023-11-02

#def main function:
#   make score list
#   ask user for number of scores to enter
#   for each integer n in range (number of scores):
#       ask user for score number n
#       while score less than 0 or score greater than 100:
#           aggressively lash out at user for entering invalid score
#           correct them
#           make them enter it again
#       add score to list
#   print "(newline)------------Results------------"
#   print lowest score
#   if number of scores greater than 1:
#       remove lowest score from scores list
#   print scores list
#   print average of scores
#   call letter grade function
#   print closing string of ---
#
# define letter grade function (grade):
#   if grade is equal to or higher than 90:
#       return 'A'
#   otherwise, if grade is equal to or higher than 80:
#       return 'B'
#   otherwise, if grade is equal to or higher than 70:
#       return 'C'
#   otherwise, if grade is equal to or higher than 60:
#       return 'D'
#   otherwise:
#       return 'F'
#
# run main()

def main():
    scores = []
    num_scores = int(input("How many scores do you want to enter? "))
    for n in range(num_scores):
        next_score = float(input(f"Enter score #{n + 1}: "))
        while (next_score < 0) or (next_score > 100):
            print('\nINVALID Score entered!!!!')
            print('Score should be between 0 and 100')
            next_score = float(input(f"Enter score #{n + 1} again: "))
        scores.append(next_score)

    print('\n'+('-'*12)+'Results'+('-'*12))
    print('Lowest score  :', min(scores))
    if num_scores > 1: #seems helpful to avoid an empty list (plus i can test this with just 1 grade)
        scores.remove(min(scores))
    print('Modified List :', scores)
    average = sum(scores)/len(scores)
    print(f'Scores Average: {average:.2f}')
    print('Grade         :', getLetterGrade(average))
    print('-'*40)

def getLetterGrade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'
        
main()
