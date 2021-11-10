from requests_html import HTMLSession

session = HTMLSession()

r = session.get("https://alpha.art/collection/dape")

r.html.render()

nftd = r.html.find(".grid grid-cols-1 gap-y-10 sm:grid-cols-2 gap-x-6 md:grid-cols-3 xl:grid-cols-4 xl:gap-x-8", first = True)

print(nftd.html)