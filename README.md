# weatherStation
Scraping data from my PWS to find emergent information


#MILESTONES

## Host application in cloud to retreive data automatically
9 May 2022 - Sucessfull API call retreived data on JSON format.

12 May 2022 - Script sucessfully runs on Google Compute VM (GVM).
  Cron Job exicutes the code every hour, formats results and prints them to a spreadsheet
  hosted on Google sheets.
  
13 May 2022 - Cron jobs set up on GVM to pull from from GitHub repo once a month and update script. 
  Hopefully I shouldn't have to log into GVM and can work on my script from home and push updates 
  to Git Hub. Next step set up GVM to come up and shutdown on a regular basis, I'm only using it 
  for 5 or so mins per hour and don't need to pay for a whole hour.
  
Next I want to break ambWeather.py up into modules and clean and document my code better.


## Work on Data Modeling, proabibly with Python Pandas





