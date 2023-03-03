import re
import requests
import requests_cache
from bs4 import BeautifulSoup

saved_links = []

def search(keyword, url, depth):
  requests_cache.install_cache('url_cache') 
  response = requests.get(url)

  soup = BeautifulSoup(response.text, 'html.parser') 
  find_keyword = soup.find_all(string=re.compile(keyword))
  
  print(" ")
  print("Nível 0")
  print(" ")
  print("----- ", url, " -----")
  
  if(search_keyword == []):
    print("O termo não foi encontrado aqui.")
    print(" ")
  else:
    for result in find_keyword:
      start_keyword = re.search(keyword, result).start()
      end_keyword = re.search(keyword, result).end()
      if start_keyword <= 19:
        print(word[0 : end_keyword + 20])
      else:
        print(word[start_keyword - 20 : end_keyword + 20])
      print(" ")
  
  links = soup.find_all('a')
  save_links = []
  for link in links:
    try:
      if(re.search('https://', link.get('href')) != None):
        save_links.append(link.get('href'))
    except TypeError:
      continue
  saved_links.append(save_links)
    
  if(depth >= 1):
    counter = 0
    
    while (counter + 1 <= depth):
      print("Nível ", counter + 1)
      print(" ")
      for saved_link in saved_links[counter]:
        print("----- ", saved_link, " -----")
        requests_cache.install_cache('url_cache')
        response = requests.get(saved_link)

        soup = BeautifulSoup(response.text, 'html.parser')
        find_keyword = soup.find_all(string=re.compile(keyword))

        if(find_keyword == []):
          print("O termo não foi encontrado aqui.")
          print(" ")
        else:
          for result in find_keyword:
            start_keyword = re.search(keyword, result).start()
            end_keyword = re.search(keyword, result).end()
            if start_keyword <= 19:
              print(word[0 : end_keyword + 20])
            else:
              print(word[start_keyword - 20 : end_keyword + 20])
          print(" ")
          
          try:
            links = soup.find_all('a')
            save_links = []
            for link in links:
              if(re.search('https://', link.get('href')) != None):
                save_links.append(link.get('href'))
            saved_links.append(save_links)
          except TypeError:
            continue

      counter = counter + 1