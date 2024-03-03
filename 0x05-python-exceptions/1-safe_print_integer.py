#!/usr/bin/pyhton3
def safe_print_integer(value):
    try:
        valueAsInt = int(value)
            print("{:d}".format(valueAsInt))
            return True
    except Exception as e:
        print(f"Error: {e}")
        return False
    
    finally:
        print()
