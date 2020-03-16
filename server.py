from vk_bot import VKbot 
from time import sleep
from cfg import *
import datetime




def make_time():
    return datetime.datetime.now().strftime("%H:%M:%S")


def run():
	print("Server started!")

	bot = VKbot()


	while True:
		try:
			print('[{}] Creating post...'.format(make_time()))
			bot.wall_post()

			print('[{}] Success!'.format(make_time()))
			print("[{}] Sleeping...".format(make_time()))
			sleep(220)
		except Exception as err:
			print('[{}] Error: {}'.format(make_time(), err))
			continue