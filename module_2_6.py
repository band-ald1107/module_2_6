def generate_password(n):
    password = ""
    for i in range(1, 21):
        for j in range(i + 1, 21):
            pair_sum = i + j

            if n % pair_sum == 0:
                password += f"{i}{j}"

    return password


n = 9
result = generate_password(n)
print(result)
