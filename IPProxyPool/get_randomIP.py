import requests
from random import choice



def get_random_ip():#随机取50个http代理 随机取一个
        response = requests.get('http://127.0.0.1:8000/?count=50&protocol=0').text
        IP_list=eval(response)
        IP =choice(IP_list)
        ip='http://'+str(IP[0])+':'+str(IP[1])
        return ip



if __name__ == '__main__':
    print(get_random_ip())