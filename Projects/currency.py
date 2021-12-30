# currency converter 
# bitcoin convertor 
#  
from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.bitcoin import BtcConverter

c = CurrencyRates()
btnCvr = CurrencyCodes()
print('1$ equvalent to ', end='')
print(btnCvr.get_symbol("EUR"), end='') # print symbol of currency 
print(c.get_rate("USD", 'EUR')) # print the rate of currency 


print('20$ is equvalent to ', end='')
print(btnCvr.get_symbol("INR"), end='')
print(c.convert("USD", "INR", 20))

# for bitcoin
b = BtcConverter()
print(btnCvr.get_symbol("BTC"), end='')
print("1 is equvalent to ", end='')
print(btnCvr.get_symbol("INR"), end='')
print(b.get_latest_price("INR")) # print the latest INR rate of BTC