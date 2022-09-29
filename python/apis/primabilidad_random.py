import random


try:

    a = (random.randint(2, 100000000))
    b = a % 2 and a % 3 and a % 5 and a % 7

    def primos():
        if b != 0:
            print(f"El número {a} SI un número primo")

        else:
            print(f"El número {a} NO es Primo")

    if __name__ == "__main__":
        primos()


except Exception as e:
    print(e)
             