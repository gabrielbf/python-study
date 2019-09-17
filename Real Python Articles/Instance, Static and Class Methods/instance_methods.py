class Test:
    def __init__(self):
        self.campo = 1

    def method(self):
        print('Entrou no método method da instância ', self)

    def outro():
        print('Entrou no método outro')


print('Test.outro()')
Test.outro()
print('obj = Test()')
print('obj.method()')
obj = Test()
obj.method()
print('Test.method(obj)')
Test.method(obj)
print('Test.method()')
Test.method()
