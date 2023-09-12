import requests

url = 'https://www.gutenberg.org/files/10/10-0.txt'
file_path = 'C:/Users/jiang/Desktop/holy_bible_chapter_1.txt'

response = requests.get(url)
content = response.text

with open(file_path, 'w', encoding='utf-8') as file:
    file.write(content)