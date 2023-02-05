# WebAutomation

1. Download ```chromedriver``` and make sure is the same version of your Chrome browser
2. To be able to inspect elements and use Xpath add ```ChroPath```extension to your Chrome
3. In `Tests/test_config.py` file make sure ```browser``` variable is showing right path to chromedriver
4. Navigate to ```Test``` folder
5. Install all dependencies ```pip install -r requirements.txt``` 
6. To tun the tests and generate html report:
```pytest --html=report.html test_Login.py ```
# Note
In Pages folder are  located all the elements for specific page ex:
```HomePage.py```, ```LoginPage.py``` if you want to add locators for new pagepleas add ```new file```
in Pages folderwith the locators

- Test will generate ```report.html``` file, copy file path and insert into browser to see the test 
results
- Currently is saving ```screenshots``` on each step executed, NOT implemented yet to add screenshots 
to the report.

---
- To freeze your dependencies use this command ```pip3 freeze > requirements.txt ```