#!/usr/bin/python3

from datetime import datetime
from pathlib import Path

import itchat
from get_userid import get_user_id


itchat.login()
itchat.send('Hello world', toUserName='filehelper')
me = itchat.search_friends()['UserName']
# some group name is hard to get
get_user_id()
room_id = input('要记录的群聊ID：')
room_name = itchat.search_chatrooms(userName=room_id)['NickName']
record_file = Path(f'record-{room_name}.txt').absolute()
handle = open(record_file, 'a', encoding='utf-8')
@itchat.msg_register([itchat.content.TEXT, ], isGroupChat=True)
def record(msg):
    if msg['ToUserName'] != room_id:
        return
    line = '\t'.join([datetime.now(), msg['ActualNickName'], msg['Text']]) + '\n'
    print(line)
    handle.write(line)
    if msg['Text'] == '#Stop' and msg['FromUserName'] == me:
        print('记录文件', record_file)
        itchat.logout()
itchat.run()

