#####Tested on !/usr/bin/env python3.7 and python2.7 with bs4 package installed through pip
import sys
from bs4 import BeautifulSoup as soup

# Read the html file and pull differences
input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file, 'r') as file :
    page_soup = soup(file, "html.parser")
differences = page_soup.findAll("td", {"class" : "highlight"})

# html_style to print with color coding
html_style = '''<style>
div {
    padding: 0px 20px 20px 20px;
}
h1,h2,h3,h4,h5,h6 {
    font-family: Georgia, Georgia, serif;;
}
a {
    font-family: Georgia, Georgia, serif;;
}
p {
    font-family: Georgia, Georgia, serif;;
}
th {
    font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;;
    text-align: left;
    color: white;
    background-color: #4CAF50;
    border-bottom: 1px solid #ddd;
    padding: 5px;
}
td {
    font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;;
    padding-left: 5px;
    padding-right: 5px;
    vertical-align: top;
    word-wrap: break-word;
}
td.highlight {
    background-color: #fa9e91;
    border-bottom: 1px solid #ddd;
}
td.exists {
    background-color: #fa9e91;
    border-bottom: 1px solid #ddd;
}
td.dummy {
    background-color: #8CCBA3;
    border-bottom: 1px solid #ddd;
}
td.separator {
    background-color: #4CAF50;
    padding: 1px;
}
table {
    table-layout: fixed;
    border-collapse: collapse;
    border: 1px solid #ddd;
    width: 100%;
    -moz-box-shadow: 0 0 10px #888888
    -webkit-box-shadow: 0 0 10px #888888;
    box-shadow: 0 0 10px #888888
}
tr:nth-child(even) {
    background-color: #f2f2f2
}
</style>'''

# print the difference in HTML format to OUTPUT_File
sys.stdout = open(output_file, 'w')

print("<html>")
print("<head>")
print(html_style)
print("</head>")
print("<body>")
print('<div class="pagePadding">')
print("<table>")
print("<tbody>")
for items in differences :
    print("<tr>")
    print("\n".join([str(item) for item in differences[:3]]))
    del differences[:3]
    print("</tr>")
print("</tbody>")
print("</table>")
print('</div>')
print("</body>")
print("</html>")

sys.stdout.close()
# End of printing to file
