from vk_api.audio import VkAudio
import urllib.request
from cfg import *
import requests
import random
import vk_api
import time
import bs4



class Mine:
	# next lvl parse? xd
	time = time.localtime()

	def __init__(self):
		self.userid = None

	LAST_NAME_USER = None


	#TODO:
	def check_auth(self):
		pass


	def get_username_by_id(self, user_id):
		return self._get_username_by_id(user_id)


	def _get_username_by_id(self, user_id):
		b = self.req("https://vk.com/id" + str(user_id))
		user_name = self._clean_tag_from_str(b.findAll("title")[0])


		self.LAST_NAME_USER = user_name
		self.userid = user_id

		return user_name


	def _get_api(self):
		vk_session = vk_api.VkApi(login=LOGIN, password=PASSWORD)
		vk_session.auth()
		vk = vk_session.get_api()

		tool = vk_api.VkTools(vk_session)

		return vk_session, tool


	### should be done ###
	# https://vk-api.readthedocs.io/en/latest/upload.html
	# https://vk.com/dev/photos.get
	#TODO:  check if self.user_id is None
	#		figure out how to store it
	#		choose 1 pic randomly
	def get_photo(self):
		_, tool = self._get_api()
		dump = tool.get_all('photos.get', 100, {'owner_id': MY_ID, 'album_id': 'saved'})
		# picture_url = dump.get('items')[-1].get('sizes')[-1].get('url')
		picture_id = dump.get('items')[-1].get('id')

		return picture_id


	def get_audio(self):
		vkObj, _ = self._get_api()
		dump = VkAudio(vkObj).get(owner_id=self.userid)

		data = ''.join([str(x['id']) + " " for x in dump])
		track_id = self.get_random(data.split())
		
		int_opt = next(filter(lambda name: str(name['id']) == track_id, dump))

		return str(int_opt['artist'] + "-" + int_opt['title'])


	####finish writing
	# def check_instance(self, obj, key):
	# 	if isinstance(obj, dict):
	# 		for k, v in obj.items():
	# 			if isinstance(v, dict) or isinstance(v, list):

	# 	elif isinstance(obj, list):
	# 		return


	@staticmethod
	def _clean_tag_from_str(string):
		s = ""

		for char in string:
			s += char

		return s


	@staticmethod
	def _clean_all_tag_from_str(stringLine):
		result = ""
		not_skip = True

		for i in list(stringLine):
			if not_skip:
				if i == "<":
					not_skip = False
				else:
					result += 1
			else:
				if i == ">":
					not_skip = True

		return result


	#yep another GET_SOMETHING, do SOMETHING with it...
	def get_random(self, obj):
		return random.choice(obj)


	def get_playlist_by_id(self, user_id):
		url = "https://vk.com/audios" + str(user_id)
		return url


	def req(self, http: str):
		request = requests.get(http)
		bs = bs4.BeautifulSoup(request.text, "html.parser")
		return bs