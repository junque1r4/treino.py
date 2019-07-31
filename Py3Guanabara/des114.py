import requests


try:
    requests.get('http://www.pudim.com.br/')
except:
    print('\033[0;31mNão consegui acessar o pudim... :(\033[m')
else:
    print('\033[0;33mConsegui acessar o site PUDIM! YEEY \033[m')
