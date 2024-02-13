class BankVersion_1:
    Bank_name = "IPPB"
    Bank_roi = 6
    Bank_addr = "kizikistan"
    
    def __init__(self, C_name, C_acc, C_bal, C_pin):
        self.C_name = C_name
        self.C_acc = C_acc
        self.C_bal = C_bal
        self.C_pin = C_pin
    @classmethod
    def bank_Details(cls):
        print(cls.Bank_name)
        print(cls.Bank_roi)
        print(cls.Bank_addr)
        
    def withdraw(self):
        amount = self.get_Amount()
        if  amount <=  self.C_bal:
            self.C_bal-= amount
            print("withdrawal succefully")
        else:
            print("Insufficient balance !")

    def account_Holder_Detailes(self):
        print(self.C_name)
        print(self.C_acc)
        print(self.C_bal)
        print(self.C_pin)
    @staticmethod  
    def get_Amount():
        a=int(input("enter Value here:-"))
        return a

class BankVersion_2(BankVersion_1):
    Bank_addr = "hyd"
    Bank_mobile  =1234567891

    def __init__(self,C_name, C_acc, C_bal, C_pin,adhar,pan):
        super().__init__(C_name, C_acc, C_bal, C_pin)
        self.Cadhar = adhar
        self.Cpan = pan

    @classmethod
    def bank_Details(cls):
        super().bank_Details()
        #BankVersion_1.bank_Details()
        print(cls.Bank_mobile)
        print(cls.Bank_addr)

    def account_Holder_Detailes(self):
        super().account_Holder_Detailes()
        #BankVersion_1.account_Holder_Detailes(self)
        print(self.Cadhar)
        print(self.Cpan)

    def deposite(self):
        self.C_bal += self.get_Amount()
        print("Balance is ",self.C_bal)
        
    def change_Pin(self):
        pin = int(input("please enter old pin"))
        if self.C_pin  == pin:
            self.C_pin = self.get_Amount()
            print("pin changed successfully and your new pin is",self.C_pin)
    @classmethod
    def change_Roi(cls):
        cls.B_roi = cls.get_Amount()
        print("Rate of Intrest changed succ to =",cls.B_roi)
        

kalyan = BankVersion_2("kalyan", 1234, 1000000, 5252,77773,99999)
print("bank detailes")
kalyan.bank_Details()
print()
print("performing withdraw")
kalyan.withdraw()
print()
print("printing acc holder fdetailse")
kalyan.account_Holder_Detailes()
print()
print("performing deposite")
kalyan.deposite()
print()
print("changing Pin")
kalyan.change_Pin()
print()
print("changing ROI")
kalyan.change_Roi()
