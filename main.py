from bs4 import BeautifulSoup
import requests
desired_list = []
start = 9099326190
end = 9099326295
for i in range(start,end):
    try:
        url = f"https://www.roblox.com/games/{i}"
        page = requests.get(url)
        print(url)
        pagecontents = page.content
        soup = BeautifulSoup(pagecontents, 'html.parser')
        line = soup.find("h1", class_ = 'game-name')
        if line:
            # print(line)
            game_title = line.text.strip()
            game_title = game_title.upper()
            if "PLACE" in game_title:
                continue
            else:
                print("VALID",url)
                desired_list.append(str(url))
        else:
            continue
    except Exception as e:
        print("Error",e)

print("desired list is ", desired_list)
with open('result.txt', 'a') as results:
    for url in desired_list:
        results.write(url + '\n')
