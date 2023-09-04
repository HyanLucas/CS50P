from random import randint


def main():
    level = get_level()
    numbers = generate_integers(level)
    problems = generate_problems(numbers)
    answers = generate_answers(numbers)
    score = 0
    tries = 3
    question = 0
    while True:
        if tries == 0:
            print(str(problems[question]) + str(answers[question]))
            question += 1
            tries = 3
        else:
            try:
                answer = int(input(problems[question]))
            except ValueError:
                print("EEE")
                tries -= 1
                pass
            if answers[question] == answer:
                question += 1
                score += 1
            else:
                tries -= 1
            if question == 10:
                break
    print("Score: ", score)


def get_level():
    while True:
        try:
            answer = int(input("Level: "))
            if answer != 1 and answer != 2 and answer != 3:
                pass
            else:
                return answer
        except ValueError:
            pass


def generate_integers(level):
    numbers = []
    for _ in range(20):
        if level == 1:
            numbers.append(randint(0, 9))
        elif level == 2:
            numbers.append(randint(10, 99))
        else:
            numbers.append(randint(100, 999))
    return numbers


def generate_problems(numbers):
    problem_list = []
    first_number_problem = numbers[:len(numbers) // 2]
    first_number_problem = [str(number) for number in first_number_problem]
    second_number_problem = numbers[len(numbers) // 2:]
    second_number_problem = [str(number) for number in second_number_problem]
    for i in range(10):
        problem_list.append(
            first_number_problem[i] + " + " + second_number_problem[i] + " = ")
    return problem_list


def generate_answers(numbers):
    first_number_problem = numbers[:len(numbers) // 2]
    second_number_problem = numbers[len(numbers) // 2:]
    answers = []
    for i in range(10):
        answers.append(first_number_problem[i] + second_number_problem[i])
    return answers


if __name__ == "__main__":
    main()
