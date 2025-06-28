import requests
import webbrowser
import colorama
from colorama import Fore, init

init(autoreset=True)

print(Fore.RED + "GEOLOCATER MADE BY @REDSIMIT")
ip = input(Fore.GREEN + "Enter IP Address: ")

def track_ip(ip):
    url = f"https://ipapi.co/{ip}/json/"
    response = requests.get(url)
    data = response.json()

    network = data.get("network")
    version = data.get("version")
    city = data.get("city")
    country = data.get("country")
    country_name = data.get("country_name")
    country_code = data.get("country_code")
    postal = data.get("postal")
    timezone = data.get("timezone")
    asn = data.get("asn")
    languages = data.get("languages")
    country_capital = data.get("country_capital")
    country_area = data.get("country_area")

    longitude = data.get("longitude")
    latitude = data.get("latitude")

    print(Fore.GREEN + "Network: " + network)
    print(Fore.GREEN + "Version: " + version)
    print(Fore.GREEN + "City: " + city)
    print(Fore.GREEN + "Country: " + country)
    print(Fore.GREEN + "Country_name: " + country_name)
    print(Fore.GREEN + "Country_code: " + country_code)
    print(Fore.GREEN + "Country_capital: " + country_capital)
    print(Fore.GREEN + "Postal Code: " + postal)
    print(Fore.GREEN + "Timezone: " + timezone)
    print(Fore.GREEN + "ASN: " + asn)
    print(Fore.GREEN + "Languages: " + languages)
    print(Fore.GREEN + "Country_area: " + str(country_area))

    print(Fore.GREEN + "Longitude: " + str(longitude))
    print(Fore.GREEN + "Latitude: " + str(latitude))
    print(Fore.GREEN + f"https://www.google.com/maps?q={latitude},{longitude}")
    webbrowser.open(f"https://www.google.com/maps?q={latitude},{longitude}")

# Call the function
track_ip(ip)
