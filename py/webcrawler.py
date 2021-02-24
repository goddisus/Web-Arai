import requests
from requests.exceptions import HTTPError
from urllib.parse import urljoin
import os, codecs
from urllib.parse import unquote

headers = {
    'User-Agent': 'Jadesada Dansawatwong 6110503215 Agent 1.0',
    'From': 'jadesada.d@ku.th'
}
#seed_url = "https://www.google.co.th/maps/place/13%C2%B050'56.8%22N+100%C2%B034'15.1%22E/@13.8491111,100.5686724,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x0!8m2!3d13.8491111!4d100.5708611?hl=th"
seed_url = 'http://siamchart.com/stock/'
frontier_q = [seed_url]
visited_q = []
robots_file = []
os.makedirs('robots', 0o755, exist_ok=True)
os.makedirs('sitemap', 0o755, exist_ok=True)

def get_headerpage(url):
    global headers
    text = ''
    try:
        response = requests.head(url, headers=headers, timeout=3)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        #print(response) 
        print(url)
        #print(response.url)
        print(response.status_code)
        #print(response.headers)
        #print(response.is_redirect)
        #print(response.is_permanent_redirect)
        #print(response.url==url)
        #print(response.url)
    except HTTPError as http_err:
        #print(f'HTTP error occurred: {http_err}')  # Python 3.6
        return 'error',False,0
    except Exception as err:
        #print(f'Other error occurred: {err}')  # Python 3.6
        return 'error',False,0
    else:
        #print('Success!')
        text = response.text
        #print(text)
    if 'Content-Type' in response.headers:
        return text.lower(),response.is_redirect,response.headers['Content-Type']
    else :
        return 'error',False,0

def get_page(url):
    global headers
    text = ''
    try:
        response = requests.get(url, headers=headers, timeout=3)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        #print(unquote(response.url))
        print(response.status_code,'hellooooooooooo')
        print(response.is_permanent_redirect)
        print(response.is_redirect)
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
        return 'error',''
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
        return 'error',''
    else:
        print('Success!')
        text = response.text
        #print(text)
    return text.lower(),response.url

def get_robotspage(url):
    global headers
    text = ''
    try:
        response = requests.get(url, headers=headers, timeout=3)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
        text = response.text
        #print(text)
    return text

def link_parser(raw_html,url):
    urls = [];
    pattern_start = '<a href="';  pattern_end = '"'
    index = 0;  length = len(raw_html)
    while index < length:
        start = raw_html.find(pattern_start, index)
        if start > 0:
            start = start + len(pattern_start)
            end = raw_html.find(pattern_end, start)
            link = raw_html[start:end]
            #print(link)
            if len(link) > 0: 
              # Define an absolute (base) URL of a web page
              base_url = url

              # Resolve links
              abs_link_1 = urljoin(base_url, link)

              if link not in urls:
                urls.append(abs_link_1)
            index = end
        else:
            break
    return urls

def enqueue(links):
    global frontier_q
    for link in links:
        if link not in frontier_q and link not in visited_q:
            frontier_q.append(link)

# FIFO queue
def dequeue():
    global frontier_q
    current_url = frontier_q[0]
    frontier_q = frontier_q[1:]
    return current_url

def isRobotsTxt(url):
    global headers
    global robots_file
    count = 0
    maindomain = ''
    for string in url:
      if string == '/' :
        if count < 2 :
          count += 1
        else :
          break
      maindomain = maindomain + string
    # Define an absolute (base) URL of a web page
    if maindomain in robots_file:
      return 1
    robotstxt = '/robots.txt'
    #print('robot checkkkkkkkkkkkkkkkkkk')
    # Resolve links
    abs_link_1 = urljoin(maindomain, robotstxt)
    #print(abs_link_1)
    linktest = abs_link_1
    text = get_robotspage(linktest)
    index = 0;  length = len(text)
    isBot = True
    sitemap = False
    if length == 0:
      return 0
    if 'User-agent:' in text or 'Disallow:' in text or 'Allow:' in text:
      isBot = True
    else:
      return 0
    if 'Sitemap:' in text:
      sitemap = True
    if isBot == True:
      #print('i am robottttttttttttttttttttttttttttttttttt')
      countsl = 0
      path = 'robot/'
      for i in current_url:
        if countsl < 2:
          if i == '/':
            countsl += 1
        elif countsl == 2:
          if i == '/':
            countsl += 1
          elif i == '?':
            path += '&qry&'
          elif i == ':':
            path += '&cln&'
          elif i == '<':
            path += '&lsth&'
          elif i == '>':
            path += '&meth&'
          elif i == '|':
            path += '&pip&'
          elif i == "'":
            path += '&qt&'
          elif i == "\"":
            path += '&dqt&'
          elif i == '*':
            path += '&mul&'
          elif i == '\\' :
            break
          elif i == ' ':
            continue
          else :
            path = path + i
        else:
          break
      os.makedirs(path, 0o755, exist_ok=True)
      # Write content into a file
      abs_file = path + '/robots.txt'
      f = codecs.open(abs_file, 'w', 'utf-8')
      f.write(text)
      f.close()
      bs_file = 'robots/list_robots.txt'
      f = codecs.open(bs_file, 'a', 'utf-8')
      f.write(maindomain+'\n')
      f.close()
      robots_file.append(maindomain)
      if sitemap == True:
        s_file = 'sitemap/list_sitemap.txt'
        f = codecs.open(s_file, 'a', 'utf-8')
        f.write(maindomain+'\n')
        f.close()
    return 1


