def kovid(x, y, z):
    print("My name is " + x)
    if y == "M" or y == "m":
        print("My gender is Male")
    elif y == "F" or y == "f":
        print("My gender is female!")
    else:
        print("My gender is " + y)
    print("My age is ", z)


kovid("Coder Kovid", "Male", 14)
