dict1={"candy": 10, "juice": 5, "pen": 50}

def func(arg1, arg2):
    for key, value in dict1.items():
        if arg1 in dict1 and arg2<=dict1[arg1]:
            return True
        else:
            return False
            
func("candy",12)
func("candy",8)