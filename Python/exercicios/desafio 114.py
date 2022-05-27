import requests
resp = requests.get('http://www.pudim.com.br/')
if resp.status_code == 200:
    print('O site esta fncionando normalmente')
else:
    print('O site está off')
print(resp.reason)
print('='*30)
print(resp.history)
print('='*30)
print(resp.headers['Server'])
print('='*30)
print(resp.cookies)
print('='*30)
print(resp.elapsed)
print('='*30)
print(resp.text)
print('='*30)
print(resp.encoding)
