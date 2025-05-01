# import requests library
import requests
# import beautifulSoup4
import bs4

# URL Test : https://en.wikipedia.org/wiki/Python_(programming_language)
#url = "https://en.wikipedia.org/wiki/Python_(programming_language)"


# # Get request responses
# re = requests.get(url)
#
# # Read html with beautifulSoup4
# container = bs4.BeautifulSoup(re.text, "html.parser")
#
# print("Title page:", container.title.text)
# print("Special class:", container.find("div", class_="mw-heading mw-heading2")
#       .css.select("h2")[0].get_text())
#
# print("Link Pic:", container.find("img",
#                                   class_="mw-file-element").attrs.get("src"))


class HTML:
    def __init__(self, get_url):
        self.url = requests.get(get_url)
        self.container = bs4.BeautifulSoup(self.url.text, "html.parser")

    def get_all_header(self):
        all_header = self.container.find_all("div", class_="mw-heading "
                                                           "mw-heading2")
        return all_header

    def get_all_img(self):
        all_img = self.container.find_all("img")
        return all_img

    def title(self):
        tle = self.container.title.text
        return tle

url = input("Enter URL: ")

html = HTML(url)

print(html.title())
print(html.get_all_header())
print(html.get_all_img())