b=0
time=''
cn=''
import time
import re
class Err(Exception):
    pass
class Passbook:
    
    def __init__(self,accno,ifscode,name,branch,balance):
        self.accno=accno
        self.ifscode=ifscode
        self.name=name
        self.branch=branch
        self.balance=balance
        

    def passbook(self):
        print('Account Number: ',self.accno,' ','IFSCode: ',self.ifscode,' ','Bank Name: ',self.name,' ','Branch: ',self.branch,' ','Balance: ',self.balance) 
    
class KYC(Passbook):
    
    def __init__(self,accno,ifscode,name,branch,balance,custname,age,gender,phone,pancard,aadharcard,address,accounttype,password):
        Passbook.__init__(self,accno,ifscode,name,branch,balance)
        self.custname=custname
        self.age=age
        self.gender=gender
        self.phone=phone
        self.pancard=pancard
        self.aadharcard=aadharcard
        self.address=address
        self.accounttype=accounttype
        self.password=password
        
        global cn
        cn=custname
    
    def kyc(self):
        print('Name: ',self.custname,'\nAge: ',self.age,'\nGender: ',self.gender,'\nPhone: ',self.phone,'\npancard: ',self.pancard,'\nAadhar card: ',self.aadharcard,'\nAddress: ',self.address,'\nAccounttype: ',self.accounttype)

    def passvalid(self):

        pcount=3
        while pcount>0:
            
            pwd=input('Enter your 9 character Internet banking password: ')
            if len(pwd)>9:
                print('Password Invalid: Entered password is greater than 9 characters')
                pcount-=1
            elif len(pwd)<9:
                print('Password Invalid: Entered password is less than 9 characters')
                pcount-=1
            elif not re.search('[a-z]',pwd):
                print('Password Invalid: Entered password does not contain lower case letters')
                pcount-=1
            elif not re.search('[A-Z]',pwd):
                print('Password Invalid: Entered password does not contain lower case letters')
                pcount-=1
            elif not re.search('[0-9]',pwd):
                print('Password Invalid: Entered password does not contain digits')
                pcount-=1
            elif not re.search('[!"£$%^&*#@]',pwd):
                print('Password Invalid: Entered password does not contain special characters')
                pcount-=1
            elif pwd!=self.password:
                print('Entered password is not equal to the registered password with the bank')
                pcount-=1
            if pwd!=self.password and pcount!=0:
                
                print('Warning: You have ',pcount,'wrong chances left before your account gets blocked')
            if pcount==0:break
                
            elif pwd==self.password:
                print('Password authentication successful, you are successfully logged in.')
                break
            self.welcome()
        if pcount==0:
            print('Your account is blocked as you have exceeded your wrong attempts in entering password')
            quit()

        
    def welcome(self):
        
        print('------------------------------------------------------------------')
        print('             Welcome to State Bank of India')
        print('------------------------------------------------------------------')

    def opb(self):
        global b
        b=self.balance
        
    def exp(self):
        c=[]
        d=[]
        ty=[]
        bal=[]
        ti=[]
        global time
        n=int(input('Enter the number of transactions: '))
        self.welcome()
        for i in range(1,n+1):
            print('Transaction ',i,':',end=' ')
            try:
                t=int(input('Enter the choice for transaction type(1.Credit;2.Debit): '))
                if t>2 or t<1:
                    raise Err
            except:
                print('Enter correct value for transaction type')
                t=int(input('Enter the choice for transaction type(1.Credit;2.Debit): '))
                
                
            if t==1:
                credit=round(float(input('Enter the amount to be deposited: ')),1)
                if credit>0:
                    self.balance=round(self.balance+credit,1)
                    c.append(credit)
                    d.append(0)
                    ty.append('Cr')
                    bal.append(self.balance)
                    ti.append(time.asctime())

            if t==2:
                debit=round(float(input('Enter the amount to be withdrawn: ')),1)
                if debit>self.balance:
                    print('Transaction ',i,' declined due to insufficient balance. Amount available is ',self.balance)
                    n=n-1
                    self.welcome()
                if debit>0 and debit<self.balance:
                    self.balance=round(self.balance-debit,1)
                    c.append(0)
                    d.append(debit)
                    ty.append('Dr')
                    bal.append(self.balance)
                    ti.append(time.asctime())
            
            if i<n:
                self.welcome()
        
        
        

        print('**************************************************************************')
        print('             State Bank of India Passbook Details')
        print('**************************************************************************')
        print('Opening balance: ',b)
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Status','  Credit','      Debit','      Total','        Time')
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        for j in range(n):

            
            print(ty[j],'      ',c[j],'        ',d[j],'     ',bal[j],'    ',ti[j])
        
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

        
        


k=KYC(12396586,3001,'SBI','KK Nagar',10000,'Karthik',28,'M',59635856,'OIUHR65365',965874523658,'Chennai','Platinum','Pass@1234')
print('Hi ',cn)

k.welcome()
k.passvalid()
k.welcome()
k.opb()
k.exp()



        
    
        
