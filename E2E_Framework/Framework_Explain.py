""" FRAMEWORK """


"""
    --> is a guideline to be followed while creating test scripts.
    --> BDD, Data driven, Hybrid, Keyword driven, Page object model (Already available)
    --> Base: Basic or crux of the code is available. (Browser)
            : Common files
            : Util files (Any misilienious activity)
            
    --> Configuration Data: Locators (Identifying individual web elements uniquely)
                        : ID, NAME, CLASS, CSS-SELECTOR, XPATH, LINK TEXT, PARTIALLINKTEXT, TAGNAME
                          FATEST locator(ID). Lowest locator(XPATH)
                        : Property file
                        : Test Images
                        : Excel files
                        : CSV files
    --> Pages   : Each and every page
                : Whatever action we need to perform on the respective page, we add a function in that page file.
                : A --> 10 actions, B --> 5 actions
                : pageA.py and pageB.py
                : Use? -->
    --> Test Cases : We write all the test cases
                    : Linking different module happens here
                    :This is the starting point of the framework
    --> Reports     : The reports of the execution should be stored here
                    : It contains different screenshots, video recording etc.
                    

                        
                        : ***POM.xml vs maven***

"""

"""
TESTING FRAMEWORK       :  PYTEST

1. Installing framework : pip install pytest
PYTEST RULES
    1. The files starting from test_* | *_test will be only considered for test cases
    2. The functions or test cases starting from test_* | *_test will be only considered for test cases
    3. The classes starting from test_* | *_test be only considered for test cases
    
We want to get more information about the test cases : pytest -v Pytest (v- verbosity (more informative)
Can we single single file : pytest Pytest/file1_test.py -v (pytest <foldername>/<fileName.py> -v)
can we run particular TC    : PYTEST <TC_Location>

1. PYTEST/test1
2. DIR1/test2
3. DIR2/test3
4. DIR3/test4

Can we run one particular test case pytest <TC_Location> -v -k  great (-k : it is included substring)
eg: pytest Pytest -v -k great

"""
