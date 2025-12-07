
class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
        print("init function")

    def config(self):
        print('Config: ',self.cpu,self.ram)

    def update(self,cpu):
        self.cpu = cpu
        print('Update: ',self.cpu,self.ram)

    def compare(self,other):
        if self.ram == other.ram:
            return True
        else:
            return False

com1 = computer('AMD','8GB')
com2 = computer('i9','64GB')

#computer.config(com1)
# Or
com1.cpu = 'Ryzen5'
com1.config()

com1.update('Ryzen7')
com2.config()

print(com1.compare(com2))