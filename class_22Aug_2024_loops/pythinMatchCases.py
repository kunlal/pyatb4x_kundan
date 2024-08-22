
#python 3.10 version added match case as switch case

inp = input("Please enter a value\n")

match inp:
    case "A":
        print("A")
    case "B":
        print("B")
    case "C":
        print("C")
    case "D":
        print("D")
    case _:
        print("Default")

