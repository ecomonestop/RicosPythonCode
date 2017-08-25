import socket


class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        """__call__ makes instances of this class callable like a function
        e.g.
        resolver = Resolver()
        resolver("myhost")  -- note this invokes the __call__ method
        The instructor said its good for caching, didnt follow on that exactly."""
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

def conditional_expression_example(my_bool):
    """Below is an example of conditional expression
      It reads better than if else blocks"""
    return True if my_bool == "yes" else False

def example_lambda_func():
    """Example of using lambda functions in python"""
    names = ["Rico Romero", "Celine Zhang", "Brian Lawson", "Shelly Murriel", "Tom Abe"]
    sort_by_last_name = sorted(names, key=lambda name: name.split()[-1]);
    for name in sort_by_last_name:
        print(name)

def example_extended_formal_arg_syntax(*args, **kwargs):
    """args is a tuple and kwargs is a dictionary,
    ordering of these arguments matter when defining the function.  You can google search all rules"""
    print(type(args))
    print(type(kwargs))

def example_extended_call_syntax_iter(name, age, *args):
    """You can pass in a itterable like a tuple that gets unpacked to name and age, and the rest in *args
    t = ("Rico", 27, "he is cool", "he is married")
    example_extended_call_sytax_iter(*t)"""
    print(name)
    print(age)
    print(args)

def example_extended_call_syntax_map(name, phone, **kwargs):
    """You can pass in a map like a dectionary that gets unpacked to name and phone, and the rest in *args
       d = {name: "Rico", phone: 313, isCool: True}
       example_extended_call_syntax_map(**d)"""
    print(name)
    print(phone)
    print(kwargs)

if __name__ == "__main__":
    example_lambda_func()
    t = ("Rico", 27, "he is cool", "he is married")
    example_extended_call_syntax_iter(*t)
    d = {"name": "Rico", "phone": 313, "isCool":True }
    example_extended_call_syntax_map(**d)