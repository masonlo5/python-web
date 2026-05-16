def say_hello():
    print("Hello!")



def run_with_announce(func):
    print("Running the function...")
    func()
    print("Done!")


print("Calling say_hello directly:")
say_hello()

print("\nCalling say_hello with run_with_announce:")
say_hello()


print()
print("Calling say_hello with run_with_announce:")
run_with_announce(say_hello)

print("-------------------------------")


def gift_wrap(func):
    def wrapper():
        print("Wrapping the gift...")
        func()
        print("Gift wrapped!")

    return wrapper


def say_hello():
    print("Hello!")


say_hello = gift_wrap(say_hello)

say_hello()