from python.stacksAndQueues.stack_and_queues import Stack


def stack_queue_brackets(brac_str):

    brac_arr = Stack()
    for i in brac_str:
        if i == "(" or i == "[" or i == "{":
            brac_arr.push(i)
        else:
            if i == ")":
                if brac_arr.top.value == "(":
                    brac_arr.pop()
                else:
                    return False
            elif i == "]":
                if brac_arr.top.value == "[":
                    brac_arr.pop()
                else:
                    return False
            elif i == "}":
                if brac_arr.top.value == "{":
                    brac_arr.pop()
                else:
                    return False
    return True

if __name__ == "__main__":
    print(stack_queue_brackets("{(})"))
