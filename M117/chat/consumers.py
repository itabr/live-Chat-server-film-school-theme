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
    data = eval(message.content['text'])
    action = Action.objects.create(first_name = data[0],text = data[1],)
    Group("Action").send({
        "text": json.dumps({"name" : data[0],"text" : data[1]})
    })

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("Action").discard(message.reply_channel)
