import requests
import sys
import os
# from .classmodule import MyClass
# from .funcmodule import my_function
from bs4 import BeautifulSoup

import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
if (os.environ.get("CLICOLOR") is None):
    CLICOLOR = True
else:
    CLICOLOR = os.environ.get("CLICOLOR") == "1" or os.environ.get("CLICOLOR") == 1

def main():
    # support colored print statements
    noColor = '\033[0m'
    redColor = '\033[91m'
    greenColor = '\033[92m'
    dgrayColor = '\033[90m'
    purpleColor = '\033[95m'
    args = sys.argv[1:]
    ## support help
    if len(args) < 1:
        print("HenZCLI tool is used for checking healthy links in HTML file")
        print("Basic usage as follow\n")
        print("\thenzcli <path to html file> <another file>\n")
    else:
        ## support link list flag, bad code :(
        onlyGood = onlyBad = None
        allIncluded= True
        if (args[0] == "--good"):
            onlyGood = True
            allIncluded = False
        if (args[0] == "--bad"):
            onlyBad = True
            allIncluded = False
        if (args[0] == "--all"):
            allIncluded = True
        ## support version check
        if (args[0] == "-v" or args[0] == "--version"):
            print("HenZCLI version 0.1")
        # else:
            # print('count of args :: {}'.format(len(args)))  
        print('passed argument :: {}'.format(args))
            # goodList = []
            # badList = []
            # unknownList = []
            ## support multiple files as arguments
        for arg in args:
            if (arg[0] != "-"):
                try: 
                    f = open(arg, "r")
                    if (CLICOLOR):
                        print(purpleColor +  "In file " + arg + noColor)
                    else:
                        print("In file " + arg)
                    # parse html file
                    html = BeautifulSoup(f, 'html.parser')
                    # look for all link in a tags
                    for link in html.find_all('a'):
                        URL = link.get('href').strip()
                        try:
                            # test links
                            requestObj = requests.get(URL)
                            if ((onlyBad or allIncluded) and requestObj.status_code == 404 or requestObj.status_code == 401):
                                if (CLICOLOR):
                                    print(redColor + "Bad link " + URL + noColor)                                    
                                else:
                                    print("Bad link " + URL)
                                # print(redColor + "Bad link " + URL + noColor)
                                # badList.append(URL)
                            elif ((onlyGood or allIncluded) and requestObj.status_code == 200):
                                if (CLICOLOR):
                                    print(greenColor + "Good link " + URL + noColor)
                                else:
                                    print("Good link " + URL)
                                # print(greenColor + "Good link " + URL + noColor)
                                # goodList.append(URL)
                            else:
                                if (allIncluded):
                                    if (CLICOLOR):
                                        print(dgrayColor + "Unknown "+ URL + noColor)
                                    else:
                                        print("Unknown "+ URL)
                                    # print(dgrayColor + "Unknown "+ URL + noColor)
                                    # unknownList.append(URL)
                        except:
                            if (allIncluded):
                                if (CLICOLOR):
                                    print(dgrayColor + "Unknown "+ URL + noColor)
                                else:
                                    print("Unknown "+ URL)
                                # print(dgrayColor + "Unknown "+ URL + noColor)
                                # unknownList.append(URL)
                except:
                    print(dgrayColor + "Unable to open file " + arg)
                # for link in goodList:
                # for link in badList:
                # for link in unknownList:

if __name__ == '__main__':
    main()