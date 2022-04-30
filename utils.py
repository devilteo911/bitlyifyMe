def driver_options(webdriver):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
    options.add_argument("--log-level=3")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return options