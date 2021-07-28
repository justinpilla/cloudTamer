import time


from selenium import webdriver


class phpTravels_tc3:


    def automationRunner(self, _browser, path):

        if _browser == "chrome" and path == "":
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(chrome_options=options)
        elif _browser == "chrome" and path != "":
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(executable_path=path, chrome_options=options)
        elif _browser == "firefox":
            drive = webdriver.firefox(executable_path="insert firefox here")

        # to maximize the browser window
        driver.maximize_window()
        # get method to launch the URL
        driver.get("https://www.phptravels.net/home")



        flights_Tab = driver.find_element_by_xpath("//*[@id=\"search\"]/div/div/div/div/div/nav/ul/li[2]/a")
        flights_Tab.click()

        oneWay = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[1]/div[1]/div/div[1]")
        roundTrip = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[1]/div[1]/div/div[2]")
        roundTrip.click()
        returnDate = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[3]/div[2]/div/div/div[2]/div")

        time.sleep(1)
        assert len(returnDate) == 1
        time.sleep(1)
        oneWay.click()
        time.sleep(1)
        returnDate = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[3]/div[2]/div/div/div[2]/div")
        time.sleep(1)
        assert returnDate[0].is_displayed() == False

        time.sleep(5)

        driver.quit()

        return

