from channels import Group
import json
from django.core.serializers import serialize
import re
from .models import *
# Connected to websocket.connect

def ws_add(message):
    chatroom = re.sub('/', '', message.content['path'])
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    Group(chatroom).add(message.reply_channel)

# Connected to websocket.receive
def ws_message(message):
    chatroom = re.sub('/', '', message.content['path'])
    data = eval(message.content['text'])

    if('private' in chatroom):
         Group(chatroom).send({
        "text": json.dumps({"name" : data[0],"text" : data[1],'time':data[2]})
        })         
    else:
        command =  chatroom + ".objects.create(first_name = data[0],text = data[1],time = data[2])"
        eval(command)

        Group(chatroom).send({
            "text": json.dumps({"name" : data[0],"text" : data[1],'time':data[2]})
        })

# Connected to websocket.disconnect
def ws_disconnect(message):
    chatroom = re.sub('/', '', message.content['path'])
    Group(chatroom).discard(message.reply_channel)
