class Cham(object):

    def __init__(self):
        self.counter = 1

    def write(self):
        self.counter += 1

    def add(self):
        write(self)


cham = Cham()


cham.write()

a = [1,2,3]
print(a[-1])
a.append(4)
print(a[-1])
