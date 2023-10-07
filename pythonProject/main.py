# Импорт модулей
import json
import xml.etree.ElementTree as ET


# Классы
class Building:
    year = None  # int
    city = None  # string




    def __init__(self, year, city):
        if(isinstance(city,str) == True):
            self.__city = city
        else:
            raise MYException(f"Year must be an string, but got {type(city).__name__}")

        if (isinstance(year, int) == True):
            self.year = year
        else:
            raise MYException(f"Year must be an integer, but got {type(year).__name__}")

    def getC(self):
        return self.__city
    def setC(self,city):
        self.__city = city


    def getInf(self):
        print("Year:", self.year, " City:", self.city)


class shop(Building):
    products = None  # string
    works = None  # bool

    def __init__(self, works, products, year, city):
        if (isinstance(works, bool) == True):
            self.works = works
        else:
            raise MYException(f"Year must be an boolean, but got {type(works).__name__}")

        if (isinstance(products, str) == True):
            self.products = products
        else:
            raise MYException(f"Year must be an string, but got {type(products).__name__}")
        super(shop, self).__init__(year, city)

    def getInf(self):
        super().getInf()
        print("Products:", self.products, " Works:", self.works)


class House(Building):
    family = None  # string
    free = None  # bool

    def __init__(self, free, family, year, city):
        if (isinstance(free, bool) == True):
            self.free = free
        else:
            raise MYException(f"Year must be an boolean, but got {type(free).__name__}")
        if (isinstance(family, str) == True):
            self.family = family
        else:
            raise MYException(f"Year must be an string, but got {type(family).__name__}")
        super(House, self).__init__(year, city)

    def getInf(self):
        super().getInf()
        print("Family:", self.family, " free:", self.free)


# Класс ошибок
class MYException(Exception):
    def __init__(self, message="Invalid input"):
        self.message = message
        super().__init__(self.message)


# Функция чтения JSON файла
def readJSON(filename):
    with open(filename, 'r') as file:
        return json.load(file)


# Функция записи JSON файла
def WriteJSON(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


# Создание обьектов

mag = shop(True, "Eat", 21, "Moscow")

mag2 = shop(False, "None", 0, "Moscow")

house1 = House(True, "Poverinov", 2, "Moscow")

house2 = House(False, "None", 5, "None")
ndata = readJSON('DB.json')
g = shop(ndata['Buildings'][1]['works'],ndata['Buildings'][1]['products'],ndata['Buildings'][1]['year'],ndata['Buildings'][1]['_Building__city'])

g.getInf()
def CreateShop():
    print("Напишите works: True or False")
    worksIN = input()
    print("Напишите вид товаров")
    productsIN = input()
    print("Напишите сколько лет работает магазин")
    yearIN = input()
    print("Напишите город в котором находится магазин")
    cityIN = input()
    base = shop(bool(worksIN), productsIN, int(yearIN), cityIN)
    return base
def CreateHouse():
    print("Напишите free: True or False")
    freeIN = input()
    print("Напишите вид фамилию владельца")
    FamilysIN = input()
    print("Напишите сколько лет дому")
    yearIN = input()
    print("Напишите город в котором находится дом")
    cityIN = input()
    base = House(bool(freeIN), FamilysIN, int(yearIN), cityIN)
    return base
listc = [mag, mag2, house1, house2]

bd = {
    "Buildings": []  # в массив добавляем обьекты
}
lista = [mag, mag2]

listb = [house1, house2]

print("Хотите ли вы создать обьект? (Y/N)")
a = input()
if (a == "Y") or (a == "y"):
    print("В каком формате вы хотите записать обьект? (xml,json,all)")
    aaa = input()
    if ( aaa == "json") or (aaa == "JSON") or (aaa == "Json"):
        print("Хотите ли вы создать обьект Shop или House? (shop/house)")
        aa = input()
        if (aa == "shop") or (aa == "SHOP") or (aa == "Shop"):
         b = CreateShop()
         bd['Buildings'].append(b.__dict__)
        if (aa == "house") or (aa == "House") or (aa == "HOUSE"):
            b = CreateHouse()
            bd['Buildings'].append(b.__dict__)
    if ( aaa == "xml") or (aaa =="XML") or (aaa=="Xml"):
        print("Хотите ли вы создать обьект Shop или House? (shop/house)")
        aa = input()
        if (aa == "shop") or (aa == "SHOP") or (aa == "Shop"):
         b = CreateShop()
         lista.append(b)
        if (aa == "house") or (aa == "HOUSE") or (aa == "House"):
            b = CreateHouse()
            listb.append(b)
    if ( aaa == "all"):
        print("Хотите ли вы создать обьект Shop или House? (shop/house)")
        aa = input()
        if (aa == "shop") or (aa == "SHOP") or (aa == "Shop"):
         b = CreateShop()
         lista.append(b)
         bd['Buildings'].append(b.__dict__)
        if (aa == "house") or (aa == "HOUSE") or (aa == "House"):
            b = CreateHouse()
            listb.append(b)
            bd['Buildings'].append(b.__dict__)


# Запись обьектов в JSON файл

for i in range(len(listc)):
    bd['Buildings'].append(listc[i].__dict__)
WriteJSON(bd, 'DB.json')

# print(readJSON('DB.json'))

# Чтение JSON файла





# Чтение XML файла


tree = ET.parse('line.xml')
root = tree.getroot()
for mag_element in root.findall('Shop'):
    works = bool(mag_element.find('Works').text)
    products = mag_element.find('Products').text
    year = int(mag_element.find('Year').text)
    city = mag_element.find('City').text
    a = shop(works, products, year, city)
    a.getInf() # вывод обьекта составленных из данный XML

# Создание древовидной структуры XML и запись

buildings = ET.Element('Buildings')
for i in range(len(lista)):
    id = ET.SubElement(buildings, 'Shop')
    idw = ET.SubElement(id, 'Works')
    idp = ET.SubElement(id, 'Products')
    idy = ET.SubElement(id, 'Year')
    idc = ET.SubElement(id, 'City')
    idw.text = str(lista[i].works)
    idp.text = str(lista[i].products)
    idy.text = str(lista[i].year)
    idc.text = str(lista[i].getC())

for i in range(len(listb)):
    id = ET.SubElement(buildings, 'House')
    idw = ET.SubElement(id, 'free')
    idp = ET.SubElement(id, 'family')
    idy = ET.SubElement(id, 'Year')
    idc = ET.SubElement(id, 'City')
    idw.text = str(listb[i].free)
    idp.text = str(listb[i].family)
    idy.text = str(listb[i].year)
    idc.text = str(listb[i].getC())

data = ET.tostring(buildings, encoding='unicode')
file = open('line.xml', 'w')
file.write(data)


