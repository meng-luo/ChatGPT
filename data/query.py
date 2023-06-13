import datetime
import requests
import time

proxies = {
    'http': 'http://127.0.0.1:10809',
    'https': 'http://127.0.0.1:10809'
}


def get_key(apikey):
    '''查询余量'''

    error = 0
    status = True

    subscription_url = "https://api.openai.com/v1/dashboard/billing/subscription"

    headers = {
        "Authorization": "Bearer " + apikey,
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }

    # 主请求段1
    while status == True:
        try:
            subscription_response = requests.get(subscription_url, headers=headers, proxies=proxies)
            status = False  # 判断成功退出循环
        except:
            error+=1    # 添加失误次数
            time.sleep(1)   # 暂停1秒
            if error > 5:
                status = False

    if subscription_response.status_code == 200:
        data = subscription_response.json()
        total = data.get("hard_limit_usd")  # 总量
    else:
        pass

    # 生成时间
    start_date = (datetime.datetime.now() - datetime.timedelta(days=99)).strftime("%Y-%m-%d")
    end_date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

    billing_url = f"https://api.openai.com/v1/dashboard/billing/usage?start_date={start_date}&end_date={end_date}"

    # 主请求段2
    status = True
    while status == True:
        try:
            billing_response = requests.get(billing_url, headers=headers, proxies=proxies)
            status = False  # 判断成功退出循环
        except:
            error+=1    # 添加失误次数
            time.sleep(1)   # 暂停1秒

    if billing_response.status_code == 200:
        data = billing_response.json()
        total_usage = data.get("total_usage") / 100     # 当前使用量
        daily_costs = data.get("daily_costs")   # 剩余
    else:
        pass
    output = []
    output.append(total)
    output.append(total_usage)

    return output



def get_dayly(day, apikey):
    '''查询使用情况'''

    error = 0
    status = True

    subscription_url = "https://api.openai.com/v1/dashboard/billing/subscription"

    # 请求头
    headers = {
        "Authorization": "Bearer " + apikey,
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }

    # 设置起始时间和终止时间
    start_date = (datetime.datetime.now() - datetime.timedelta(days=day)).strftime("%Y-%m-%d")
    end_date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

    billing_url = f"https://api.openai.com/v1/dashboard/billing/usage?start_date={start_date}&end_date={end_date}"

    # 主请求
    while status == True:
        try:
            billing_response = requests.get(billing_url, headers=headers, proxies=proxies)
            status = False # 判断成功退出循环
        except:
            error+=1 # 添加失误次数
            time.sleep(1) # 暂停1秒

    if billing_response.status_code == 200:
        data = billing_response.json()
        daily_costs = data.get("daily_costs")
        days = min(day, len(daily_costs))   # 需要查询的天数

        recent = f"最近{days}天使用情况  \n"

        # 循环每日使用情况
        for i in range(days):
            cur = daily_costs[-i - 1]
            date = datetime.datetime.fromtimestamp(cur.get("timestamp")).strftime("%Y-%m-%d")
            line_items = cur.get("line_items")
            cost = 0

            for item in line_items:
                cost += item.get("cost")
            recent += f"\t{date}\t{(cost / 100):.2f} \n"
    else:
        return billing_response.text

    return f"\n" + recent