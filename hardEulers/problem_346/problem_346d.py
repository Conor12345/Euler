import itertools

def compute():
    LIMIT = 10 ** 3

    # Collect all generated numbers to eliminate duplicates
    strongrepunits = {1}  # Special case

    # For each possible length of strong repunits (ignoring the trivial length of 2)
    for length in range(3, LIMIT.bit_length() + 1):

        # For each base to evaluate the repunit in, until the value exceeds the limit
        for base in itertools.count(2):

            # Evaluate value = base^(length-1) + base^(length-2) + ... + base^1 + base^0
            # Due to the geometric series, value = (base^length - 1) / (base - 1)
            value = (base ** length - 1) // (base - 1)
            print(value, base, length)
            if value >= LIMIT:
                break
            strongrepunits.add(value)
            print(strongrepunits)
            #x = input("oo")

    # Sum all the numbers generated
    ans = sum(strongrepunits)
    return str(ans)


if __name__ == "__main__":
    print(compute())