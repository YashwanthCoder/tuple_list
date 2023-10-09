def guest_list(guests):
	for i in guests:
		print("{} is {} years old and works as {}".format(i[0],i[1],i[2]))
print("Output should match:")
guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
