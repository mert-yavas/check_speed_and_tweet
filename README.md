# Speed Checker
## Overview
Hello, I'm Mert, and today marks Day 50-51 of my "100 Days of Python" challenge. Welcome to the Speed Checker project. In this project, we've developed a Python script that measures internet speed using Speedtest.net and tweets the results to your internet service provider (ISP) if the speed is below the promised values.

## Project Description
The script utilizes Selenium to automate the process of conducting a speed test on Speedtest.net and posting the results on Twitter. It logs into your Twitter account, performs a speed test, and tweets at your ISP if the internet speed falls below the promised values.

## How to Run
To use the Speed Checker script, follow these steps:

* Ensure Python is installed on your system.
* Install the Selenium library using pip:
```bash
pip install selenium
```

* Download the Chrome WebDriver compatible with your Chrome browser version and place it in the project directory.
* Open the Python script: main.py.
* Customize the script by providing your Twitter credentials (email and password), and your Twitter profile name.
* Run the script:
```bash
python main.py
```
* Sit back and let the script automate the speed testing and tweeting process.
## Project Files
* main.py: The main Python script for conducting speed tests and tweeting the results.
## Customization
Feel free to customize the script by adjusting parameters such as the promised download and upload speeds, or the timeout intervals for better performance.

## Dependencies
The project relies on the following Python libraries:

* selenium: For automating web browser interactions.
* time: For managing timeouts and delays.
## Educational Insights
Through this project, you can gain insights into the following:

* Web Automation: Learn how to automate web browser interactions using Selenium.
* Speed Testing: Understand how to conduct internet speed tests using Speedtest.net.
* Twitter Automation: Implement automation for tweeting results on Twitter.
* Script Optimization: Explore techniques to optimize script performance and efficiency.
## Conclusion
We hope you find the Speed Checker script useful in monitoring your internet speed and communicating with your ISP. Feel free to explore, modify, and adapt the script to suit your specific needs. Happy browsing!
