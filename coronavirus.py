from bs4 import BeautifulSoup
import requests
from colorama import Fore

response = requests.get('https://стопкоронавирус.рф/')
soup = BeautifulSoup(response.text, 'html.parser')
data = soup.find_all('div', {'class': 'cv-countdown__item-value'})

cases = data[1].text
last = data[2].text
well = data[3].text
deaths = data[4].text
tests = data[0].text

print(Fore.BLUE + 'Подтверждено случаев: ' + str(cases))
print(Fore.CYAN + 'За последние сутки: ' + str(last))
print(Fore.YELLOW + 'Выздоровело: ' + str(well))
print(Fore.RED + 'Умерло: ' + str(deaths))
print(Fore.WHITE + 'Проведено тестов: ' + str(tests))