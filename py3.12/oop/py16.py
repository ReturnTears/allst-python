class Duck:
    def walk(self):
        print('this duck is walking.')

class Person:
    def walk(self):
        print('this person is walking.')

def start_walking(object):
    object.walk()

d = Duck()
p = Person()
start_walking(d)
start_walking(p)

