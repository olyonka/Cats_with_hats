
class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest_rate):
        super().__init__(balance, account_number)
        self._interest_rate = interest_rate

    def add_interest(self):
        self._balance += self._balance * self._interest_rate


class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self._overdraft_limit = overdraft_limit

    def send_overdraft_letter(self):
        if self._balance < 0:
            print(f'Overdraft letter sent for account {self._account_number}')


class Bank:
    def __init__(self):
        self._accounts = []

    def open_account(self, account):
        self._accounts.append(account)

    def close_account(self, account):
        self._accounts.remove(account)

    def pay_dividend(self, amount):
        for account in self._accounts:
            account.deposit(amount)

    def update(self):
        for account in self._accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.send_overdraft_letter()


# Test open_account method of Bank class
if __name__ == "__main__":
    bank = Bank()

    savings_account = SavingsAccount.create_account("SA123")
    savings_account.deposit(1000)

    current_account = CurrentAccount.create_account("CA456")
    current_account.deposit(500)
    current_account.withdraw(700)

    bank.open_account(savings_account)
    bank.open_account(current_account)

    print("Accounts opened:")
    for account in bank._accounts:
        print(account)


    print("\nUpdating accounts:")
    bank.update()

    print("\nUpdated accounts:")
    for account in bank._accounts:
        print(account)