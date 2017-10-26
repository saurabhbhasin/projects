import requests

key = 'MW9S-E7SL-26DU-VV8V'
t_count = 'http://api.bart.gov/api/bsa.aspx?cmd=count&key=%s&json=y' % key
get_count = requests.get(t_count)
response = get_count.json()
print(response['root']['traincount'] + ' active BART trains at '
      + response['root']['time'])

sa = 'http://api.bart.gov/api/bsa.aspx?cmd=bsa&key=%s&json=y' % key
get_sa = requests.get(sa)
response = get_sa.json()

print(response['root']['bsa'][0]['description']['#cdata-section'])