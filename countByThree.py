if __name__ == '__main__':
	f = open("countByThree.txt", 'w')
	for x in range (0, 101, 3):
		f.write(str(x) + '\n')
	f.close()
