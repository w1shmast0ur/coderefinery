def say_something(something):
    if something:
        something.reverse()
        print(" ".join(something))
    else:
        print("Hello World!")
