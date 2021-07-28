import time


from selenium import webdriver

class phpTravels_tc4:


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


        hotels_Tab = driver.find_element_by_xpath("//*[@id=\"search\"]/div/div/div/div/div/nav/ul/li[1]/a")
        flights_Tab = driver.find_element_by_xpath("//*[@id=\"search\"]/div/div/div/div/div/nav/ul/li[2]/a")
        boats_Tab = driver.find_element_by_xpath("//*[@id=\"search\"]/div/div/div/div/div/nav/ul/li[3]/a")
        rentals_Tab = driver.find_element_by_xpath("//*[@id=\"search\"]/div/div/div/div/div/nav/ul/li[4]/a")
        tours_Tab = driver.find_element_by_xpath("//*[@id=\"search\"]/div/div/div/div/div/nav/ul/li[5]/a")
        cars_Tab = driver.find_element_by_xpath("//*[@id=\"search\"]/div/div/div/div/div/nav/ul/li[6]/a")
        visa_Tab = driver.find_element_by_xpath("//*[@id=\"search\"]/div/div/div/div/div/nav/ul/li[7]/a")

        search1 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[4]/button")
        search2 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[3]/div[4]/button")
        search3 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[3]/div/div/form/div/div/div[4]/button")
        search4 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[4]/div/div/form/div/div/div[4]/button")
        search5 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[5]/div/div/form/div/div/div[4]/button")
        search6 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[6]/div/div/form/div/div/div[5]/button")
        search7 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[7]/div/div/form/div/div/div[4]/button")

        tabsList = [hotels_Tab, flights_Tab, boats_Tab, rentals_Tab, tours_Tab, cars_Tab, visa_Tab]
        searchBtnList = [search1, search2, search3, search4, search5, search6, search7]

        for i in range(7):
            tabsList[i].click()
            time.sleep(1)
            assert searchBtnList[i].is_displayed() == True

        time.sleep(5)

        driver.quit()

        return

