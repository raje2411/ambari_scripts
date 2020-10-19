#####Tested on !/usr/bin/env python3.7 and python2.7 with bs4 package installed through pip
import sys
from bs4 import BeautifulSoup as soup
import pandas as pd

# Read the html file and pull differences
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r') as file :
    page_soup = soup(file, "html.parser")

HTML_data = page_soup.find_all("tr")
# print(HTML_data)
list_header = []
data = []
for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
    data.append(sub_data)
dataFrame = pd.DataFrame(data = data)
dataFrame.to_csv(output_file,header=False,index=False)
