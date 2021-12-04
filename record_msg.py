#!/usr/bin/python3

from datetime import datetime
from pathlib import Path

import itchat
from get_userid import get_user_id


record_file = Path('record.txt').absolute()
handle = open(record_file, 'a', encoding='utf-8')

itchat.login()
itchat.send('Hello world', toUserName='filehelper')
get_user_id()
room_id = input('群聊ID：')
me = input('自己ID:')

@itchat.msg_register([itchat.content.TEXT, ], isGroupChat=True)
def record(msg):
    if msg['ToUserName'] != room_id:
        return
    line = '\t'.join([datetime.now(), msg['AcutalNickName'], msg['Text']]) + '\n'
    print(line)
    handle.write(line)
    if msg['Text'] == '#Stop' and msg['FromUserName'] == me:
        print('记录文件', record_file)
        itchat.logout()
itchat.run()

