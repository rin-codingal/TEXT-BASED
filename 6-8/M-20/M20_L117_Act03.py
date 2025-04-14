country_code = {'India' : '0091',
                'Australia' : '0025',
                'Indonesia' : '0062'}
 
# search dictionary for country code of India
print("Country code for Indonesia -")
print(country_code.get('Indonesia', 'Not Found'))

print()
 
# search dictionary for country code of Japan
print("Country code for Japan -")
print(country_code.get('Japan', 'Not Found'))