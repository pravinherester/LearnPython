from coffee_maker import CoffeeMaker
from menu import Menu
ACTION_OFF="OFF"
ACTION_REPORT="REPORT"
coffeeMaker=CoffeeMaker()
off_flag=True

action=input("​What would you like? (espresso/latte/cappuccino):")
while off_flag ==True:
        if action ==ACTION_OFF.lower():
            off_flag=False
            break
        elif action==ACTION_REPORT.lower():
            coffeeMaker.report()
           
        else:
            menu=Menu()
            drink=menu.find_drink(action)
            resource_sufficient=coffeeMaker.is_resource_sufficient(drink)
            print(resource_sufficient)
            
        action=input("​What would you like? (espresso/latte/cappuccino):")   

        
