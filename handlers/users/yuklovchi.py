import requests
import json

def tiktok(link):
    

    url = "https://tiktok-downloader-download-videos-without-watermark1.p.rapidapi.com/media-info/"

    querystring = {"link":link}

    headers = {
        "X-RapidAPI-Key": "42d6f07749mshb9b66ec144acdc4p132b88jsn786d4996054d",
        "X-RapidAPI-Host": "tiktok-downloader-download-videos-without-watermark1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    result = response.text
    rest = json.loads(result)
    res = rest['result']['video']['url_list'][0]
    # music = rest['result']['music']['url_list']
    return res

def insta(link):

    url = "https://instagram-media-downloader.p.rapidapi.com/rapid/post.php"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "42d6f07749mshb9b66ec144acdc4p132b88jsn786d4996054d",
        "X-RapidAPI-Host": "instagram-media-downloader.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    resp= json.loads(result)
    rest = resp['video']
    return rest


# inp = input("link: ")
# print(insta(inp))