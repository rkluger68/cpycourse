# object_introspection.property

import json
import sys


def ask_user(prompt='Your input please: ', types=(int, float, json.loads)):
    """Get user input and convert to target data type with the 1st usable
    `types` converter.

    Returns the converted data or the string input if no converter is able to
    convert the text input data.
    """
    text = input(prompt)

    # str is the default.
    value = text
    for typ in types:
        try:
            value = typ(text)
            break
        except Exception:
            # Try the next type...
            pass

    print(f"value = {value} [{type(value)}]")
    return value


def get_object_methods(obj):
    """Return a list of all `obj` methods that do not start with a leading
    underscore.
    """
    methods = [
        value for name in dir(obj)
        if not name.startswith('_') and callable(value := getattr(obj, name))
    ]
    return methods


def select_method(methods):

    print("==========================================")
    print("Please select the method you want to call:")
    for (i, method) in enumerate(methods):
        print(f" {i+1} - {method.__name__}")
    print("==========================================")
    while (input_text := input("Please enter your choice: ")):
        try:
            choice = int(input_text)
            break
        except ValueError:
            continue

    selected_method = methods[choice-1]
    print(f"You selected '{selected_method.__name__}'")
    return selected_method


def run_method(method):
    result = method()
    print("Result:")
    print(
        f"  ({method.__self__}).{method.__name__}() --> "
        f"{result} [{type(result)}]"
    )
    print(f"  value = {method.__self__}")


def main():
    obj = ask_user()
    methods = get_object_methods(obj)
    selected_method = select_method(methods)
    try:
        run_method(selected_method)
    except Exception as exc:
        print(f"Oops! Ran into exception: {exc}.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
