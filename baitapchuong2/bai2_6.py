import requests
# Thực hiện yêu cầu HTTP đến URL 'https://jsonplaceholder.typicode.com/posts'
response = requests.get('http://www.hindustantimes.com/rss/topnews/rssfeed.xml')
if response.status_code == 200:
# Nếu yêu cầu thành công, lấy dữ liệu JSON từ phản hồi
    json_data = response.json()