import requests
import sys
from .classmodule import MyClass
from .funcmodule import my_function
from bs4 import BeautifulSoup

def main():
    ## support colored print statements
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
        print("\thenzcli {path to html file} {another file}\n")
    else:
        ## support version check
        if (args[0] == "v" or args[0] == "version"):
            print("HenZCLI version 0.1")
        else:
            # print('count of args :: {}'.format(len(args)))  
            print('passed argument :: {}'.format(args))
            ## support multiple files as arguments
            for arg in args:
                try: 
                    f = open(arg, "r")
                    print(purpleColor +  "In file " + arg)
                    # parse html file
                    html = BeautifulSoup(f, 'html.parser')
                    # look for all link in a tags
                    for link in html.find_all('a'):
                        URL = link.get('href').strip()
                        try:
                            # test links
                            requestObj = requests.get(URL)
                            if (requestObj.status_code == 404 or requestObj.status_code == 401):
                                print(redColor + "Bad link " + URL + noColor)
                            elif (requestObj.status_code == 200):
                                print(greenColor + "Good link " + URL + noColor)
                            else:
                                print(dgrayColor + "Unknown "+ URL + noColor)
                        except:
                            print(dgrayColor + "Unknown "+ URL + noColor)
                except:
                    print(dgrayColor + "Unable to open file " + arg)

if __name__ == '__main__':
    main()