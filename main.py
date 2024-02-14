from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set the promised internet speed from your provider
PROMISED_DOWN = 30  # you can change download and upload speed values
PROMISED_UP = 5

# Enter your Twitter credentials
TWITTER_EMAIL = "YOUR EMAIL"
TWITTER_PASSWORD = "YOUR PASSWORD"

# Enter your Twitter profile name
NAME = "YOUR PROFILE NAME"


class InternetSpeedTwitterBot:
    def __init__(self):
        # Configure Chrome options to keep the browser open
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", value=True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.upload = 0
        self.download = 0

    # Method to get the internet speed using Speedtest.net
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # Click on the speed test button
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()
        time.sleep(60)

        # Get the download and upload speeds
        self.download = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.upload = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    # Method to tweet at the internet service provider
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")

        # Click on the sign-in link
        time.sleep(5)
        sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        sign_in.click()

        # Enter email and proceed to the next step
        time.sleep(5)
        enter_email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        enter_email.send_keys(TWITTER_EMAIL)
        forward_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        forward_button.click()
        time.sleep(3)

        # Enter username and proceed to the next step
        enter_user_name = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        enter_user_name.send_keys(NAME)
        username_forward_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
        username_forward_button.click()
        time.sleep(5)

        # Enter password and login
        enter_password = self.driver.find_element(By.NAME, value='password')
        enter_password.send_keys(TWITTER_PASSWORD)
        login_button_xpath = '//div[@data-testid="LoginForm_Login_Button"]'
        login = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, login_button_xpath))
        )
        login.click()

        # Compose the tweet with internet speed information and post
        time.sleep(5)
        write_tweet = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.download}down/{self.upload}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        write_tweet.send_keys(tweet)
        time.sleep(1)

        # Click on the post button to publish the tweet
        post_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span')
        post_button.click()


# Instantiate the InternetSpeedTwitterBot class
speed = InternetSpeedTwitterBot()
# Call the methods to get the internet speed and tweet at the provider
speed.get_internet_speed()
speed.tweet_at_provider()
