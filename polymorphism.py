# class 1
class India():
    def capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("Hindi is the most widely spoken language of India") 

    def type(self):
        print("Inida is a developing country")

# class 2 
class USA():
    def capital(self):
        print("Washington DC is the capital of USA")

    def language(self):
        print("English is the primary language of USA") 

    def type(self):
        print("USA is a developed country")

# onject creation
obj_ind = India()
obj_usa = USA()

# common interface
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()