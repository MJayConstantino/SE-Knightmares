def print_and_assert(left_side_function, right_side, *args):
    print(f"Test Case with parameters {args}")
    print(f"Expected output: {right_side}")
    print(f"Your output: {left_side_function(*args)}")

    assert left_side_function(*args) == right_side
    print("Success!\n")