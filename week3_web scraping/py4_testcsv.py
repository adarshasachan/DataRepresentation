import csv

employee_file=open('employee_file.csv',mode='w')
employee_writer=csv.writer(employee_file,delimiter=',',quotechar='"',quoting =csv.QUOTE_MINIMAL )
employee_writer.writerow(['john smith','accounting','nove'])
employee_writer.writerow(['hay smith','ggg','march'])
employee_file.close()
