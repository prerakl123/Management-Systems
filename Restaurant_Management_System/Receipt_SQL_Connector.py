import pymysql


def print_data():
    pass


def AddtoDrinks(command):
    """Add Drinks Data to table : drinks_info.
    :param command (received through dicts and lists corresponding to drinks details in '__main__' file)"""
    connection = pymysql.Connect(host='localhost', user='root', passwd='', database='rms_ri_db')
    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()


def AddtoFood(command):
    """Add Food Data to table : food_info.
    :param command (received through dicts and lists corresponding to food details in '__main__' file)"""
    connection = pymysql.Connect(host='localhost', user='root', passwd='', database='rms_ri_db')
    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()


def AddtoPackedFood(command):
    """Add Packed Food Data to table : packed_food_info.
    :param command (received through dicts and lists corresponding to packed food details in '__main__' file)"""
    connection = pymysql.Connect(host='localhost', user='root', passwd='', database='rms_ri_db')
    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()


def Connect_TO_SQL():
    """Connects to database and creates tables if they don't exist."""
    runing = True
    while runing:
        try:
            connection = pymysql.Connect(host='localhost', user='root', passwd='', database='rms_ri_db')
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS receipt_info(BILL_NO INTEGER(25) PRIMARY KEY,DATE_OF_PURCHASE DATE,'
                           'MODE_OF_PAY VARCHAR(30),TOTAL_BILL INTEGER(30))')
            connection.commit()
            cursor.execute('CREATE TABLE IF NOT EXISTS drinks_info(BILL_NO INTEGER(25) PRIMARY KEY,MineralWater INTEGER(15),'
                   'HotCoffee INTEGER(15),ColdCoffee INTEGER(15),HotChocolate INTEGER(15),Cappuccino INTEGER(15),Tea INTEGER(15),IcedTea INTEGER(15),'
                   'ChocolateShake_R INTEGER(15),OreoShake_R INTEGER(15),StrawberryShake_R INTEGER(15),PineappleShake_R INTEGER(15),KitkatShake_R INTEGER(15),ChocolateShake_T INTEGER(15),'
                   'OreoShake_T INTEGER(15),StrawberryShake_T INTEGER(15),PineappleShake_T INTEGER(15),KitkatShake_T INTEGER(15),ColdDrink_C INTEGER(15),ColdDrink_S INTEGER(15),'
                   'VirginMojito INTEGER(15),MoscowMule INTEGER(15),Martini INTEGER(15),CranberryJuice INTEGER(15))')
            connection.commit()
            cursor.execute('CREATE TABLE IF NOT EXISTS food_info(BILL_NO INTEGER(25) PRIMARY KEY,FrenchFries INTEGER(15),'
                   'CheeseBalls INTEGER(15),'
                   'VegSandwich INTEGER(15),GrilledSandwich INTEGER(15),GrilledCheeseSandwich INTEGER(15),'
                   'PaneerSandwich INTEGER(15),NutellaSandwich INTEGER(15),AlooTikkiBurger INTEGER(15),'
                   'VegWhooper INTEGER(15),'
                   'DoubleCheeseBurger INTEGER(15),PaneerKingBurger INTEGER(15),WhitePasta INTEGER(15),'
                   'RedPasta INTEGER(15),'
                   'SpecialItalianPasta INTEGER(15),'
                   'Margherita INTEGER(15),SuperVegiePizza INTEGER(15),PaneerCrispPizza INTEGER(15),'
                   'PeriPeriPaneerPizza INTEGER(15),ChefSpecialCountryConnectionPizza INTEGER(15),'
                   'MexicanTacos INTEGER(15),'
                   'PaneerWrap INTEGER(15),SpringRoll INTEGER(15),PizzaRolls INTEGER(15))')
            connection.commit()
            cursor.execute('CREATE TABLE IF NOT EXISTS packed_food_info(BILL_NO INTEGER(25) PRIMARY KEY,Lays INTEGER(15),'
                   'Kurkure INTEGER('
                   '15),'
                   'Bingo INTEGER(15),Nutella INTEGER(15),HersheysChocolateSyrup INTEGER(15),Bhujia INTEGER(15),'
                   'Mixture INTEGER(15),SoyaStix INTEGER(15),'
                   'BrittaniaMarieGold INTEGER(15),_5050_ INTEGER(15),'
                   'Oreo INTEGER(15),HideandSeek INTEGER(15),DarkFantasy INTEGER(15),KinderJoy INTEGER(15),'
                   'Nachos INTEGER(15),Bournvita INTEGER(15),'
                   'Complan INTEGER(15),KellogsChocos INTEGER(15),Rusk INTEGER(15),DairyMilkSilk INTEGER(15),'
                   'NestleDarkSensation INTEGER(15),HersheysWhiteCocoaChocolate INTEGER(15),'
                   'Pedigree INTEGER(15))')
            connection.commit()
            runing = False

        except Warning as w:
            print('Error in creating tables'), w
            print('TABLES EXIST...')
            runing = False
        except pymysql.err.ER.CANT_CREATE_TABLE:
            print('TABLES EXIST....')


if __name__ == '__main__':
    '''Connecting database and creating database if it doesn't exist.'''
    running = True
    while running:
        try:
            connect = pymysql.Connect(host='localhost', user='root', passwd='', database='rms_ri_db')
            if connect is True:
                continue
            else:
                conn = pymysql.Connect(host='localhost', user='root', passwd='')
                curs = conn.cursor()
                curs.execute('CREATE DATABASE rms_ri_db')
                conn.commit()
                Connect_TO_SQL()
        except Exception as e:
            print('Could not Connect to database!', e)
            print()
            print('Creating Database and Tables...')
            try:
                conn = pymysql.Connect(host='localhost', user='root', passwd='')
                curs = conn.cursor()
                curs.execute('CREATE DATABASE rms_ri_db')
                conn.commit()
                Connect_TO_SQL()
                running = False
            except Exception as E:
                print("Could not create 'rms_ri_db' !", E)
                running = False
                Connect_TO_SQL()
        except pymysql.err.ER.CANT_CREATE_DB:
            print('Database exists.')
