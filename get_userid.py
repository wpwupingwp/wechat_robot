#!/usr/bin/python3

import itchat


itchat.auto_login()
# itchat.auto_login(hotReload=True)
print('查询用户ID')
while True:
    name = input('输入用户名/群聊名:\t')
    if name == 'exit':
        break
    rooms = itchat.search_chatrooms(name)
    for room in rooms:
        print('用户ID:', room['UserName'])
        print('用户昵称:', room['NickName'])
    users = itchat.search_friends(name)
    for user in users:
        print('用户ID:', user['UserName'])
        print('用户昵称:', user['NickName'])