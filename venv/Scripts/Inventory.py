from faker import Faker
from collections import OrderedDict
from time import sleep
from datetime import timedelta, date, datetime, time

import sys
import os

fake = Faker()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def currency(amount):
   return "${:,.2f}".format(amount)

def percentage(amount):
    return "{:.0%}".format(amount)
ct = datetime.now()
print((ct.strftime("%c")))

num = 5
space = "\t" * 4
print(f'{space}{space}{space}\tRun how many times?: {bcolors.UNDERLINE}{num}{bcolors.ENDC} ')
print(f'{space}{space}{space}{bcolors.BOLD}{bcolors.BOLD}********** INVENTORY **********{bcolors.ENDC}{bcolors.ENDC}\n')
answer = 'y'

grandtotal = 0
gemslist = {}
gemsum = 0

while answer == 'y':
    def screen():
        os.system("mode con lines=20")

    def getinventory():
        iv = {}
        iv['type1'] = Faker().safe_color_name()
        iv['type2'] = Faker().safe_color_name()
        iv['type3'] = Faker().safe_color_name()
        iv['type4'] = Faker().safe_color_name()
        iv['type5'] = Faker().safe_color_name()
        iv['inventory'] = Faker().random_elements(elements=OrderedDict(
            [(iv['type1'], 0.5),
             (iv['type2'], 0.2),
             (iv['type3'], 0.1),
             (iv['type4'], 0.1),
             (iv['type5'], 0.1)]),
            length=20, unique=False)
        return iv
    def calculatetotal(ri):
        t = [ri['type1'],
             ri['type2'],
             ri['type3'],
             ri['type4'],
             ri['type5']]

        tv = [100, 200, 500, 500, 1000]
        ti = [ri['inventory'].count(i['type1']),
          ri['inventory'].count(i['type2']),
          ri['inventory'].count(i['type3']),
          ri['inventory'].count(i['type4']),
          ri['inventory'].count(i['type2'])]

        total = 0
        for nm in range(5):
            total = total + (tv[nm] * ti[nm])
        #for nm in range(5):
            # print(f'{ti[nm]} {t[nm].capitalize()}
            # gems worth ${tv[nm]}.00 each.   
            # ++ ${ti[nm] * tv[nm]}')

        for nm in range(5):
            if t[nm] in gemslist:
                gemslist[t[nm]] = gemslist[t[nm]] + ti[nm]
            else:
                gemslist[t[nm]] = ti[nm]
        #print(f'Total Earned: ${total}.00')
        return total

    load = 0
    per = f"{str(load)}/{str(num)}"
    for r in range(int(num)):
        screen()
        i = getinventory()
        w = calculatetotal(i)
        grandtotal = grandtotal + w
        load = load + 1
        pe = (int(load) / int(num))
        perc = pe * 30
        per = f"{str(load)}/{str(num)}"
        loaded = f"{bcolors.OKGREEN}•{bcolors.ENDC}" * int(perc)
        unloaded = f"{bcolors.FAIL}°{bcolors.ENDC}" * (30 - int(perc))

        bar = f"[{loaded}{unloaded}]"
        loadereven = 0
        if (load % 2) == 0:
            loader = '°'
            loadereven = 1
        else:
            loader = '•'
            loadereven = 0
        # sys.stdout.write(f'\r{loader * 3}  Loading  {loader * 3}')
        # sys.stdout.write(f'  {per}{bar}  ')

        gemsum = 0
        for s in list(gemslist.values()):
            gemsum = gemsum + s
        #sys.stdout.write(f'\n{loader * 10} Collecting Gems {loader * 10}')
        #sys.stdout.write(f'-----Total Gems: {gemsum} ')

        loadertxt = f'{bar} {per} '
        grandtotaltxt = (f'{bcolors.OKGREEN}{bcolors.UNDERLINE}Currency{bcolors.ENDC}: {bcolors.BOLD}{currency(grandtotal)}{bcolors.ENDC}{bcolors.ENDC}')
        gemstxt = (f'{bcolors.OKBLUE}{loader * 2}{bcolors.ENDC}{bcolors.BOLD}Collecting Gems{bcolors.ENDC}{bcolors.OKBLUE}{loader * 2}{bcolors.ENDC}') if loadereven != 1 else (f'{bcolors.FAIL}{loader * 2}{bcolors.ENDC}Collecting Gems{bcolors.FAIL}{loader * 2}{bcolors.ENDC}')
        totalgemtxt = (f'{bcolors.OKBLUE}{bcolors.UNDERLINE}Gems{bcolors.ENDC}: {bcolors.BOLD}{gemsum}{bcolors.ENDC}{bcolors.ENDC}')

        sys.stdout.truncate(0)
        if num == load:
            break
        else:
            sys.stdout.writelines(f'\r{gemstxt} | {percentage(pe)} {loadertxt}| {totalgemtxt} | {grandtotaltxt} | {gemstxt}')
        sys.stdout.flush()
        #sleep(.0001)

    gemstxt = (f'--Complete--')
    sys.stdout.writelines(
            f'\r{bcolors.OKGREEN}{bcolors.BOLD}{per}{bcolors.ENDC}{bcolors.ENDC} '
            f'{bcolors.BOLD}{gemstxt.upper()}{bcolors.ENDC} '
            f'{bcolors.BOLD}{bar}{bcolors.ENDC}\n')

    sys.stdout.write(f'\n{bcolors.UNDERLINE}{"Gem Type".capitalize()}{bcolors.ENDC}  \t\t{bcolors.UNDERLINE}Total{bcolors.ENDC}')
    for k, v in list(gemslist.items()):
         sys.stdout.write(f'\n{k.capitalize()} Gems: \t\t{v}')

    sys.stdout.writelines(f'\n\n{totalgemtxt} \n{grandtotaltxt}\n ')
    ft = datetime.now()
    td = (ft - ct)
    tdms = f"{td.microseconds} milliseconds " if td.microseconds != 0 else ( "" )
    tds = f"{td.total_seconds()} seconds " if td.total_seconds() != 0 else ( "" )
    tdm = f"seconds " if td.total_seconds() != 0 else ( "" )

    print(f"{tds} {tdms}")