while len(visited_q) < 10000 :
  current_url = dequeue()
  #print(unquote(current_url))
  #print(current_url)
  #urltest = unquote(current_url)

  #------------------CHECK PDF----------------------------
  length_url = len(current_url)
  if current_url[length_url-4] + current_url[length_url-3] + current_url[length_url-2] + current_url[length_url-1] == '.pdf':
    continue
  #------------------END OF CHECK PDF---------------------

  #-------------------CHECK HEADER------------------------
  meta_html,isRedirect,isHTML = get_headerpage(current_url)
  if meta_html == 'error' :
    continue
  if 'html' in isHTML:
    #print(isHTML)
    pass
  else :
    continue
  if isRedirect == True:
    print('redirect')
    raw_html,real_url = get_page(current_url)
    if raw_html == 'error':
      continue
    if real_url not in visited_q:
      if real_url in frontier_q:
        frontier_q.remove(real_url)
      frontier_q.insert(0,real_url)
    continue
  #---------------END OF CHECK HEADER---------------------

  if '%0' in current_url:
    new_current_url = ''
    i = 0
    while i < len(current_url):
        if current_url[i] == '%' and i < len(current_url):
            if current_url[i+1] == '0':
                i+=3
                continue
        new_current_url += current_url[i]
        i+=1
    current_url = new_current_url
  current_url = unquote(current_url)
  if len(current_url) > 190:
    continue
  #print(current_url)
  countsl = 0
  path = 'html/'
  for i in current_url:
    if countsl < 2:
        if i == '/':
            countsl += 1
    else:
      if i == '?':
        path += '&qry&'
      elif i == ':':
        path += '&cln&'
      elif i == '<':
        path += '&lsth&'
      elif i == '>':
        path += '&meth&'
      elif i == '|':
        path += '&pip&'
      elif i == "'":
        path += '&qt&'
      elif i == "\"":
        path += '&dqt&'
      elif i == '*':
        path += '&mul&'
      elif i == '\\' :
        break
      elif i == ' ':
        continue
      else :
        path += i
  if len(path) > 205:
    continue
  #print(path)
  if 'https.colon.//' in path or 'http.colon.//' in path:
    continue
  if path[len(path)-10:len(path)] == 'index.html':
    #check_index = current_url[:len(current_url)-11]
    #print(check_index)
    #if check_index in visited_q:
    #  print('check')
    #  continue
    path += '&idxpt&'
  #print(path)
  print(current_url)
  raw_html,notuse = get_page(current_url)
  if raw_html == 'error':
    continue
  visited_q.append(current_url)
  isRobotsTxt(current_url)
  extracted_links = link_parser(raw_html,current_url)
  enqueue(extracted_links)
  print(len(visited_q))
  # Create (sub)directories with the 0o755 permission
  # param 'exist_ok' is True for no exception if the target directory already exists
  #print(path)
  os.makedirs(path, 0o755, exist_ok=True)
  # Write content into a file
  abs_file = path + '/index.html'
  f = codecs.open(abs_file, 'w', 'utf-8')
  f.write(raw_html)
  f.close()

countf = 0
countv = 0
for i in frontier_q:
  countf += 1
  #print(i)
for i in visited_q:
  countv += 1
  print(i)

print(countf)
print(countv)
print(countf+countv)