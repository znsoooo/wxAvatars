import os
import sys # non_bmp_map 用到
import itchat
import PIL.Image as Image

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

name_chatrooms = [
                '砚湖大水坑',
                'NUAA研究生会15',
                'NUAA校研会2016',
                '祝17届同学们一路顺风',
                '17南航北京新生群'
                '南航NUAA北京校友群',
                '8090北京南航校友群',
                '南航南京校友会信息分会',
                '南航photo',
                '藤之屋日料',
                '北航就业信息分享群',
                '电力电子-全国硕博总群',
                '电力电子-电网级-硕博',
                '电力电子-中小功率-硕博',
                '电气硕博总群-按方向进分群',
                '航小团～二院物品交换空间5群',
                '包邮区适马交流群',
                '老虎证券港美股交流群',
                ]

user = 'avatars'
num_all = 0
all_friends = []

if not os.path.exists(user):
    os.makedirs(user)

itchat.auto_login(hotReload=True)

def log(text):
    f=open('log.txt','w',encoding = 'utf-8')
    f.write(str(text))
    f.close()

text = '\nfriends:\n\n'

friends = itchat.get_friends()[0:]
num_all = 0
for friend in friends:
    all_friends.append(friend["UserName"])
    ''''''
    #当只是需要输出好友列表而不需要下载头像时可以注释掉此段
    img = itchat.get_head_img(userName=friend["UserName"])
    fileImage = open(user + "/" + str(num_all) + ".jpg",'wb')
    fileImage.write(img)
    fileImage.close()
    ''''''
    text = text + str(num_all) + ".jpg " + friend["NickName"] + '\n'
    num_all += 1
print('friends finished:', len(all_friends))

for name_chatroom in name_chatrooms:
    chatrooms = itchat.search_chatrooms(name_chatroom)
    if chatrooms != []:
        chatroom = chatrooms[0]
        chatroom_id = chatroom['UserName']
        try:
            print('chatroom:', chatroom['NickName'].translate(non_bmp_map))
            text = text + '\nchatroom: ' + chatroom['NickName'] + '\n\n'
        except:
            print('chatroom name error')
        print('MemberCount:', chatroom['MemberCount'])
        memberList = itchat.update_chatroom(chatroom_id, detailedMember=True)
        chatroom = memberList
        num = 0
        print(len(chatroom))
        for member in chatroom['MemberList']:
            if member["UserName"] not in all_friends:
                all_friends.append(member["UserName"])
                ''''''
                #当只是需要输出好友列表而不需要下载头像时可以注释掉此段
                img = itchat.get_head_img(userName=member["UserName"],chatroomUserName=chatroom_id)
                fileImage = open(user + "/" + str(num_all) + ".jpg",'wb')
                try:
                    fileImage.write(img)
                    fileImage.close()
                except:
                    print('img error:', member["UserName"])
                ''''''
                text = text + str(num_all) + ".jpg " + member["NickName"] + '\n'
                num += 1
                num_all += 1
                if num < 10:
                    try:
                        print(num, member["NickName"].translate(non_bmp_map))
                    except:
                        print('nickname error')
            else:
                pass
                # print('duplicate:', member["NickName"].translate(non_bmp_map))
    else:
        print('Not found chatroom:', name_chatroom)
        print('MemberCount:', 0)
print('chatroom finished:', len(all_friends))
log(text)

