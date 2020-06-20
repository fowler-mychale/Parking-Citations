# Parking-Citations

## Initial Dataset 

At a glance we need to clean up some of the information in the doc. What immediately stands out is we should break down the issue date column and remove the 'Ticket number' column as we will not need it for our purposes.
</br>
|Ticket number|Issue Date|Issue Time|RP State Plate|Plate Expiry Date|Make|Body Style|Color|Location|Route|Agency|Violation Description|
|-------------|----------|:---------|--------------|-----------------|----|----------|-----|--------|-----|------|---------------------|
|1103341116   |12/21/2015|   1251   |      CA      |     200304      |HOND|    PA    | GY  |13147 W.|1521 |  1   |No eveidence of Reg  |  |1103700150   |12/21/2015|   1435   |      CA      |     201512      |GMC |    VN    | WH  |525 S Ma|1C51 |  1   |No eveidence of Reg  |
|1104803000   |12/21/2015|   2055   |      CA      |     201503      |NISS|    PA    | BK  |200 West|2R2  |  2   |No eveidence of Reg  |   



### Dataset after alterations
Once completed, we now have two seperate columns for 'Year/Month' and omit the day from 'Issue date' and 'Ticket number'. This serves two purposes as now the dataset itself is easier to wield and with our 'Year/Month' columns, we can break down information without being too granular and cluttering our dashboard. 
</br></br>
|Issue Time|RP State Plate|Plate Expiry Date|Make|Body Style|Color|Location|Route|Agency|Violation Description|Month|Year|
|----------|--------------|:----------------|---------------|-----|--------|-----|------|---------------|-----|-----|----|
|   1251   |      CA      |     200304      |HOND|    PA    | GY  |13147 W.|1521 |  1   |No eveidence of Reg  |  12 | 15 |   
|   1435   |      CA      |     201512      |GMC |    VN    | WH  |525 S Ma|1C51 |  1   |No eveidence of Reg  |  12 | 15 |





### Resulting Dashboard

<img src="Graph.PNG" width="1050" height="550">


### What we learned.

From the initial pie chart we can see that January, February, March and April were the most active.

Below we can observe the top 5 most ticketed by color and the count of tickets issued to out of state vehicles.</br>

### Top 5 ticketed cars by color and by out of state: </br>
  
- Black
- White
- Gray
- Silver
- Blue

### Top 5 by vehicles by Color and Make: 

The line chart tells us that the top 10 ticketed Make and Top 5 Color:</br>

### Top 5 ticket vehicles by state outside of CA: 


- Arizona
- Texas
- Nevada
- Florida
- Washington

And finally, we are able to determine what street issues the most tickets by month using a heatmap. What we can conclude is from January to May is when activity spikes and June through January shows a decline. We can also observe that 11600 San Vicente blvd had the most tickets issued total in the month of January.
</br>

### Tools used for this project:
- Python 3.8.2
- Excel
- AWS Quicksight
- CMD/Powershell
- VS Code

### Link to dataset </br>
https://www.kaggle.com/cityofLA/los-angeles-parking-citations?select=parking-citations.csv
