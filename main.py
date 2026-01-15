class Build:
    year = None
    city = None
    def __init__(self, year, city):
        self.year = year
        self.city = city
        self.get_info()
    def get_info(self):
        print("Year: ", self.year, '!!!! ' "City: ", self.city, sep='')
class School(Build):
    pupils = None
    def __init__(self, year, city, pupils = 500):
        super(School, self).__init__(year, city)
        self.pupils = pupils
class House(Build):
    pass
class Shop(Build):
    pass
School = Build(1990, 'Lviv')
School.get_info()
house = Build(2010, 'Lviv')
house.get_info()
shop = Build(2020, 'Lviv')

