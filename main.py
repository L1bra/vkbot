### Explain: 
###
###	Бот, генерирует контент(лол) на основе открытых сохраненок и музыки в вк.
###
###	Контент?
###	> Рандомная фотка и песня от пользователя, т.е люди сами генерят контент в группе
###	> cool? хз 
###


## TODO:	
##	class VKbot:
##	> new_message(открой картинки/музыку, мудак)
##






if __name__ == "__main__":
	try:
		import server
		server.run()
	except KeyboardInterrupt:
		print("terminated!")