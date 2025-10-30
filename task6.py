from requests import get, post, put, delete


address = 'http://' + input()
name_key = input()

r = get(address)
dict = r.json()

print(dict.get(name_key, 'No data'))
