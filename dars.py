class Talaba:
    def__init__(self,ism,familyasi,tyil,otasining_ism):
        self.name = ism
        self.surname = familyasi
        self.brthday = tyil
        self.ochestva = otasining_ism
    def FIO(self):
        return f"{self.surname.title()} {self.name} {self.ochestva}"
    def yoshi(self):
        return f"{2026-self.tyil} - yoshda"
    t1 = Talaba('maftuna','madaminova','muzaffarovna',2010)
    t2 = Talaba('matluba','ollayorova','bektemirovna',2010)
    t2 = Talaba('mohinur','rozmetova','jorabekovna',2010)
    print(t1.FIO(),t1.yosh(),t2.FIO(),t2.yosh(),t3.FIO(),t3.yosh())