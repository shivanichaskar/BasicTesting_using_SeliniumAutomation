from selenium.webdriver import Chrome

def before_scenario(context, scenario):
    path = "D:\\chromedriver_win32\\chromedriver.exe"
    context.driver = Chrome(executable_path=path)

def after_scenario(context, scenario):
    context.driver.close()