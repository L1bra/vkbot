### Explain: 
###
###	Бот, генерирует контент(лол) на основе открытых сохраненок и музыки в вк.
###
###	Контент?
###	> Рандомная фотка и песня от пользователя, т.е люди сами генерят контент в группе
###	> cool? хз 
###


## its time to think:
## 
## > 24/7 работающий код -> cost money (heroku?)
## > Запускать код фоном, когда работает ноут?
## > Запускать код когда это нужно(wtf!?)
## > Database?
##


# TODO:	
#	class Mine:
#	> https://vk.com/dev/photos.get
#	> Дописать get_photo()
#	> Парсинг всех подписавшихся пользователей > добавление их в "лотерею"
#
#
#	class VKbot:
#	> дописать post_wall()
#	> future: модерация?
#	> new_message(открой картинки/музыку, мудак)
#






if __name__ == "__main__":
	try:
		import server
		server.run()
	except KeyboardInterrupt:
		print("terminated")