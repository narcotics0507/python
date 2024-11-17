"""
allpost - 

Author: sonic
Version: 0.1
Date: 2024/11/15
"""
import requests
import time


def fetch_identity_info(batch_size=10, delay=1):
    """


    参数:
    - batch_size: 需要获取的批次数量。
    - delay: 每次请求之间的延迟，单位为秒，避免对服务器的过度请求。

    返回:

    """
    url = "https://api.pearktrue.cn/api/sfz/usa.php"
    identities = []

    for i in range(batch_size):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data["code"] == 200:
                    identities.append(data["data"])
                    print(f"第 {i + 1} 条信息获取成功: {data['data']}")
                else:
                    print(f"获取失败: {data.get('msg', '未知错误')}")
            else:
                print(f"请求失败，状态码: {response.status_code}")
        except Exception as e:
            print(f"请求异常: {e}")

        # 等待指定的时间
        time.sleep(delay)

    return identities


# 示例: 获取10条信息，每次请求间隔1秒
identities_info = fetch_identity_info(batch_size=10, delay=1)

# 输出结果
for identity in identities_info:
    print(identity)
