class PrivateDemo:
    def __init__(self):
        self.__privateVar = 18

    def __private_mth(self):
        return "this ia a private method."

d = PrivateDemo()
# print(d.__privateVar) # AttributeError:
# print(d.__private_mth()) # AttributeError:

print(d._PrivateDemo__privateVar)
print(d._PrivateDemo__private_mth())
