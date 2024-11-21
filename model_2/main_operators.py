for number in range(3, 21):
    answer = ""

    divisors = []
    for divisor in range(3, number + 1):
        if number % divisor == 0:
            divisors.append(divisor)

    for one_number in range(1, number // 2 + 1):
        for divisor in divisors:
            two_number = divisor - one_number
            if one_number != two_number and two_number > 0 and one_number < two_number:
                answer += f"{one_number}{two_number} "

    print(f"{number}:", answer)
