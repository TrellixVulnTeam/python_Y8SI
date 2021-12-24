# doct type of morphism
class Nepal:
    def capital(self):
        print('kathmandu is the capital if Nepal')

    def language(self):
        print('Nepali is the most widely spoken language')

    def type(self):
        print('Nepal is a Developing Country')

class USA():
    def capital(self):
        print("Washington D.C is the capital of USA")

    def language(self):
        print('English is the most spoken language')
    
    def type(self):
        print('USA is the developed country')

obj_nep = Nepal()
obj_usa = USA()
for country in (obj_nep, obj_usa):
    print(country.capital)
    print(country.language)
    print(country.type)