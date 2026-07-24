import urllib.request
import re

url = 'https://upload.wikimedia.org/wikipedia/commons/b/b3/Outline_Map_of_India.svg'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Find all path 'd' attributes
    paths = re.findall(r'<path[^>]*d="([^"]+)"', html)
    if not paths:
        # try single quotes
        paths = re.findall(r"<path[^>]*d='([^']+)'", html)
    
    if paths:
        longest = max(paths, key=len)
        print("Found longest path with length:", len(longest))
        with open('india_path.txt', 'w') as f:
            f.write(longest)
    else:
        print("No paths found.")
except Exception as e:
    print('Error:', e)
