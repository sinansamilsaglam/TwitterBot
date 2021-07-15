from typing import NoReturn
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = "YOUR USERNAME"
password = "YOUR PASSWORD"


class Twitter:

    def __init__(self, username, password):
        
        self.browser = webdriver.Chrome(
            "YOUR WEB DRİVER PATH")
        self.username = username
        self.password = password
        self.followings = []
        self.followers = []


    def signIn(self):

        self.browser.get("https://twitter.com/login")
        time.sleep(2)

        self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input").send_keys(self.username)

        self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div").click()

        time.sleep(3)

    def getFollowings(self):
        self.browser.get(f"https://twitter.com/{self.username}")
        time.sleep(2)
        self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div[1]/a").click()
        time.sleep(2)

        #self.followings= []
        followingsList = self.browser.find_elements_by_xpath(
            "//div[@data-testid = 'UserCell']/div[1]/div[2]/div[1]/div[1]")
        time.sleep(1)

        followButton = self.browser.find_element_by_css_selector(
            "div[role=button]")

        for i in followingsList:
            self.followings.append(i.text)

        scrollCounter = 0
        lastHeight = self.browser.execute_script(
            "return document.documentElement.scrollHeight")

        while True:
            self.browser.execute_script(
                "window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(1)

            newHeight = self.browser.execute_script(
                "return document.documentElement.scrollHeight")

            if lastHeight == newHeight:
                break
            lastHeight = newHeight
            scrollCounter += 1

            followingsList = self.browser.find_elements_by_xpath(
                "//div[@data-testid = 'UserCell']/div[1]/div[2]/div[1]/div[1]")

            time.sleep(1)

            for i in followingsList:
                self.followings.append(i.text)

        # print("******* FOLLOWİNGS *******")

        # for item in self.followings:
            
        #     print("*****")
        #     print(item)


    def getFollowers(self):

        time.sleep(2)

        action = webdriver.ActionChains(self.browser)
        action.key_down(Keys.HOME).key_up(Keys.HOME).perform()
        time.sleep(2)

        self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[1]/a").click()
        time.sleep(2)

        #followers = []
        followersList = self.browser.find_elements_by_xpath(
            "//div[@data-testid = 'UserCell']/div[1]/div[2]/div[1]/div[1]")
        time.sleep(1)

        for i in followersList:
            self.followers.append(i.text)

        scrollCounter = 0
        lastHeight = self.browser.execute_script(
            "return document.documentElement.scrollHeight")

        while True:
            self.browser.execute_script(
                "window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(1)

            newHeight = self.browser.execute_script(
                "return document.documentElement.scrollHeight")

            if lastHeight == newHeight:
                break
            lastHeight = newHeight
            scrollCounter += 1

            followersList = self.browser.find_elements_by_xpath(
                "//div[@data-testid = 'UserCell']/div[1]/div[2]/div[1]/div[1]")

            time.sleep(1)

            for i in followersList:
                self.followers.append(i.text)

        #print("******* FOLLOWERS *******")

        # for item in self.followers:
            
        #     print("*****")
        #     print(item)


    def search(self, hashtag):
        searchInput = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/label/div[2]/div/input")
        searchInput.send_keys(hashtag)

        time.sleep(2)

        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)

        result = []
        list = self.browser.find_elements_by_xpath(
            "//div[@data-testid = 'tweet']/div[2]/div[2]/div[1]")
        time.sleep(2)

        for i in list:
            result.append(i.text)

        scrollCounter = 0
        lastHeight = self.browser.execute_script(
            "return document.documentElement.scrollHeight")

        while True:
            if scrollCounter > 5:
                break
            self.browser.execute_script(
                "window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(2)

            newHeight = self.browser.execute_script(
                "return document.documentElement.scrollHeight")

            if lastHeight == newHeight:
                break
            lastHeight = newHeight
            scrollCounter += 1

            list = self.browser.find_elements_by_xpath(
                "//div[@data-testid = 'tweet']/div[2]/div[2]/div[1]")
            time.sleep(2)

            for i in list:
                result.append(i.text)

        for item in result:
            print("********")
            print(item)


    def compare(self):
        time.sleep(2)

        print("***** YOU FOLLOW EACH OTHER *****")
        for user in self.followings:
            if user in self.followers:
                print("\n" + user)
        
        time.sleep(2)

        print("***** DOESN'T FOLLOW YOU BACK *****")
        for user in self.followings:
            if user != self.followers:
                print("\n" + user)
        

twitter = Twitter(username, password)
twitter.signIn()
# twitter.search("python")
twitter.getFollowings()
twitter.getFollowers()
twitter.compare()
