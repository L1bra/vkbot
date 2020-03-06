from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot import VKbot 
from time import sleep
from mine import Mine
from cfg import *
import datetime
import random
import vk_api
import sys
import os


vk = vk_api.VkApi(token=TOKEN)


tool = vk_api.VkTools(vk)
longpoll = VkLongPoll(vk)


def make_time():
    return datetime.datetime.now().strftime("%H:%M:%S")


def run():
	print("Server started!")
	post_time = None
	urlid = 0
	bot = VKbot()

	while True:
		try:
			print('[{}] Creating post...'.format(make_time()))

			bot.wall_post()

			print('[{}] Success!'.format(make_time()))
			print("[{}] URL: https://vk.com/wall-100372734_{}".format(make_time(), urlid))
			urlid += 1
			print("[{}] Sleeping...".format(make_time()))
			sleep(60)
		except Exception as err:
			print('[{}] Error: {}'.format(make_time(), err))
			break