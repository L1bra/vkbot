from mine import Mine
from cfg import *
import requests
import vk_api





class VKbot:
	def __init__(self, user_id=None):

		self.parser = Mine()

		self._USER_ID = user_id
		self._USERNAME = self.parser.get_username_by_id(user_id)


		# chat things
		self.WELCOME_MSG_SEND = False
		self._COMMANDS = ["ПРИВЕТ", "", ""] # privet, poka i td


	def get_welcome_msg(self, user_id: any) -> str:
		if self.parser.LAST_NAME_USER is None:
			user_name = self.parser.get_username_by_id(user_id)
		else:
			user_name = self.parser.LAST_NAME_USER

		self.WELCOME_MSG_SEND = True

		return "Privet! " + user_name.split()[0]


	def new_message(self, message):
		if message.upper() == self._COMMANDS[0]:
			print(self._COMMANDS[0])

			return f"Hello!", {self._USERNAME}

		#elif message.upper() == self._COMMANDS[1]
			#return 
		else:
			return "idk what are you talking about.."


	#TODO: 	audio from playlist and album
	def wall_post(self):
		photo_id, owner_photo_id = self.parser.get_photo()
		audio_id, owner_audio_id = self.parser.get_audio(flag)



		attachments = 'photo{}_{}, audio{}_{}'.format(owner_photo_id, photo_id,
						owner_audio_id, audio_id)

		response = self.send_method('wall.post', {
			'owner_id': "-"+GROUP_ID,
			'from_group': 1,
			'attachments': attachments
			})

		return response


	# ???
	def send_method(self, method, data=None):
		vk, _ = self.parser._get_api()
		rs = vk.method(method, data)
		return rs