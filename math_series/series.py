
def fibonacciSeries():
    N = int(input("Number of elements in Fibonacci Series, N, (N>=2) : "))

    fib_list = [0, 1]

    if N > 2:
    for i in range(2, N):
        fib_num = fib_list[i-1] + fib_list[i-2]
        # append the element to the series
    fib_list.append(fib_num)

    print(fib_list)
