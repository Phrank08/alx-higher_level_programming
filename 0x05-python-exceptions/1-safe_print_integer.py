#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(valueAsInt))
        return True
    except Exception as e:
        return False
    finally:
        print()
