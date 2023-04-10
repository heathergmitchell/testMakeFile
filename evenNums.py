if __name__ == '__main__':
	f = open("evenNums.txt", 'w')
	for x in range(0, 101, 2):
		f.write(str(x) + '\n')
	f.close()
