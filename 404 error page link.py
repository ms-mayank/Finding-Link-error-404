import xlrd
import requests
from bs4 import BeautifulSoup

"""Give the domain of the site
     -For multi instance site: Use CF domain.
     -For single instance site: Use the same domain as URL"""

"""@@ domain- Provide the domain name of the ^^"""
domain = ("https://XYZ-preview.dev.pfizerstatic.io")

"""@@One time change path for destination of result file"""
f = open("D:\\User\\Desktop\\URL_status_result.txt", "w")  # Create file for the result


def errorpg(url):
    try:
        r = requests.get(url)  # Get the HTML
        htmlContent = r.content  # Get the content of the HTML
        soup = BeautifulSoup(htmlContent, "html.parser")  # Parse the HTML
        anchors = soup.find_all("a")  # Get all anchor <a> tags
        helixs = soup.find_all("helix-anchor")  # Get all helix anchor <helix-anchor> tags
        all_helix_links = set()  # Create empty set to store all URL of the page

        # Gather all the <a> links and add in all_helix_links set
        for anchor in anchors:
            anchortext = anchor.get("href")
            if anchortext == None or anchortext[0] == "#":
                continue
            if anchortext[0] == "/":
                anchortext = domain + anchortext
            all_helix_links.add(anchortext)

        # Gather all the <helix-anchors> links and add in all_helix_links set.
        for helix in helixs:
            helixtext = helix.get("href")
            if helixtext == None or helixtext[0] == "#":
                continue
            if helixtext[0] == "/":
                helixtext = domain + helixtext
            all_helix_links.add(helixtext)

        # check Status of all the URLs in all_helix_links set.
        for link in all_helix_links:
            try:
                req = requests.head(link)
                if req.status_code != 200:
                    f.write("\n" + link + "\t" + str(req.status_code))
            except:
                f.write("\n" + link + "\t" + "------> ExCEPTION")
        f.write("\n" + str(len(all_helix_links)) + "\n")
    except:
        f.write("\n" + url + "\t" + "-----> !!OOPs EXCEPTION OCCURED")

"""@@loc -  Provide the location of the excelsheet path which have urls in the firstsheet and first column
NOTE- Only provide Edison lite url, which have ".dev.pfizerstatic.io" in the url
"""
loc = "D:\\User\\Downloads\\Link status.xlsx"  # Location of the excelsheet file
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

for i in range(sheet.nrows):
    urlcheck = sheet.cell_value(i, 0)  # Gathering each URL from the excelsheet
    f.write("\t Page URL = " + urlcheck)  # Printing the URL to indetify the page in file
    errorpg(urlcheck)  # Passing the url to errorpg() function
    f.write("\n ******************************* \n")
f.close()
