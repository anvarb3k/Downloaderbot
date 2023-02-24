import requests
import json

def tiktok(link):
    url = "https://tiktok82.p.rapidapi.com/getDownloadVideoWithoutWatermark"

    querystring = {
        "video_url": link}

    headers = {
        "X-RapidAPI-Key": "42d6f07749mshb9b66ec144acdc4p132b88jsn786d4996054d",
        "X-RapidAPI-Host": "tiktok82.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    result = response.text
    rest = json.loads(result)
    answer = rest['video_url']
    return answer

def insta(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "42d6f07749mshb9b66ec144acdc4p132b88jsn786d4996054d",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.text
    resp = json.loads(result)
    answer = resp['media']
    return answer

def stories(link):
    url = "https://facebook-story-saver-and-video-downloader.p.rapidapi.com/"

    payload = f"URL={link}"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "42d6f07749mshb9b66ec144acdc4p132b88jsn786d4996054d",
        "X-RapidAPI-Host": "facebook-story-saver-and-video-downloader.p.rapidapi.com"
    }

    response = requests.request("GET", url, data=payload, headers=headers)
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
    answer = resp['formats'][1]['url']
    return answer