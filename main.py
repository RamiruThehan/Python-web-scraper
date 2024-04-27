from bs4 import BeautifulSoup
import requests

url = 'https://www.booking.com/searchresults.html?ss=London&ssne=London&ssne_untouched=London&label=gog235jc-1DCAEoggI46AdICVgDaFCIAQGYAQm4ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArDuuaEGwAIB0gIkZmJhYjE4YzAtNDdhMy00MmY1LTk2NWItN2UzOTgyNTk1OWEx2AIE4AIB&aid=397594&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-2601889&dest_type=city&checkin=2023-05-06&checkout=2023-05-07&ltfd=6%3A1%3A5-2023%3A&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&selected_currency=USD&soz=1&lang_changed=1'

headers = {
    'User-Agent':
    'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
hotels = soup.findAll('div', {'data-testid': 'property-card'})

hotels_data = []

for hotel in hotels:
  name_element = hotel.find('div', {'data-testid': 'title'})
  name = name_element.text.strip()

  location_element = hotel.find('span', {'data-testid': 'address'})
  location = location_element.text.strip()

  price_element = hotel.find('span',
                             {'data-testid': 'price-and-discounted-price'})
  price = price_element.text.strip() if price_element is not None else 'N/A'

  rating_element = hotel.find('div', {'class': 'b5cd09854e d10a6220b4'})
  rating = rating_element.text.strip() if rating_element is not None else 'N/A'

  hotels_data.append({
      'name': name,
      'location': location,
      'price': price,
      'rating': rating
  })

print("Hotel Data Scraper")
print("\n")
loc = input("Enter your location: ")
bud = input("Enter your budget in Rupees: ")
print("\n")
print(hotels_data)