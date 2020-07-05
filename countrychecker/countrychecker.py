import requests


class Country:
    def __init__(self, host_url: str = None, api_key: str = None):
        self.host_url = host_url
        self.api_key = api_key
        global headers
        headers = {'x-rapidapi-host': host_url,
                   'x-rapidapi-key': api_key
                   }

    def search_by_country_code(self, country_code):
        try:
            url = "https://restcountries-v1.p.rapidapi.com/alpha/{}".format(country_code)
            response = requests.get(url, headers=headers)
            result = response.json()
            name = result['name']
            capital = result['capital']
            region = result['region']
            languages = result['languages']
            population = result['population']
            currencies = result['currencies']
            print("{}:".format(name))
            print(" Capital: {}".format(capital))
            print(" Region: {}".format(region))
            print(" Languages: {}".format(languages))
            print(" Population: {}".format(str(population)))
            print(" Currencies: {}".format(currencies))
        except:
            print("Invalid country code")


    def search_by_currency(self, currency):
        try:
            url = "https://restcountries-v1.p.rapidapi.com/currency/{}".format(currency)
            response = requests.get(url, headers=headers)
            result = response.json()
            count = len(result)
            print("There are {} countries corresponding to your search:".format(count))
            for i in result:
                print(i['name'])
        except:
            print("Incorrect currency code")

    def search_by_language(self, language):
        try:
            url = "https://restcountries-v1.p.rapidapi.com/lang/{}".format(language)
            response = requests.get(url, headers=headers)
            result = response.json()
            count = len(result)
            print("There are {} countries corresponding to your search:".format(count))
            for i in result:
                print(i['name'])
        except:
            print("Incorrect language code")

    def search_by_region(self, region):
        try:
            url = "https://restcountries-v1.p.rapidapi.com/region/{}".format(region)
            response = requests.get(url, headers=headers)
            result = response.json()
            count = len(result)
            print("There are {} countries corresponding to your search:".format(count))
            for i in result:
                print(i['name'])
        except:
            print("Incorrect region")

    def search_by_capital(self, capital):
        try:
            url = "https://restcountries-v1.p.rapidapi.com/capital/{}".format(capital)
            response = requests.get(url, headers=headers)
            result = response.json()
            print("The country with the capital {}:".format(capital))
            for i in result:
                print(i['name'])
        except:
            print("Incorrect capital")

    def search_by_country_name(self, countryname):
        try:
            url = "https://restcountries-v1.p.rapidapi.com/name/{}".format(countryname)
            response = requests.get(url, headers=headers)
            result = response.json()
            for i in result:
                print("{}:".format(i['name']))
                print(" Capital: {}".format(i['capital']))
                print(" Region: {}".format(i['region']))
                print(" Population: {}".format(i['population']))
                print(" Language: {}".format(i['languages']))
                print(" Currencies: {}".format(i['currencies']))

        except:
            print("Invalid country name")
