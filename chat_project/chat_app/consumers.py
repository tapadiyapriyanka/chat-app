import json
from django.core import serializers
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
from channels.sessions import channel_session
from .models import chatmessage
from .utils import get_current_users

@channel_session_user_from_http
def ws_connect(message):
    Group('users').add(message.reply_channel)
    # data = json.loads(message['text'])
    #
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': True,
        })
    })

@channel_session_user
def ws_disconnect(message):
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': False
        })
    })
    Group('users').discard(message.reply_channel)

# @channel_session
# @channel_session_user
def ws_receive(message):
    data = json.loads(message['text'])
    print("data in ws_receive = ",data)
    # chatMessage = chatmessage.objects.create(username=message.user, textmsg=data['message'])
    # print("chatMessage = ",chatMessage)
    # obj = chatmessage.objects.get(pk=chatMessage.pk)
    # data = serializers.serialize('json', [obj,])
    # struct = json.loads(data)
    # data = json.dumps(struct[0])
    data1 = json.dumps(data)
    # Group('users').send({'text': json.dumps(data) }) #json.dumps(data.as_dict())})

# @channel_session
# def ws_message(message):
#     Group("users").send({
#             "text": message['text']
#         })




    # Group('users').send({
    #     "text": json.dumps({
    #         "text": message["text"],
    #         "username": message.channel_session["username"],
    #     }),
    # })

# @channel_session_user
# def ws_message(message):
#     Group("users").send({
#
#         "text": "[user] %s" % message.content['text'],
#     })
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    # message.reply_channel.send({
    #     "text": message.content['text'],
    # })
