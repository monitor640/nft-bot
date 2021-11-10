from requests_html import HTMLSession
#from bs4 import BeautifulSoup
session = HTMLSession()
r=session.get("http://python-requests.org/")
print("0")
r.html.render(sleep=10)
print("1")
r.session.close()
#h3=response.html.find("h3")
#print(h3[0].text)
#print("done")
#soup = BeautifulSoup(page.content, "html.parser")
#print(soup.prettify())
