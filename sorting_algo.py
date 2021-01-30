from opencsv import Opencsv
from sector_sorting import Sector

patient_info = Opencsv.open_csv('patients.csv')
vaccines = Opencsv.open_csv('vaccines.csv')
all_sectors = Sector('patients.csv')
sorted_sectors = all_sectors.sort_sector()

def main_script():
    for sector in sorted_sectors:
        #patient_in_sector=patient_sector(sector)
        sorted_patient = sort_patient(sector)
        print("LISTED PEOPLE FOR VACCINATIONS IN RANK AS FOLLOWS FOR", sector)
        print(sorted_patient)
        print('\n')
        

def patient_sector(sector): # sorts patients based on their sectors
    sec=[]
    for patient in patient_info:
        if int(patient.get('sector'))==sector:
            sec.append(patient)
    
    return sec

def algo_metrics(age,occupation):    #prioritizing the people based on their age and occupation
    if age>70:
        age_priority=4
    elif age>60:
        age_priority=3
    elif age>40:
        age_priority=2
    elif age>20:
        age_priority=1
    else:
        age_priority=0
    
    major = ['Retired','Nurse','Doctor','Care Home Employee']
    medium = ['Electrician','Athlete','Politician','Teacher', 'Lawyer','Accountant','Banker']
    minor = ['Student', 'Artist','Bus Driver','Programmer','Plumber']

    if occupation in major:
        occupation_priority=3
    elif occupation in medium:
        occupation_priority=2
    elif occupation in minor:
        occupation_priority=1
    else:
        occupation_priority=0
    
    return (age_priority+occupation_priority)/2
    
def sort_patient(sector):        
    patients_of_sector=patient_sector(sector)
    priorities=[]
    for i in range(len(patients_of_sector)):
        age=2021-int(patients_of_sector[i].get('date_of_birth').split('-')[0])

        priority=algo_metrics(age,patients_of_sector[i].get('occupation'))
        priorities.append(priority)
        patients_of_sector[i]['priority']=priority
    
    priorities.sort()
    reverse=priorities[::-1]
    new_patient_list=[]
    for p in reverse:
        for patient in patients_of_sector:
            if patient.get('priority')==p:
                new_patient_list.append(patient)
    
    return new_patient_list





main_script()


















        




























































































