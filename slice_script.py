import re
import csv
line = []
list2 = []
with open('output2.txt') as f:
    for i in f:
    	line.append(i)
    	outList = re.findall(r"[-+]?\d*\.\d+|\d+", line[0]) # extracting integers from string
    	list2.append(outList[0])
    	list2.append(outList[2])
	#writing into csv file 
    	with open('epoch_loss.csv', 'a') as csvFile:
    		writer = csv.writer(csvFile)
    		writer.writerow(list2)

    	line.clear()
    	list2.clear()
