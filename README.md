This is our implementation of our design for DEES Hackthon. 

Below you can find a broad description of our design -
Hi ,
Addressing the problem in two stages -

Logistics related to the transportation of vaccines effectively-
We are planning to use cold chain distribution process along ML, IOT to improve
·         Logistics performanance
·         Operations cost optimization 
of vaccine delivery from the central vaccine centres to the city vaccination centres. 
--- Hamza
 
Vaccine distribution system - Vaccinating people encomposses a lot of challenges, the main four we identified are -
Population attitude which also relates to individual Consent, How effectively can people get vaccinated at the fastest rate possible, who are the most vulnerable and how we do we reach out to them , and the last but not the least how fast can the whole process be implemented ensuring maximum efficiency, least wastage and fastest flattening of the curve. 
 
 
 Now, To administer the process of vaccination, we plan to make an app available for the citizens to download and enter the relevant details through which they can be identified from the data already available to the government. ---- Taseen
 
 
 
 We have designed our idea to address each sector individually based on their current situation of covid, rather than having a centralized system . This way we can leverage microservices which will further ensure that  there is no dependency between the sectors.    
	 
       Such Sector based approach rather than a central administration , will also help to tackle the spread of the virus as efficiently as possible. Moreover, sector based approach will also help to address the issue of skepticism of particular individuals regarding the vaccination since we can assume that a particular group of people or a sector’s community will have a similar mindset. --- rajarshi 
 
 
 
Firstly, the app will ask for each citizen’s consent when they download the app for the first time. We’ll assume that there would be governmental legislation to ensure that every citizen downloads the app and provides their consent within a specific span of time. After the end of the specified period , the city council can get an estimate of the amount of vaccines to be ordered. If a good number opts for the vaccine , the cheaper can be ordered and if not the other. This way we reduce the wastage , without compromising with the vaccination of citizens.
 
After that , we’ll use the current data and previous covid relevant data of the sectors to categorize them .Bsaically we’’ have the sectors ranked
 
Then, we’ll apply all of the factors of Age and Occupation  for the each of the sectors individually to rank the citizens within their particular sectors.
We will essentially assign each citizen a priority rating through our designed algorithm that we have implemented here. The algorithm takes mostly into consideration age and occupation, along with recovered patients. 
 
 
After having sorted all the citizens, we will use the sorted data and the data aggregated from the vaccine.csv file to assign each of them a due time for their vaccination. 
 
----Now here comes the question of consent when covid is already on the run and ruining lives. This is an assumption made.
 
---Future goals to integrate the whole network, 
Regular text messages will also be sent to check on the citizen’s health or whether he/she is having side effects or not. 
 
-- 

