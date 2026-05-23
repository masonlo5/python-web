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

def register_command(name, description):
    print(f"[登記] command / {name}: {description}")

    def decorator(func):
        def wrapper():
            print(f"[執行] command / {name}")
            func()

        return wrapper
    
    return decorator


@register_command(name="hello", description="say hello")
def hello_command():
    print("hello, I am a command!")

hello_command()
print("-------------------------------")