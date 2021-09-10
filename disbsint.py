import csv

def add_entry(dis_id,bs_tag):
	file=open('disbs.csv','a',newline='')
  print('file opened')
	wr=csv.writer(file)
	wr.writerow([dis_id,bs_tag])
	file.close()

def show_entries():
	file=open('disbs.csv','r',newline='')
	wr=csv.reader(file)
	b=[i for i in wr]
	file.close()
	return b

def retr_entry(**data):
	file=open('disbs.csv','a',newline='')
	wr=csv.reader(file)
	b=[i for i in wr]
	file.close()
	if 'dis_id' in data:
		for i in range(len(b)):
			if data['dis_id']==i[0]:
				return i[1]
	if 'bs_tag' in data:
		for i in range(len(b)):
			if data['bs_tag']==i[1]:
				return i[0]
	