# Импорт модулей
import json
import xml.etree.ElementTree as ET

# Классы
class Building:
    year = None #int
    city = None #string

    def __init__(self,year,city):
        self.city = city
        if (isinstance(year, int) == True):
            self.year = year
        else:
            raise MYException(f"Year must be an integer, but got {type(year).__name__}")



    def getInf(self):
        print("Year:", self.year, " City:" , self.city)



class shop(Building):
    products = None #string
    works = None #bool


    def __init__(self, works, products, year, city):
        if (isinstance(works, bool) == True):
            self.works = works
        else:
            raise MYException(f"Year must be an boolean, but got {type(year).__name__}")

        self.products = products
        super(shop,self).__init__(year,city)


    def getInf(self):
        super().getInf()
        print("Products:" , self.products, " Works:", self.works)



class House(Building):
    family = None #string
    free = None #bool

    def __init__(self, free, family, year, city):
        self.free = free
        self.family = family
        super(House,self).__init__(year,city)


    def getInf(self):
        super().getInf()
        print("Family:" , self.family, " free:", self.free)


#Класс ошибок
class MYException(Exception):
    def __init__(self, message="Invalid input"):
        self.message = message
        super().__init__(self.message)


#Функция чтения JSON файла
def readJSON(filename):
    with open(filename, 'r') as file:
        return json.load(file)


#Функция записи JSON файла
def WriteJSON(data,filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w') as file:
        json.dump(data,file,indent=4)


#Создание обьектов

mag = shop(True, "Eat", 21, "Moscow")

mag2 = shop(False, "None", 0, "Moscow")

house1 = House(True, "Poverinov", 2, "Moscow")

house2 = House(False, "None", 5, "None")

#Запись обьектов в JSON файл

listc = [mag,mag2,house1,house2]

bd = {
    "Buildings" : [] # в массив добавляем обьекты
}

for i in range (len(listc)):
    bd['Buildings'].append(listc[i].__dict__)
WriteJSON(bd,'DB.json')

#print(readJSON('DB.json'))

#Чтение JSON файла

ndata = readJSON('DB.json')

g = shop(ndata['Buildings'][0]['works'], ndata['Buildings'][0]['products'],ndata['Buildings'][0]['year'],ndata['Buildings'][0]['city'])

g.getInf()

#Чтение XML файла

lista = [mag, mag2]

listb = [house1,house2]

tree = ET.parse('line.xml')
root = tree.getroot()
for mag_element in root.findall('Shop'):
    works = bool(mag_element.find('Works').text)
    products = mag_element.find('Products').text
    year = int(mag_element.find('Year').text)
    city = mag_element.find('City').text
    a = shop(works,products,year,city)
    a.getInf()

#Создание древовидной структуры XML и запись

buildings = ET.Element('Buildings')
for i in range (len(lista)):
    id = ET.SubElement(buildings, 'Shop')
    idw = ET.SubElement(id, 'Works')
    idp = ET.SubElement(id, 'Products')
    idy = ET.SubElement(id, 'Year')
    idc = ET.SubElement(id, 'City')
    idw.text = str(lista[i].works)
    idp.text = str(lista[i].products)
    idy.text = str(lista[i].year)
    idc.text = str(lista[i].city)

for i in range (len(listb)):
    id = ET.SubElement(buildings, 'House')
    idw = ET.SubElement(id, 'free')
    idp = ET.SubElement(id, 'family')
    idy = ET.SubElement(id, 'Year')
    idc = ET.SubElement(id, 'City')
    idw.text = str(listb[i].free)
    idp.text = str(listb[i].family)
    idy.text = str(listb[i].year)
    idc.text = str(listb[i].city)

data = ET.tostring(buildings, encoding='unicode')
file = open('line.xml', 'w')
file.write(data)
