import requests

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/8ee18d7ec9d5378c83f07bd7/latest/USD'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print (data['conversion_rates'])