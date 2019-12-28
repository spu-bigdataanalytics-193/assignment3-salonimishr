# assignment3-salonimishr
assignment3-salonimishr created by GitHub Classroom

I downloaded the data from "http://stat-computing.org/dataexpo/2009/" website, I used user-defined library data_handler. 
The whole data which is stored in 22 data files in zip format(.bz2) consists of the size of 12gb. The system random access memory was
limited and do not allow to load the complete data. As suggested, only the data important for map reduce is loaded to surpass
the difficulty. The data consists of 123 million of records from year 1987 to 2008.

Map reduce is very functional algorithm where three parts of it can easily executed. The goal is to use map-reduce algorithm to get
the count of number of flights for each carrier. For comparison, I used two ways of getting counts of carriers.

1. Looping through each record and counting each airline's flight.

2. Map reduce way - map, reduce and sort, and collect way to count the flights. 

In map phase, for each line of flight data, I extracted the carrier code and make a key value pair as ('TW' 1). In shuffle and sort phase
In this phase, I listed the pairs from the map phase and grouped all values of each key together. After this, I sorted the data by the key.
In reduce phase, I read each key and list of values from shuffle and sort phase. I also added the total # of ones in the carrier code's
list together.
It can be concluded from above, map-reduce does not only take less time but also easy to implement.
