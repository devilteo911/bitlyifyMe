import itertools


def driver_options(webdriver):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
    options.add_argument("--log-level=3")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return options

def split_multi_link(in_str: str) -> list:
    in_str = string_normalizer(in_str)
    in_str = in_str.split(" ")
    in_str = list(filter(None, in_str))
    return in_str

def string_normalizer(str_: str) -> str:
    banned_char = ",;/'#@"
    for bc in banned_char:
        str_ = str_.replace(bc, " ")
    return str_