# -*- coding: UTF-8 -*-

import csv
import io
# with io.open('./test.csv', 'r', encoding = 'utf-8-sig') as r:
# 	print('内容如下\n')
# 	reader = csv.reader(r)
# 	for x in reader:
# 		print(x)
arr = [[11,12,13], [21,22,23], [31,32,33]]
with open('./test.csv', 'a') as r:
	writer = csv.writer(r)
	for i in arr:
		writer.writerow(i)
	print('写入完成')