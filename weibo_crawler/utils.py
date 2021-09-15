#!/usr/bin/env python3
# -*- coding: utf-8 -*-

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

def get_weibo_cookies():
    url = 'https://login.sina.com.cn/signup/signin.php?entry=sso'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="username"]').clear()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys("1156618076@qq.com")
    driver.find_element_by_xpath('//*[@id="password"]').clear()
    driver.find_element_by_xpath('//*[@id="password"]').send_keys("zhenwoduzun1741!")
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.ENTER)
    time.sleep(10)
    driver.get("https://service.account.weibo.com/index?type=5&status=0&page=1")
    cookies = driver.get_cookies()

    return cookies

def base62_encode(num, alphabet=ALPHABET):
    """Encode a number in Base X

    `num`: The number to encode
    `alphabet`: The alphabet to use for encoding
    """
    if (num == 0):
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def base62_decode(string, alphabet=ALPHABET):
    """Decode a Base X encoded string into the number

    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for encoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num

def url_to_mid(url):
    url = str(url)[::-1]
    size = int(len(url) / 4) if len(url) % 4 == 0 else int(len(url) / 4) + 1
    result = []
    for i in range(size):
        s = url[i * 4: (i + 1) * 4][::-1]
        s = str(base62_decode(str(s)))
        s_len = len(s)
        if i < size - 1 and s_len < 7:
            s = (7 - s_len) * '0' + s
        result.append(s)
    result.reverse()
    return int(''.join(result))


