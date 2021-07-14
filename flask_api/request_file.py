import requests

BASE_URL = "http://127.0.0.1:5000/"

# resp = requests.get(BASE_URL + "videos/111")
# print(resp.text)
# print(resp.status_code)

# resp = requests.put(BASE_URL + "videos/1", {"name": "Video Test",
#                                             "likes": "123",
#                                             "views": 10000})
# print(resp.text)

# resp = requests.put(BASE_URL + "videos/1", {"name": "Video Test",
#                                             "likes": "123",
#                                             "views": 10000})
# print(resp.text)

# resp = requests.patch(BASE_URL + "videos/1", {"name": "Video Test 2"})
# print(resp)

resp = requests.post(BASE_URL + "videos/", {"name": "Video Test",
                                           "likes": "123",
                                           "views": 10000})
print(resp)

resp = requests.get(BASE_URL + "videos/1")
print(resp.text)


# resp = requests.get(BASE_URL + "videos/1")
# print(resp.text)

resp = requests.delete(BASE_URL + "videos/1")
# print(resp.status_code)

# resp = requests.get(BASE_URL + "videos/1")
# print(resp.text)
