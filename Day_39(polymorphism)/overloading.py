def overloading():
    class A:
        def show(self):
            print("Welcome again Shubham 😊")
        def show(self,firstname="Shubham"):
            print("Welcome", firstname)
        def show(self, firstname,lastname="Jana"):
            print("Welcome",firstname,lastname)
    obj1 = A()
    A.show()
    # A.show("Shubham")
    # A.show("Shubham","Jana")
overloading()