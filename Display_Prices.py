import json

file = open('prices.json',)
data = json.load(file)
fnp,mwp,ftp,wwp,bsp,aep = ([None]*3 for i in range(6))

def list_prices_good(i,condition):
    price = data['items_list'][i]['price']
    global pd
    pd = [0,1,2]
    if '24_hours' in price:
        pd[0] = "$"+str(data['items_list'][i]['price']['24_hours']['average'])
    else:
        pd[0] = "No Sales in Last 24 Hours." 
    
    if '30_days' in price:
        pd[1] = "$"+str(data['items_list'][i]['price']['30_days']['average'])
    else:
        pd[1] = "No Sales in Last 30 Days."     
    
    if 'all_time' in price:
        pd[2] = "$"+str(data['items_list'][i]['price']['all_time']['average'])
    else:
        pd[2] = "No Sales for All Time."
    return pd

for i in data['items_list'].keys():
    weapon_bool = False
    condition = None
    if str(data['items_list'][i]['type']) == 'Weapon':
        weapon_bool = True
        condition = str(i.split(" (")[1])[:-1]
    elif data['items_list'][i]['type'] is None:
        Type = "Sticker"
    else:
        Type = str(data['items_list'][i]['type'])
    
    if 'price' in data['items_list'][i]: 
        if condition == "Factory New":
            fnp = list_prices_good(i,condition)
        elif condition == "Minimal Wear":
            mwp = list_prices_good(i,condition)
        elif condition == "Field-Tested":
            ftp = list_prices_good(i,condition)
        elif condition == "Well-Worn":
            wwp = list_prices_good(i,condition)
        elif condition == "Battle-Scarred":
            bsp = list_prices_good(i,condition)
        else: 
            aep = list_prices_good(i,condition)
        if weapon_bool:
            if condition == "Well-Worn":
                print("Name: "+str(i.split(" (")[0]))
                print("Type: "+data['items_list'][i]['weapon_type'])
                print("Price Information:")
                print("    Factory New:")
                print("        24 Hour Average: "+fnp[0]+" 30 Day Average: "+fnp[1]+" All Time Average: "+fnp[2])
                print("    Minimal Wear:")
                print("        24 Hour Average: "+mwp[0]+" 30 Day Average: "+mwp[1]+" All Time Average: "+mwp[2])
                print("    Field-Tested:")
                print("        24 Hour Average: "+ftp[0]+" 30 Day Average: "+ftp[1]+" All Time Average: "+ftp[2])
                print("    Well-Worn:")
                print("        24 Hour Average: "+wwp[0]+" 30 Day Average: "+wwp[1]+" All Time Average: "+wwp[2])
                print("    Battle-Scarred:")
                print("        24 Hour Average: "+bsp[0]+" 30 Day Average: "+bsp[1]+" All Time Average: "+bsp[2])
                print("==================================================")
        else:
            print("Name: "+i)
            print("Type: "+Type)
            print("Price Information:")
            print("    24 Hour Average: "+aep[0]+" 30 Day Average: "+aep[1]+" All Time Average: "+aep[2])
            print("==================================================")
    else:
        print("Name: "+i)
        print("Type: "+Type)
        print("Price Information:")
        print("    No Price Data")
        print("==================================================")
file.close()