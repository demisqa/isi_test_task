## *Description:* 
There is a QA Automation test task for ISI Technology.
____
### Technologies: 
Python 3.11.5

Pytest 7.4.3

Selenium 4.15.2

Webdriver Manager 4.0.1

Python-dotenv 1.0.0

Allure-pytest 2.13.2

____
### How to run:

To run this test project you have to install JAVA on your computer or JAVA should already been installed.
Also, you have to install Allure. For macOS, run the command (make sure Homebrew is installed):

```
brew install allure
```
For others OS follow the instructions on site:

```
https://allurereport.org/docs/gettingstarted-installation/
```

Create a virtual environment and install all requirements from the
file "requirements.txt". You can do it by the commands:

```
python3 -m venv <venv>
```
to create virtual environment, where &lt;venv&gt; is name of your virtual environment;

```
source <venv>/bin/activate
```
to activate your virtual environment;

```
pip3 install -r requirements.txt
```
to install requirements.

I use webdriver-manger from pip3, so you don't need to set a path to your WebDriver.

Also, it's required to do some steps:

1. Create .env file in the root of this project (this file has already been added to .gitignore)
2. Add current code to .env file:

```
USERNAME = ""
PASSWORD = ""
```
and in quotes put your credentials.

For run tests with future allure report generating use the command from the root of project:

```
pytest -s -v ui_tests/test_alerts_page.py --alluredir=allure_results
```
where "allure_results" is a directory for JSON files of the report ("allure_results" has already been added to .gitignore file).

To see the pretty view of the report run the command:

```
allure serve allure_results/ 
```
the pretty view of the report should be open in your browser automatically. If not, check in the terminal, where you wrote the current command, the message should be like this:

```
Server started at <http://192.168.1.178:64361/>
```
but with your link, so copy and open it in the browser.
