class Account:
    def __init__(self,account_name,account_number,bank_name):
        self.account_name = account_name
        self.account_number = account_number
        self.bank_name = bank_name

    def display(self):
        print(f"Account Name: {self.account_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Bank Name: {self.bank_name}")


class CurrentAccount(Account):
    def __init__(self,account_name,account_number,bank_name,tpin):
        super().__init__(account_name,account_number,bank_name)
        self.tpin= tpin
    

    
    def display(self):
        super().display()
        print(f"TPIN Number: {self.tpin}")


if __name__ == "__main__":
    c1 = CurrentAccount("Praful",1234567890,"SBI","123456")
    c1.display()