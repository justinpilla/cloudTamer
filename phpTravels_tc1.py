import datetime
import time

from selenium import webdriver

class phpTravels_tc1:



    # main function
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
        #get method to launch the URL
        driver.get("https://www.phptravels.net/home")

        def fill(element, text):
            element.send_keys(text)

        hotels_Tab = driver.find_element_by_xpath("//*[@id=\"search\"]/div/div/div/div/div/nav/ul/li[1]/a")
        destination_textbox_1 = driver.find_elements_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[1]/div/div[2]/div/a/span[1]")
        destination_textbox_input = driver.find_element_by_css_selector('input.select2-input')

        hotels_Tab.click()
        destination_textbox_1[0].click()
        fill(destination_textbox_input, "Alzer Hotel Istanbul")

        time.sleep(1)

        hotel_result = driver.find_element_by_xpath("/html/body/div[6]/ul/li/ul/li/div")
        time.sleep(1)
        hotel_result.click()

        checkin = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[2]/div/div/div[1]/div/div[2]/input")
        checkin.clear()

        dt = datetime.datetime.today()
        todaysDate = dt.strftime("%d/%m/%Y")
        todaysDate2 = dt.strptime(todaysDate, "%d/%m/%Y")
        fill(checkin, todaysDate)

        checkoutDateDelta = datetime.timedelta(days=7)
        checkoutDate = todaysDate2 + checkoutDateDelta

        checkout = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[2]/div/div/div[2]/div/div[2]/input")
        checkout.clear()

        fill(checkout, checkoutDate.strftime("%d/%m/%Y"))

        childButton = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div[2]/div/span/button[1]")
        childButton.click()
        childButton.click()

        time.sleep(5)
        submitButton = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[4]/button")
        submitButton.click()

        time.sleep(5)

        driver.quit()

        return





