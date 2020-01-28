def capital(S=""):
    if not S:
        S = input("Input first and last name: ")
    if not 0 < len(S) < 1000:
        print("Error: length of line must be > 0 and < 1000.")
        return
    elif not S.replace(' ','').isalnum():
        print("Error! The string consists of alphanumeric characters and spaces.")
        return

    if not S.istitle():
        S_list = []
        for part in S.split():
            S_list.append(part.capitalize())
        S = ' '.join(S_list)

    print(S)

def test1_1():
    capital('123abc 345dfg')
    capital('abc 345dfg')
    capital('abc dfg')
    capital('Abc dfg123')
#     capital()

test1_1()
