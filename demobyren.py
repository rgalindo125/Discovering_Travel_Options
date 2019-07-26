 pip install unirest
    response = requests.post("https://fuelprice.p.mashape.com/",
    headers={
    "X-Mashape-Key": "eqPyWAd3Wrmsh52b6fvG3AQ5T2ygp1KZhDfjsng702Sd7DmWN7",
    "Content-Type": "application/json",
    "Accept": "application/json"
  },
    data={'fuel': 'p', 'state': 'dl'}
)

price = response.json()