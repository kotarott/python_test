a = 1
b = 2
c = 3

param_list = [1, 2, 3, 4, 5]

# print(param_list)

def test():
    for i in param_list:
        if i % 2 == 0:
            print(f"偶数:{i}")
        elif i % 2 != 0:
            print(f"奇数:{i}")

if __name__ == "__main__":
    test()