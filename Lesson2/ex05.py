def password_ch(name = '', passw = ''):

    base = {'a':'123','b':'456','c':'789','d':'563'}

    if name not in base:
        print("Incorrect user name", name)
        return

    while base[name] != passw:
        print ("Password for user:", name, "is incorrect\nPlease try again...")
        passw = input("Input password for user: ")

    print ("Password for user:", name, "is correct")

def test2_5():
    password_ch("b", "456")
    password_ch("b", "845")
    password_ch("bb", "456")

test2_5()
