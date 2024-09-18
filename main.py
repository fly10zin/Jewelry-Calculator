import requests
from bs4 import BeautifulSoup


url = "https://www.apmex.com/gold-price"

metal_option = {"a": "gold", "b":"silver", "c": "platinum"}

loop = True
while loop: 
    print("What type of metal is your jewelry?")
    metal = input("Options: (a)Gold (b)Silver (c)Platinum ").lower()

    if metal in metal_option:
        print(f"You would like to find the value of your {metal_option[metal]} jewelry")
        loop = False
    else:
        print("Please choose from the given options.")

if metal == "a":
    purity = int(input(f"What karat of gold is your jewelry in number? "))
        

def gold_calculation(purity):
    purity = (purity / 24) * 100
    print(f"Purity: {purity:.2f}%")
    return purity/100

weight = float(input("How much grams does your jewelry weight? "))

def get_price():
    response = requests.get(url)
    #print(response)
   
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')


        price_element = soup.find('span', id='metal-priceask')
    
        
        if price_element:
            price = price_element.get_text(strip=True)
            print(f"Current Gold per Oz: {price}")
            price_num = price.split(" ")[0]
            return float(price_num.replace("$","").replace(",",""))
        else:
            print("Could not find the gold price on the page.")

    else:
        print(f"Failed to load {response.status_code}")

live_gold_price = get_price()




def value (purity, live_gold_price, weight):
    total_price = purity * (live_gold_price/31.1035) * weight
   # print (f"{purity, live_gold_price, weight}")
    return total_price

output_money = value(gold_calculation(purity), live_gold_price, weight)

print(f"With the information you entered, the current market value of your {metal_option[metal]} jewelry is ${output_money:.2f}")








