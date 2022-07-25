import webbrowser
import requests

print("Let's find an old website.")
site = input("Type a website URL: ")
era = input("Type a year, month, and day, like 20150613")
url = f"http://archive.org/wayback/available?url{site}&timestamp={era}"
response = requests(url)
data = response.json()
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print(f"Found this copy: {old_site}.")
    print("It should appear in your browser now.")
    webbrowser.open(old_site)
except:
    print(f"Sorry, no luck finding {site}.")