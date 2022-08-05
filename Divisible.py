def divisibility(a, b, k):
    divisible = []
    for i in range(a, (b + 1)):
        if i % k == 0:
            divisible.append(i)

    divisible_len = len(divisible)

    return divisible_len


print(divisibility(6, 11, 2))
