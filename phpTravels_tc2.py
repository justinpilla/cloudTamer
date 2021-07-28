
import time


from selenium import webdriver



class phpTravels_tc2:

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

        oneWay = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[1]/div[1]/div/div[1]/input")
        roundTrip = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[1]/div[1]/div/div[2]")
        assert oneWay.is_selected() == True
        assert roundTrip.is_selected() == False

        fromLabel = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[3]/div[1]/div/div[1]/div/label")
        toLabel = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[3]/div[1]/div/div[2]/div/label")
        departLabel = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[3]/div[2]/div/div/div[1]/div/label")
        adultsLabel = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[3]/div[3]/div/div/div[1]/div/label")
        childLabel = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[3]/div[3]/div/div/div[2]/div/label")
        infantLabel = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[3]/div[3]/div/div/div[3]/div/label")

        assert len(fromLabel) == 1
        assert len(toLabel) == 1
        assert len(departLabel) == 1
        assert len(adultsLabel) == 1
        assert len(childLabel) == 1
        assert len(infantLabel) == 1

        flightClass = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[1]/div[2]/div/div/a")
        flightClass.click()

        firstClass = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div/div[1]/div[2]/div/div/div/ul/li[1]")
        firstClass.click()

        time.sleep(10)

        driver.quit()

        return
