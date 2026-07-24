import os
import re
import time

cache_version = str(int(time.time()))

for f in os.listdir("."):
    if f.endswith(".html") or f.endswith(".php"):
        try:
            content = open(f, "r", encoding="utf-8", errors="ignore").read()
            new_content = re.sub(r'style\.css\?v=\d+', f'style.css?v={cache_version}', content)
            if new_content != content:
                open(f, "w", encoding="utf-8").write(new_content)
        except Exception as e:
            pass

print(f"Cache buster bumped to v={cache_version}!")
