def recursive_nth_fibo(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)


def main():
    n = 6
    vysledek = recursive_nth_fibo(n)
    print(vysledek)

if __name__ == "__main__":
    main()
