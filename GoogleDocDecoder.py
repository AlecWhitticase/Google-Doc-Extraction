import requests
from bs4 import BeautifulSoup

def extract(responce):
    parsed = BeautifulSoup(responce, 'html.parser')
    tables = parsed.find_all('table')
    table = tables[0]
    rows = table.find_all('tr')
    coordinates = []
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 3: 
            try:
                x = int(cells[0].get_text(strip=True)) 
                char = cells[1].get_text(strip=True)
                y = int(cells[2].get_text(strip=True))
                coordinates.append((char, x, y))
            except ValueError:
                pass
    return coordinates

def decode(url):
    response = requests.get(url)
    coordinates = extract(response.text)
    grid = [[' ' for _ in range(max(x for _, x, _ in coordinates) + 1)] for _ in range(max(y for _, _, y in coordinates) + 1)]
    for char, x, y in coordinates:
        grid[y][x] = char
    grid.reverse() 
    if grid:
        for row in grid:
            print(''.join(row).rstrip())

decode("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")
decode("https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub")
