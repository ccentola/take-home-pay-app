import requests
import config

salary = int(input('Enter you annual salary: ' ))    # annual salary
pay_periods = 26                                     # n pay periods
pay_rate = round((salary / pay_periods),2)           # calculate gross paycheck
year = 2019                                          # set to year

url = f'https://taxee.io/api/v2/calculate/{year}'

# query parameters
# need to hide auth
headers = {
    'Authorization': config.AUTHORIZATION,
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
  'state': 'AZ',
  'filing_status': 'single',
  'pay_periods': pay_periods,
  'pay_rate': pay_rate,
  'exemptions': '1'
}

r = requests.post(url, headers=headers, data=data)

result = r.json()

state = result['per_pay_period']['state']['amount']
federal = result['per_pay_period']['federal']['amount']
fica = result['per_pay_period']['fica']['amount']

taxes = state + federal + fica

print(round(pay_rate - taxes, 2))