# henz-cli

osd release 0.1  
A cli tools to check broken links in HTML files

## Installation

   1. install python
   2. to install cli open terminal and run:

    pip3 install -e .

   3. to uninstall run:

    pip3 uninstall henzcli

## Usage

Basic usage:

    henzcli <path to html file> <another path to html file>

Example:

    henzcli .\test\index.html .\test\index2.html

## Features

By default, all good links are printed in green color, bad links are red and broken links are gray.  
You can add environment variable or add variable in .env to override default color setting

    ## in .env
    CLICOLOR = 0 // no color result, default is 1
