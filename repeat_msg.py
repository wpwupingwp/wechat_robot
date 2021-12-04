#!/usr/bin/python3

import itchat
from datetime import datetime
from get_userid import get_user_id


itchat.login()
itchat.send('Hello world', toUserName='filehelper')
get_user_id()
room_id = input('群聊ID：')
me = input('自己ID:')

@itchat.msg_register([itchat.content.TEXT, ], isGroupChat=True)
def repeat(msg):
    print(datetime.now())
    if msg['ToUserName'] != room_id:
        return
    print(datetime.now(), +msg['ActualNickName'], msg['Text'])
    if msg['FromUserName'] == me:
        if not msg['Content'].startswith('#'):
            pass
    else:
        itchat.send('[机器人]'+msg['ActualNickName']+':'+msg['Text'], room_id)
itchat.run()

