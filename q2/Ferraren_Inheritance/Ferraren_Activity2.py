#Single Inheritance
class Parent:
    def __init__(self, name):
        self.name = name

    # Getter method
    def get_name(self):
        return self.name

    # Setter method
    def set_name(self, name):
        self.name = name

    def func1(self):
        print("This function is in the parent class.")

class Child(Parent):
    def func2(self):
        print("This function is in the child class.")
        print("My name is", self.name)


object1 = Child("Prince")
object2 = Child("Maria")

object1.func1()
object1.func2()

object1.set_name("John")

print("Updated name:", object1.get_name())

object2.func2()

#Multilevel Inheritance
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

    def get_grandfathername(self):
        return self.grandfathername

    def set_grandfathername(self, name):
        self.grandfathername = name


class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        super().__init__(grandfathername)
        self.fathername = fathername

    def get_fathername(self):
        return self.fathername

    def set_fathername(self, name):
        self.fathername = name


class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        super().__init__(fathername, grandfathername)
        self.sonname = sonname

    def get_sonname(self):
        return self.sonname

    def set_sonname(self, name):
        self.sonname = name

    def print_name(self):
        print("Grandfather name:", self.grandfathername)
        print("Father name:", self.fathername)
        print("Son name:", self.sonname)


s1 = Son("Prince", "Rampal", "Lal Mani")
s2 = Son("Anna", "Robert", "James")

s1.print_name()

s1.set_sonname("Daniel")
s1.set_fathername("Michael")
s1.set_grandfathername("William")

print("\nUpdated names:")
s1.print_name()

print("\nSecond object:")
s2.print_name()

#Hierarchical Inheritance
class Parent:
    def __init__(self, familyname):
        self.familyname = familyname

    def get_familyname(self):
        return self.familyname

    def set_familyname(self, name):
        self.familyname = name

    def func1(self):
        print("This function is in the parent class.")

class Child1(Parent):
    def __init__(self, name, familyname):
        super().__init__(familyname)
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def func2(self):
        print("Child 1:", self.name)
        print("Family name:", self.familyname)

class Child2(Parent):
    def __init__(self, name, familyname):
        super().__init__(familyname)
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def func3(self):
        print("Child 2:", self.name)
        print("Family name:", self.familyname)


object1 = Child1("Prince", "Santos")
object2 = Child2("Maria", "Santos")
object3 = Child1("Daniel", "Reyes")

object1.func1()
object1.func2()

object2.func1()
object2.func3()

object1.set_name("John")
object1.set_familyname("Cruz")

print("\nAfter updating object1:")
object1.func2()

print("\nAdditional object:")
object3.func2()