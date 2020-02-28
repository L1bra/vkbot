from mine import Mine
from cfg import *
import vk_api


class VKbot:
	def __init__(self, user_id):

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



	#нет метода для поста фотки с url, придётся писать свою, ахуенно
	# ОПТЯТ РАБОТА (с) rab iz wc3
	# self.parser.get_audio/photo 
	def wall_post(self):
		vk, _ = self.parser._get_api()

		upload = vk_api.VkUpload(vk)

		photo = upload.photo_wall(
			'',
			group_id=GROUP_ID
			)