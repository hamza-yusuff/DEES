from opencsv import Opencsv

class Sector:
    def __init__(self,filename):
        self.filename=filename
        
    
    
    def fileopen(self):
        patient_list=Opencsv.open_csv(self.filename)    #reading the data from the csv file
        return patient_list
    
    
    def extract_sector(self):
        patient_list=self.fileopen()
        sectors=[]
        for patient in patient_list:
            sector=patient.get('sector')
            if sector not in sectors:
                sectors.append(sector)
        
        return sectors
    
    
    def urgency(self):
        sectors_list=Opencsv.open_csv('urgency.csv')
        urgency_list=[]
        for sector in sectors_list:
            
            covid_cases=int(dict(sector).get('covid'))
            area=int(sector.get('area'))
            sector_name=sector.get('sector')
            density=int(covid_cases/area)
            urgency_list.append([sector_name,density])
        
        return urgency_list

    def sort_sector(self):
        covid_values=self.urgency() # returns nested list 
        densities=[]
        for covid_value in covid_values:
            densities.append(covid_value[1])
        sorted_density=sorted(densities)[::-1]
        #sorted out the densities according to the their covid value
        sorted_sector=[]
        for density in sorted_density:
            for covid in covid_values:
                if covid[1]==density:
                    sorted_sector.append(int(covid[0]))
                    break
        
        return sorted_sector # has the sorted list 
        

        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        



        




