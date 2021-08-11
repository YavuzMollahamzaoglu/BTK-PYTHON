'''class Personel:
    personel_sayisi = 0
    zam_orani = 1.05

    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.eposta = f'{isim}.{soyisim}@firmam.com'
        Personel.personel_sayisi += 1


    
    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'

    def zam_uygula(self):
        self.maas = int(self.maas * Personel.zam_orani)

    @classmethod
    def zam_oranini_belirle(cls, oran):
        eski_oran = cls.zam_orani
        cls.zam_orani = oran
        print(f'Eski zam orani ({eski_oran}) güncellendi. Yeni oran: {cls.zam_orani}')

    @classmethod
    def from_string(cls, per_str):
        isim, soyisim, maas = per_str.split('-')
        return cls(isim, soyisim, maas)


    @staticmethod
    def mesai_gunu(gun):
        if gun.weekday() == 5 or gun.weekday() == 6
          return 'Hafta sonu'
        else:
            return 'Hafta İçi'  

    import

per_str_1 = 'Jack-Cherry-5000'
per_str_2 = 'Dua-Lipa-7000'
per_str_3 = 'Michael-Hans-9000'

yeni_per_1 = Personel.from_string(per_str_1)
print(yeni_per_1.eposta)
print(yeni_per_1.maas)



per_1 = Personel('John', 'Smith', 2000)
per_2 = Personel('Mary','Kaplan', 1700)
per_3 = Personel('Test', 'User', 1000)

print(Personel)
print(per_1.isim)
print(per_2.eposta) 
print(per_2.isim)
print(per_1.maas)

print(f'{per_1.isim} {per_1.soyisim}')
print('{} {}'.format(per_2.isim, per_2.soyisim))
print(per_2.tam_isim())
print(Personel.tam_isim(per_1))


print(per_1.maas)
per_1.zam_uygula()
print(per_1.maas)
print(Personel.zam_orani)
print(per_1.zam_orani)
print(per_2.zam_orani)


Personel.zam_orani = 1.1

print(per_2.zam_orani)

from pprint import pprint
pprint(per_1.__dict__)
print(per_1.zam_orani)
per_1.zam_orani = 1.3
pprint(per_1.__dict__)


print(Personel.personel_sayisi)
Personel.zam_oranini_belirle(1.50) #bu değeri değiştiremeyiz 


from datetime import datetime

timestamp = 1564534
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)



per_1.isim = 'John' 
per_1.soyisim = 'Smith'
per_1.eposta = 'john.33@firmam.com'

per_2.isim = 'Mary'
per_2.soyisim = 'Smith'
per_2.eposta = 'mary.33@firmam.com'''
'''
