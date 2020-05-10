# Parking-Citations

## Initial DataSet 

At a glance we need to clean up some of the information in the doc. What immediately stands out is we should break down the issue date column and remove the 'Ticket number' column as we will not need it for our purposes.
</br></br>
|Ticket number|Issue Date|Issue Time|RP State Plate|Plate Expiry Date|Make|Body Style|Color|Location|Route|Agency|Violation Description|
|-------------|----------|:---------|--------------|-----------------|----|----------|-----|--------|-----|------|---------------------|
|1103341116   |12/21/2015|   1251   |      CA      |     200304      |HOND|    PA    | GY  |13147 W.|1521 |  1   |No eveidence of Reg  |  |1103700150   |12/21/2015|   1435   |      CA      |     201512      |GMC |    VN    | WH  |525 S Ma|1C51 |  1   |No eveidence of Reg  |
|1104803000   |12/21/2015|   2055   |      CA      |     201503      |NISS|    PA    | BK  |200 West|2R2  |  2   |No eveidence of Reg  |   

</br></br>

Once completed, we now have two seperate columns for 'Year/Month' and omit the day from 'Issue date' and 'Ticket number'. This serves two purposes as now the dataset itself is easier to wield and with our 'Year/Month' columns, we can break down information without being too granular and cluttering our dashboard. 
</br></br>
|Issue Time|RP State Plate|Plate Expiry Date|Make|Body Style|Color|Location|Route|Agency|Violation Description|Month|Year|
|----------|--------------|:----------------|---------------|-----|--------|-----|------|---------------|-----|-----|----|
|   1251   |      CA      |     200304      |HOND|    PA    | GY  |13147 W.|1521 |  1   |No eveidence of Reg  |  12 | 15 |   
|   1435   |      CA      |     201512      |GMC |    VN    | WH  |525 S Ma|1C51 |  1   |No eveidence of Reg  |  12 | 15 |



</br></br>











<img src="Graph.png" width="1050" height="550">
