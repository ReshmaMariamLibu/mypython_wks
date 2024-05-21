class Bank:
    account_no:int
    account_type:str
    balance:int
    bank_name:str="SBI"  #static variable
    person_name:str
    ifsc_code:str

    def __init__(self,account_no,account_type,balance,person_name,ifsc_code):
          self.account_no=account_no
          self.account_type=account_type
          self.balance=balance
          self.person_name=person_name
          self.ifsc_code=ifsc_code
  
    def withdraw_amount(self,amount):
        if self.balance>amount:
          self.balance-=amount
          print(f"your {self.bank_name} account debited with amount {amount} avail bal {self.balance}")
        else:
           print("transacation declined...........")


    def deposit(self,amount):
      self.balance+=amount
      print(f"your {self.bank_name} account credited with amount {amount} avail bal {self.balance}")
       

    def bal_enq(self):
       print(f"your {self.bank_name} account balance is {self.balance}")


bank1=Bank(234,"current",50000,"anika","sbin@123")
bank1.bal_enq()
bank1.deposit(40000)
bank1.withdraw_amount(60000)
















       

