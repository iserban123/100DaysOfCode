from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
genrep = CoffeeMaker()
itema = Menu()
bani = MoneyMachine()
#val = MenuItem()

#itema.__init__()#
#for x in itema.menu:
 #   y = itema.menu("latte")
  #  print(y)



option = input(f"What do you like?{itema.get_items()}: ")
print(itema.get_items())
if option == "report":
    genrep.report()
else:
    is_found = itema.find_drink(option)
    yes_no = genrep.is_resource_sufficient(is_found)
    if yes_no == True:
        bani.process_coins()
       # bani.make_payment(val.cost)
        genrep.make_coffee(is_found)




