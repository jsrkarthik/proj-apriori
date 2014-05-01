import csv
cr = csv.reader(open("DMEF customer data file_comma.csv","rb"))
dic=dict()
for row in cr:    
    if row[5] not in dic:
       dic[row[5]]=list()
       dic[row[5]].append(row[6])
    else:
       if row[6] not in dic[row[5]]:
          dic[row[5]].append(row[6])

for keys in dic:
   for val in dic[keys]:
      print val,
      print " ",
   print "\n"             
       
