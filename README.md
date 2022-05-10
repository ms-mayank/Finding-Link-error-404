# Finding-Link-error-404
Find 404 error URLs in the page :

The project Extracts the URLs from an excelsheet and Run the Python script over it, which gathers all the unique URLs from the page and returns their status code in a URL_status_result.txt file if the page have any 404/302 error links.

Library Used:
1. xlrd -  To read Excelsheet
2. requests - To get status of URL
3. BeautifulSoup -  To extract HTML content of page.

Input & Initial configuration:
Line no. 10 : Enter Domain name of the site.
Line no. 13 : Provide the path where URL_status_result.txt gets created.
Line no. 58 : Provide the location of excelsheet.

Excelsheet:
  Keep all the URL in 1st column and in first sheet without adding heading to it.
  
Output:
  A text file with the status code of all the URLs of every page present in excelsheet.
