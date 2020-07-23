from vk_api.audio import VkAudio
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
        self._random_id = None

    LAST_NAME_USER = None


    # TODO:
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


    def get_photo(self):
        _, tool = self._get_api()
        random_id = self.get_id()

        try:
            dump = tool.get_all('photos.get', 100, {'owner_id': random_id, 'album_id': 'saved'})
            lists_items = dump.get('items')

            data = ''.join([str(x['id']) + " " for x in lists_items])
            photo_id = self.get_random(data.split())

            int_opt = next(filter(lambda name: str(name['id']) == photo_id, lists_items))
        except Exception as error:
            print(f"Error: {error}")

            self.add_to_ignore_list(str(random_id))
            return

        return int_opt['id'], int_opt['owner_id']


    def get_audio(self, flag=None):
        vkObj, _ = self._get_api()

        if flag:
            random_album = random.randint(0, 3)
            dump = VkAudio(vkObj).get(owner_id=ALBUM_DICT['ALBUM_{}'.format(random_album)].split('_')[0],
                                      album_id=ALBUM_DICT['ALBUM_{}'.format(random_album)].split('_')[1])
        else:
            dump = VkAudio(vkObj).get(owner_id=self.get_id())

        data = ''.join([str(x['id']) + " " for x in dump])
        track_id = self.get_random(data.split())

        int_opt = next(filter(lambda name: str(name['id']) == track_id, dump))

        return int_opt['id'], int_opt['owner_id']


    def get_id(self):
        _, tool = self._get_api()
        dump = tool.get_all('groups.getMembers', 100, {'group_id': "192701320"})

        while True:
            self._random_id = self.get_random(list(dump['items']))
            if str(self._random_id) not in SKIP_LIST:
                break

        return self._random_id


    def add_to_ignore_list(self, owner_id):
        if owner_id not in SKIP_LIST:
            SKIP_LIST.append(owner_id)


    # TODO: Finish this
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
    def _clean_all_tag_from_str(string):
        result = ""
        not_skip = True

        for i in list(string):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += 1
            else:
                if i == ">":
                    not_skip = True

        return result

    # yep another GET_SOMETHING, do SOMETHING with it...
    def get_random(self, obj):
        return random.choice(obj)

    def get_playlist_by_id(self, user_id):
        url = "https://vk.com/audios" + str(user_id)
        return url

    def req(self, http: str):
        request = requests.get(http)
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        return bs