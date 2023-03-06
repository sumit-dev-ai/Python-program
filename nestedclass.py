class outer:
    def __init__(self):
        print("outer class")
    def display():
        print("this is display method")
    class inner(object):
        def __init__(self):
            print('inner class')
        def show(self):
            print('this is show method')
ob=outer()
inn=ob.inner()
inn.show()
ob.show()