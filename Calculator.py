from colorama import Fore
from pyfiglet import Figlet
wik=Figlet()
print(Fore.RED + wik.
renderText("WikiSaleh"))
number1=input(Fore.BLUE + "Please Enter Number 1 : ")
number2 = input(Fore.GREEN + "Please Enter Number 2 : " )
number1=int(number1)
number2=int(number2)
Jam = ("{} + {} = {}" .format(number1, number2, number1 + number2))
Tafrigh = ("{} - {} = {}" .format(number1, number2, number1 - number2))
Zarb = ("{} × {} = {}" .format(number1, number2, number1 * number2))
Taghsim = ("{} ÷ {} = {}" .format(number1, number2, number1 / number2))
operation=input(Fore.WHITE + "1.Jam " + Fore.RED + " 2.Tafrigh" + Fore.BLUE + " 3.Zarb" + Fore.YELLOW + " 4.Taghsim : ")
if operation=="1":print(Jam)
elif operation=="2":print(Tafrigh)
elif operation=="3":print(Zarb)
elif operation=="4":print(Taghsim)
else:print(Fore.RED + "Please Enter Valid Operation:1,2,3,4")
