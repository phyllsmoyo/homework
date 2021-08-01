import requests
import sys

resp = requests.get(f'https://wttr.in/{sys.argv[1].replace(" ", "+")}')
print(resp.text)
