Prerequisites for running the code:
1.	Make sure Python version 2.7 is installed
2.	Beautiful Soup package “beautifulsoup4” is installed
	a. To install Beautiful Soup package please follow the url: https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup
3.	urllib2 package in python is installed

----------------------------------------------------------------------------------------

How to run the code?

For Task1:

Please run the following command in command prompt for task1 in the source code folder
"python Task1.py"

Example:
"c:\WebCrawlerSource>python Task1.py"

This will generate a text file named "TASK1.txt" in the same folder of the source code. 
This file will contain the list of 1000 unique urls crawled for Task1.

----------------------------------------------------------------------------------------
For Task2:

Please run the following command in command prompt for task2 in the source code folder
'python Task2.py <<input-seed-url>> <<input-keyword>>" '
where:
input-seed-url = is the seed url which can be specified in command line as input
input-keyword = is the keyword for focused crawling

The program will run for this two inputs and perform focused crawling

If the inputs are not provided, the program will display a message informing the user to give a input.

Example:
'c:\WebCrawlerSource>python Task2.py "https://en.wikipedia.org/wiki/Sustainable_energy" "solar" '

This will generate two text files named "TASK2-A.txt" and "TASK2-B.txt" in the same folder of the source code. 
File "TASK2-A.txt" will contain the list of urls crawled using Breadth first crawling approach.
File "TASK2-B.txt" will contain the list of urls crawled using Depth first crawling approach.

----------------------------------------------------------------------------------------
For Task3:

Please run the following command for task3
"python Task3.py"

Example:
"c:\WebCrawlerSource>python Task3.py"

This will generate a text file named "TASK3.txt" in the same folder of the source code. 
This file will contain the list of 1000 unique urls crawled for Task3.
----------------------------------------------------------------------------------------