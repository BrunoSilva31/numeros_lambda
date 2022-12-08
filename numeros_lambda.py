numeros = [num for num in range(1, 11)]

result = list(
    map(
        lambda n: n * 10 if n % 2 == 0 else round(n / 3, 2), numeros
    )
)

print(result)
