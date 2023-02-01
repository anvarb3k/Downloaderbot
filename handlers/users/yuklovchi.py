import requests
import json

def tiktok(link):
    url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"

    querystring = {"url":link, "hd":"0"}

    headers = {
        "X-RapidAPI-Key": "42d6f07749mshb9b66ec144acdc4p132b88jsn786d4996054d",
        "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    rest = json.loads(result)
    answer = rest['data']['play']
    return answer

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

def stories(link):
    url = "https://facebook-story-saver-and-video-downloader.p.rapidapi.com/"

    payload = f"URL={link}"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "42d6f07749mshb9b66ec144acdc4p132b88jsn786d4996054d",
        "X-RapidAPI-Host": "facebook-story-saver-and-video-downloader.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    result = response.text
    res = json.loads(result)
    respons = res
    return respons

def youtube(link):
    url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"

    querystring = {"id":link}

    headers = {
        "X-RapidAPI-Key": "42d6f07749mshb9b66ec144acdc4p132b88jsn786d4996054d",
        "X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    res = response.text
    resp = json.loads(res)
    rest = resp['formats'][1]['url']
    return rest