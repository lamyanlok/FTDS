def divisions(n,divisor):
    number_of_times = 0
    while True:
        if n % divisor == 0:
            number_of_times +=1
            n = n / divisor
        else:
            break

    return number_of_times

n = int(input("Input the first number."))
divisor = int(input("Input the divisor number."))
print(f"n {n}, divisor {divisor}")
out = divisions(n, divisor)
print(f"The number {n} can be divided by {divisor} by {out} times")