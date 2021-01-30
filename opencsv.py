
import csv
class Opencsv:
    def open_csv(filename):
        with open(str(filename),'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            patient_list=[]
            for row in csv_reader:
                patient_list.append(row)
        return patient_list
    
    




      
               
 


        
        
           








