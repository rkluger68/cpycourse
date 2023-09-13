def gen_even():
    """Generate even natural numbers, undefinitely.
    """
    i = 1
    while True:
        if i % 2 == 0:
            yield i
        i += 1


def gen_uneven():
    """Generate even natural numbers, undefinitely.
    """
    i = 1
    while True:
        if i % 2 != 0:
            yield i
        i += 1


def gen_even_lim(upper_limit=-1):
    """Generate even natural numbers, up to max upper limit, or undefinitely if
    max < 1.
    """
    for i in gen_even():
        if i > upper_limit:
            break
        yield i


def gen_uneven_lim(upper_limit=-1):
    """Generate uneven natural numbers, up to max upper limit, or undefinitely
    if max < 1.
    """
    for i in gen_uneven():
        if i > upper_limit:
            break
        yield i


def gen_numbers(mode="even"):
    """Generate even or uneven natural numbers, undefinitely.
    """
    if mode == "even":
        return gen_even()
    elif mode == "uneven":
        return gen_uneven()
    else:
        raise ValueError(f"mode '{mode}' is not supported, use {even, uneven}")


def gen_numbers_lim(mode="even", upper_limit=-1):
    """Generate even or uneven natural numbers up to max upper limit, or
    undefinitely if max < 1.
    """
    if mode == "even":
        return gen_even_lim(upper_limit)
    elif mode == "uneven":
        return gen_uneven_lim(upper_limit)
    else:
        raise ValueError(f"mode '{mode}' is not supported, use {even, uneven}")


def main():
    # Run unlimited generator, but break out after a limit (checked outside of
    # the generator). In the REPL you'd interrupt the generator using Ctrl-c.
    generator = gen_even
    print()
    print(f"*** Generator: {generator.__name__}")
    print(f"({generator.__doc__.strip()})")
    for val in generator():
        if val > 10:
            print("...interrupting (use Ctrl-c when running in REPL)")
            break
        print(f"even: {val}")

    # Run even/uneven-switchable unlimited generator in "even" mode, but break
    # out after a limit (checked outside of the generator). In the REPL you'd
    # interrupt the generator using Ctrl-c.
    generator = gen_numbers
    print()
    mode = "even"
    print(f"*** Generator: {generator.__name__}(mode='{mode}')")
    print(f"({generator.__doc__.strip()})")
    for val in generator(mode):
        if val > 10:
            print("...interrupting (use Ctrl-c when running in REPL)")
            break
        print(f"even: {val}")

    # Run even/uneven-switchable unlimited generator in "even" mode, but break
    # out after a limit.
    print()
    mode = "uneven"
    print(f"*** Generator: {generator.__name__}(mode='{mode}')")
    print(f"({generator.__doc__.strip()})")
    for val in generator(mode):
        if val > 10:
            print("...interrupting (use Ctrl-c when running in REPL)")
            break
        print(f"uneven: {val}")


    # Run even/uneven-switchable limited generator in "even" mode with an upper
    # limit of 5.
    generator = gen_numbers_lim
    print()
    mode = "even"
    limit = 5
    print(f"*** Generator: {generator.__name__}(mode='{mode}', limit={limit})")
    print(f"({generator.__doc__.strip()})")
    for val in generator(mode=mode, upper_limit=limit):
        print(f"even: {val}")

    # Run even/uneven-switchable limited generator in "uneven" mode with an
    # upper limit of 5.
    print()
    mode = "uneven"
    limit = 5
    print(f"*** Generator: {generator.__name__}(mode='{mode}', limit={limit})")
    print(f"({generator.__doc__.strip()})")
    for val in generator(mode=mode, upper_limit=limit):
        print(f"uneven: {val}")


if __name__ == "__main__":
    # If this program is invoked as the main program, as opposed to being
    # imported, run the main function.
    main()
