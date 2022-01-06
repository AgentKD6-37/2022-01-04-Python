
def main():
    for i in range(4):
        print(i)

    for x in range(10):
        print(x, end=" ")

    for z in range(10):
        print(z)

    foo = open("ourfile.txt", "w")
    fruitbowl = ["apple", "pear", "grapes"]

    for fruit in fruitbowl:
        print(fruit, file=foo)

    foo.close()

main()