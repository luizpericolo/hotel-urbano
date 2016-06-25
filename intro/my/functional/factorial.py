def factorial(n):
    """
        returns n!
    """

    def fact_rec(n, acc):
        if n <= 1:
            return acc

        return fact_rec(n - 1, n * acc)

    return fact_rec(n, 1)


if __name__ == "__main__":
    assert factorial(5) == 120
    print("Asserted factorial(5) is 120")
