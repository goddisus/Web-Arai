
import os, codecs

path = 'robot'
raw_html = 'hello'
os.makedirs(path, 0o755, exist_ok=True)
# Write content into a file
abs_file = path + '/robots.txt'
f = codecs.open(abs_file, 'w', 'utf-8')
f.write(raw_html)
f.close()