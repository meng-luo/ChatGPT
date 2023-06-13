import requests
import json
import time


url = "https://api.openai.com/v1/chat/completions" # 接口地址

proxies = {
    'http': 'http://127.0.0.1:10809',
    'https': 'http://127.0.0.1:10809'
}


def request(key, role, text, temperature):
    '''对接口发送请求'''
    status = True
    error = 0

    headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Authorization': 'Bearer '+key
    } # 请求头

    payload = json.dumps({
    "model": "gpt-3.5-turbo",
    "messages": [
        {
        "role": role,
        "content": text
        }
    ],
    "temperature": temperature
    }) # 构造POST包


    # 发送请求
    while status == True: # 防止单次请求失败
        try:
            send = requests.post(url, headers=headers, data=payload, proxies=proxies) # 主请求
            status = False # 判断成功退出循环
        except:
            error+=1 # 添加失误次数
            time.sleep(1) # 暂停1秒

    # 处理接口返回数据
    if send.status_code == 200:
        data = json.loads(send.text)
        text = data['choices'][0]['message']['content']

        output = text
    else:
        try:
            data = json.loads(send.text)
            text = data['error']['code']
        except:
            text = send.text
        output = "请求错误\n===============\n"+text

    return output