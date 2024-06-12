#!/usr/bin/python3

if __name__ == "__main__":
    """prints all the names defined by the compiled module hidden_4.pyc"""
    import hidden_4

    x = dir(hidden_4)
    for i in x:
        if i[:2] != "__":
            print(i)
