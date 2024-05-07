def is_integer(n):
    if isinstance(n, int) and 10 >= n >= 0:
        return True
    elif isinstance(n, float):
        return n.is_integer()
    else:
        return False


def main():
    score_array = []
    total_score = 0

    while True:
        score_input = input("Enter the score (enter 'x' or -1 to stop): ")

        if score_input.lower() == 'x' or score_input == '-1':
            break

        try:
            score = float(score_input)
            if is_integer(score):
                score = int(score)
                score_array.append(score)
                total_score += score
            else:
                print("That isn't a valid score. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if not score_array:
        print("No scores entered.")
        return

    count = len(score_array)
    average = total_score / count
    highest_score = max(score_array)
    lowest_score = min(score_array)

    print(f"Number of scores entered: {count}")
    print(f"The average score is {average}")
    print(f"The highest score is {highest_score}")
    print(f"The lowest score is {lowest_score}")


if __name__ == '__main__':
    main()
