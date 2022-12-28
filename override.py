
class A:

    def Method1(self):
        print('Hello from method 1')

class B(A):

    def Method1(self):
        print('Hello from updated method 1')



O = B()

O.Method1()