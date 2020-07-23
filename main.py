"""
Explain:
- Бот, генерирует контент(лол) на основе открытых сохраненок и музыки в вк.
-
- Контент?
-  > Рандомная фотка и песня от пользователя, т.е люди сами генерят контент в группе
-  > cool? хз
-


TODO:

class VKbot:
- chat stuff
- new_message(открой картинки/музыку, мудак)

class Mine:
- filer content(somehow) !?
- wall_post(audio from playlist and album)

"""





if __name__ == "__main__":
	try:
		import server
		server.run()
	except KeyboardInterrupt:
		print("terminated!")