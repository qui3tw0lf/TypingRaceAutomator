import time
import random
import pyautogui
from itertools import islice
from selenium import webdriver
from selenium.webdriver import ChromeOptions

def main():
    _options = ChromeOptions()
    _options.debugger_address = '127.0.0.1:9090'
    _driver = webdriver.Chrome(executable_path='./chromedriver', options=_options)
    print(_driver.title)
    
    # for monkeytype.com
    # _driver.execute_script("document.getElementById('wordsWrapper').style.overflow='unset';document.getElementById('words').style.overflow='unset';")
    # _words_ele_list = _driver.find_element_by_id("words")
    # _words = _words_ele_list.text.replace("\n", " ")
    
    # for typeracer.com
    # _elements = _driver.find_elements_by_class_name('gwt-Anchor prompt-button bkgnd-blue')
    _element = _driver.find_elements_by_tag_name("table")
    _text_element = _element[16].find_elements_by_tag_name("tr")[0]
    _words = _text_element.text
    # _words = _element[16].text
    # _element[0.click()
    print(_words)
    print("End")
    setupTyper(_words)
    
def setupTyper(_words):
    # print(_words)
    _iter = iter(_words)
    _len = len(_words)
    _offset = _len % 4
    _size = (_len + _offset) // 7
    print(_len, _size, _size * 7)
    _list = [list(islice(_iter, _size)) for x in range(7)]
    # print(_len, _size, _list)
    _random_intervals = [0.05, 0.06, 0.02, 0.01]
    # _errors_list = [0.04, 0.05, 0.01, 0.08]
    _errors_list = [0, 0, 0, 0]
    # time.sleep(5)
    _list1 = []
    for x in _list:
        _random = random.randint(0, 3)
        _tmp_text = "".join(x)
        _tmp = addErrors(_tmp_text, _errors_list[_random])
        print(_random, "-->", _tmp)
        _list1.append(_tmp)
    time.sleep(2)
    for x in _list1:
        type("".join(x), _random_intervals[_random])
    # print("Total words: %d" % len(_words))
    

def addErrors(_text, _percent):
    _tmp = _text
    # print(_tmp)
    _len = int(len(_text) * _percent)
    for x in range(_len):
        _random = random.randint(0, len(_text) - 1)
        _char = _text[_random]
        if _char != ' ':
            _tmp_char = chr(ord(_char) + 1)
            _tmp_str = list(_tmp)
            # print(_random, _char, _tmp_char)
            _tmp_str[_random] = _tmp_char
            _tmp = "".join(_tmp_str)
    # print(_tmp)
    # print("Len : %d - %d" % (len(_text), _len), _percent)
    return _tmp
    

def type(_text, _int):
    try:
        pyautogui.typewrite(_text, interval=_int)
    except Exception as _error:
        print(_error)
    
    
if __name__ == '__main__':
    main()