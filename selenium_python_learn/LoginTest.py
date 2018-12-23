from selenium import webdriver

class logintest:
        dr=webdriver.Chrome("C:\\SELENIUM\\chromedriver_win32\\chromedriver.exe")
        dr.get("http://127.0.0.1/orangehrm-3.3.1/symfony/web/index.php/auth/login")
        username=dr.find_element_by_id("txtUsername")
        username.send_keys("ADMIN")
        password=dr.find_element_by_id("txtPassword")
        password.send_keys("ADMIN")
        loginButton=dr.find_element_by_id("btnLogin")
        loginButton.click()
dr.quit()
