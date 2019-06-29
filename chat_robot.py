# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse

def get_robot_reply(question):
    '''
    函数功能：对特定问题进行特定回复，对于非特定问题进行智能回复
    
    参数描述：
    question 聊天内容或问题

    返回值：str, 回复内容
    '''

    if "你叫什么名字" in question:
        answer = "我是LH"
    elif "你多少岁" in question:
        answer = "20"
    elif "你是MM还是GG" in question:
        answer = "你猜呢"
    else:
        try:
            # 调用NLP接口实现智能回复
            params = urllib.parse.urlencode({'msg': question}).encode() # 接口参数需要进行URL编码
            req = urllib.request.Request("http://api.itmojun.com/chat_robot", params, method = "POST") # 创建请求
            answer = urllib.request.urlopen(req).read().decode() # 调用接口（即向目标服务器发出HTTP请求，并获取服务器的响应数据）
        except Exception as e:
            answer = "AI机器人出现故障！（原因：%s）" % e

    return answer


# if __name__ == '__main__':
#     # 测试get_robot_reply函数
#     print(get_robot_reply("你叫什么名字"))
#     print(get_robot_reply("武汉明天天气如何"))

# while True:
#     print(get_robot_reply(input()))