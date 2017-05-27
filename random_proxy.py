import random


def random_proxy():

    proxy_list = [{"http": "http://223.19.212.30:80", "https": "http://223.19.212.30:80"}, {"http": "http://1.179.185.249:8080", "https": "http://1.179.185.249:8080"}]

    return random.choice(proxy_list)
