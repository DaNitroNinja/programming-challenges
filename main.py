# -------------------------------------------------------------------------------
# Name:        Programming Challenge 1
# Purpose:
#
# Author:      Rishi Patwardhan
#
# Created:     24/04/2024
# Copyright:   (c) r0patwardhan 2024
# Licence:     <your licence>
# -------------------------------------------------------------------------------


def isInteger(n):
    if isinstance(n, int) and n <= 10 and n >= 0:
        return True
    elif isinstance(n, float):
        return n.is_integer()
    else:
        return False


def main():
    scoreArray = []
    totalScore = 0
    count = 0
    while count < 10:
        score = float(input("Enter the score: "))

        if isInteger(score):
            score = int(score)
            scoreArray.append(score)
            count += 1
        else:
            print("That isn't a valid score. Please try again.")

    for i in range(0, 10):
        totalScore += scoreArray[i]

    average = totalScore / 10

    print(f"The average score is {str(average)}")


if __name__ == '__main__':
    main()