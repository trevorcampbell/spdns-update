import requests
import json

#load config file
print('Loading SecurePointDNS config')
f = open('spdns-config.conf', 'r')
conf = f.readline()
f.close()
toks = conf.split(' ')

print('Retrieving external IP address')
resp = requests.get('http://checkip.spdyn.de/json')
ip = resp.json()['ipinfo'][0]['ip']
print('IP: ' + str(ip))

print('Updating SecurePointDNS with hostname ' + str(toks[0]) + ', token ' + str(toks[1]))
data = {'hostname': toks[0], 'myip': ip}
resp =  requests.get('https://update.spdyn.de/nic/update', params=data, auth=(toks[0], toks[1]))

rescodes ={'abuse': 'The host is locked because of too many failed attempts.', 
         'badauth':, 'The given username / token was not accepted',
         '!yours': 'The host could not be managed by your account',
         'nochg': 'Your IP has not changed since the last update',
         'good': 'IP of ' +toks[0] +' was updated to ' + ip,
         'notfqdn': 'The host is not an FQDN',
         'nohost': 'The host does not exist or was deleted',
         'fatal': 'The host was manually deactivated'}

print('Response: ' + rescodes[resp.text] if resp.text in rescodes else 'Unknown response, ' + resp.text)

