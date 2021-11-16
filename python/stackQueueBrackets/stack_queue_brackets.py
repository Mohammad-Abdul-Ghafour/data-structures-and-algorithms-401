
def stack_queue_brackets(brac_str):

    brac_arr = []
    for i in brac_str:
        if i == "(" or i == "[" or i == "{":
            brac_arr.append(i)
        else:
            if i == ")":
                if brac_arr[-1] == "(":
                    brac_arr.pop()
                else:
                    return False
            elif i == "]":
                if brac_arr[-1] == "[":
                    brac_arr.pop()
                else:
                    return False
            elif i == "}":
                if brac_arr[-1] == "{":
                    brac_arr.pop()
                else:
                    return False
    return True

if __name__ == "__main__":
    print(stack_queue_brackets("{(})"))
