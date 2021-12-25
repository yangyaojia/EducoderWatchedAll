print("YJSchaf 来了全看了")

import requests

MAX_LEN = 60 

courseId = input("输入课程ID：")
Cookie = input("输入你的Cookie：")
headers = {
            'Host': 'data.educoder.net',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
            "Accept": "application/json",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://www.educoder.net/classrooms/" + courseId + "/video",
            "Content-Type": "application/json; charset=utf-8",
            "Origin": "https://www.educoder.net",
            "Connection": "keep-alive",
            "Cookie": Cookie
        }

vedios_info_url = "https://data.educoder.net/api/courses/" + courseId + "/course_videos.json?coursesId=" + courseId + "&id=" + courseId + "&limit=100"

vedios_info = requests.get(vedios_info_url, headers = headers).json()

post_url = "https://data.educoder.net/api/watch_video_histories.json"

for v in vedios_info["videos"]:

    req_payload = {
        "point":0,
        "video_id": v["id"],
        "course_id": courseId ,
        "duration": MAX_LEN, 
        "device": "pc"
        }
    r = requests.post(post_url, json = req_payload, headers = headers)
    
    response = r.json()

    update_payload = {
        "point": MAX_LEN,
        "log_id": response["log_id"],
        "watch_duration": MAX_LEN,
        "total_duration": MAX_LEN,
        "ed":"1"
        }
    r = requests.post(post_url, json = update_payload, headers = headers)
    response = r.json()

    if(response["message"] == "success"):
        print("【success】" + v["title"])
    else:
        print("【fail】" + v["title"])