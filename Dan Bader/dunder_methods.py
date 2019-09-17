"""
https://dbader.org/blog/python-dunder-methods
"""
from functools import total_ordering


@total_ordering
class Account:
    # Object initialization: __init__
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    # Object representation: __repr__, __str__
    # Se for implementar só um, usar __repr__
    # __repr__: Inequívoco. Como faria uma instância de objeto da classe
    def __repr__(self):
        return f'{self.__class__.__name__}({self.owner}, {self.amount})'

    # __str__: Human readable. Para o usuário final
    def __str__(self):
        return f'Account\nOwner: {self.owner}\nAmount: {self.amount}'

    # Iteration: __len__, __getitem__, __reversed__
    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('Please use int for amount')
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    # Para iterar em ordem reversa
    def __reversed__(self):
        return self[::-1]

    # Operator Overloading for Comparing Accounts: __eq__, __lt__
    # functools.total_ordering takes a shortcut and let's you implement
    # only __lt__ and __eq__
    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    # Operator Overloading for Merging Accounts: __add__
    # polymorphism so that acc2 + acc works
    def __add__(self, other):
        owner = f'{self.owner}&{other.owner}'
        start_amount = self.amount + other.amount
        acc = Account(owner, start_amount)
        for t in list(self) + list(other):
            acc.add_transaction(t)
        return acc

    # se fo adicionar a um builtin, precisa implementar o __radd__ também
    # outro exemplo é usar sum: começa com 0.__add__()
    # pensar melhor sobre isso daqui
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    # Callable Python objects: __call__
    def __call__(self):
        print(f'Start amount: {self.amount}')
        print('Transactions: ')
        for transaction in self:
            print(transaction)
        print(f'Balance: {self.balance}')

    # Context Manager Support and the With Statement: __enter__, __exit__
    def __enter__(self):
        print('ENTER WITH: Making backup of transaction for rollback')
        self._copy_transactions = list(self._transactions)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('EXIT WITH:', end=' ')
        if exc_type:
            self._transactions = self._copy_transactions
            print('Rolling back to previous transactions')
            print(f'Transaction resulted in {exc_type.__name__}, ({exc_val})')
        else:
            print('Transactions OK')


# para testar with, usar o método auxiliar
def validate_transaction(acc, amount_to_add):
    with acc as a:
        print(f'Adding {amount_to_add} to account')
        a.add_transaction(amount_to_add)
        print(f'New balance would be: {a.balance}')
        if a.balance < 0:
            raise ValueError('sorry cannot go in debt!')


# Usar assim:
acc = Account('Gabriel', 10)
validate_transaction(acc, 100)
# imprime saída OK

try:
    validate_transaction(acc, -120)
except ValueError as exc:
    print(exc)
# imprime aviso que não pode entrar em débito
