import p

siya=gp.Google_pay("siyas@gmail.com","9003085347","siyaramesh")
siya.email_verification()
siya.mobile_verification()
siya.name_verification()
siya.otp_verification(15698,15698)
siya.Bank_verification()
siya.set_Pin("5384")


class Phone_pe(p.Gpay):                                                                                     
    def __init__(self,Email_ID,Phone_number,Name):
        super().__init__(Email_ID,Phone_number,Name)

  
        
riya=Phone_pe("riyas@gmail.com","9003085347","riya")
riya.mobile_verification()
riya.name_verification()
riya.otp_verification(780965,780965)
riya.Bank_verification()
riya.set_Pin("238790")



        
googlepay=[{"name":"jina","gpaynum":9789869415,"type":"personal","transaction":"regular"},
           {"name":"kavya","gpaynum":9677150962,"type":"personal","transaction":"regular"},
           {"name":"chitra","gpaynum":9003899016,"type":"personal","transaction":"rare"},
           {"name":"kiara","gpaynum":9361486028,"type":"personal","transaction":"regular"},
           {"name":"mhima","gpaynum":7448729790,"type":"personal","transaction":"regular"},
           {"name":"rohini","gpaynum":6380874698,"type":"personal","transaction":"rare"},
           {"name":"sabitha","gpaynum":9361447138,"type":"personal","transaction":"regular"},
           {"name":"sagarika","gpaynum":7358701090,"type":"personal","transaction":"regular"},
           {"name":"nivetha","gpaynum":6382718022,"type":"personal","transaction":"regular"},
           {"name":"mohi","gpaynum":6383138140,"type":"personal","transaction":"rare"},
           {"name":"divya","gpaynum":7904104077,"type":"personal","transaction":"regular"},]


for i in googlepay:                                                                                                             
    for j,k in i.items():                                                                                                       
        print(f"{j}:{k}")
    

