class Gpay:                                                                                   
    
    def __init__(self,Email,number,Name):                                                                  
        self.emailid=Email_ID
        self.mobile=Phone_number
        self.name=Name
        
        
    def email(self):
        if isinstance(self.emailid,str):                                                                               
            if len(self.emailid) <= 10:                                                                         
                print("email_id verified")
            else:
                raise ValueError("The entered email exceeds value")
        else:
            raise TypeError("invalid emailid")
    def mobile(self):
        if (len(self.mobile)==10) and self.mobile[0]>5:
            if type(self.mobile) == str:                                                                            
                print("Number verified")
            else:
                raise TypeError("The entered phone number is invalid ")
        else:
            raise ValueError("the number exceeds value")
        
    def name(self):
        if type(self.__name) == str:
            if len(self.__name) <= 10:                                                                                
                print("name verified")
            else:
                raise ValueError("The entered name exceeds value")
        else:
            raise TypeError("The entered name must contain only letters")

    def otp(self,code,otp):
        if(otp==code):
            print("otp verified")
        else:
            raise ValueError("enterded otp is not a match" )

    def Bank(self):
        self.accno=[]
        self.anumber=7896789032
        self.accno.append(self.anumber)                                                                     
        print(self.acco)
        print(" Account Verified")

   
    

    def pinnum(self,number):
        self.pin=number
        if (len(self.pin)==4 or len(self.pin) ==6):
            print(" pin is generated")
        else:
            raise ValueError("Invalid pin")

   
