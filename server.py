from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot import VKbot 
from mine import Mine
from cfg import *
import random
import vk_api
import sys
import os


def write_msg(user_id, message):
	vk.method('messages.send', {'user_id': user_id, 'message': message, 
								'random_id': random.randint(0, 2048)})

vk = vk_api.VkApi(token=TOKEN)


tool = vk_api.VkTools(vk)
longpoll = VkLongPoll(vk)


def run():
	print("Server started!")

	for event in longpoll.listen():
	    if event.type == VkEventType.MESSAGE_NEW:

	        if event.to_me:
	        	print(f"New message from: {event.user_id} ", end='')

	        	bot = VKbot(event.user_id)

	        	if event.text:
	        		#write_msg(event.user_id, bot.new_message(event.text + ", " + bot._USERNAME))
	        		write_msg(event.user_id, bot.get_welcome_msg(event.user_id))
	        		

	        	print('Text:', event.text)