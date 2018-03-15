class To_do(object):
	def __init__(self):
		self.done_list=[]
		self.to_do_list=[]	

	def add(self):
		print('-----Tasks-----')
		x=input('enter the task  : ')
		(self.to_do_list).append(x)


	def mark_done(self):
		print('-----Tasks-----')
		for i,val in enumerate(self.to_do_list):
			print('\n',i,"-",val)
		x=int(input("\nselect the finished task  : "))
		self.done_list.append(self.to_do_list[x])
		self.to_do_list.remove(self.to_do_list[x])

	def see_task(self):
		print('-----Tasks-----\n')
		print("pending :",self.to_do_list)
		print("done    :",self.done_list)

