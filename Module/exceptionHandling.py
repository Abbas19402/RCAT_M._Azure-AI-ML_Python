def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

if __name__ == "__main__":
    try:
        x = int(input("Enter num one: "))
        y = int(input("Enter num two: "))
        print(addition(x,y))
    except Exception:
        print('Not a number!!')