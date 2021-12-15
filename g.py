import p
def __init__(self):
        print("welcome to gpay")

siya=p.Gpay("siyas@gmail.com","9003085347","siyaramesh")
siya.email()
siya.mobile()
siya.name()
siya.otp(15698,15698)
siya.Bank()
siya.set_Pin("88899")


class Phone_pe(p.Gpay):                                                                                     
    def __init__(self,Email,number,Name):
        super().__init__(Email,number,Name)

  
        
riya=Phone_pe("riyas@gmail.com","9003085347","riya")
riya.mobile_verification()
riya.name_verification()
riya.otp_verification(780965,780965)
riya.Bank_verification()
riya.set_Pin("238790")



        
googlepay=[{"name":"jina","phone":9789869415,"type":"personal"},{"name":"kavya","phone":9677150962,"type":"personal"},{"name":"chitra","phone":9003899016,"type":"personal"},{"name":"kiara","phone":9361486028,"type":"personal"},{"name":"mhima","phone":7448729790,"type":"personal"},
{"name":"rohini","phone":6380874698,"type":"personal"},{"name":"sabitha","phone":9361447138,"type":"personal"},{"name":"sagarika","phone":7358701090,"type":"personal"},{"name":"nivetha","phone":6382718022,"type":"personal"},
{"name":"mohi","phone":6383138140,"type":"personal"},{"name":"divya","phone":7904104077,"type":"personal"},]


for i in googlepay:                                                                                                             
    for j,k in i.items():                                                                                                       
        print(f"{j}:{k}")
    

