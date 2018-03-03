import os
import sys # non_bmp_map 用到
import itchat
import PIL.Image as Image

# 转载请注明出处
# 原文标题：微信好友头像拼接
# 原文地址：https://github.com/znsoooo/wxAvatars
# 原文作者：硫酸锌01/流水线

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

name_chatrooms = [
                '硫酸锌01粉丝群1',
                '硫酸锌01粉丝群2',
                '硫酸锌01粉丝群3',
                '微信群名记录在这里',
                '需要提前将群保存到通讯录',
                '群名可以不是全称',
                '只要搜索到没有歧义就行',
                '不然只能返回搜索结果的第一项',
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

