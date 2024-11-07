class Employee:
    # private variable
    def __init__(self, id):
        self.__id = id
    # getter method
    def get_id(self):
        return self.__id

# emp = Employee(1)
# print(emp.get_id())
