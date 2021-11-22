def oops():
    raise IndexError()

def main():
    try:
        oops()
    except IndexError:
        print("Got Index Error!")
main()


