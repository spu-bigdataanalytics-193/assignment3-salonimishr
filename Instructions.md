# :zzz: Assignment 2 :dancers::volcano:

In this assignment, we will work on map reduce algorithm. We have a dataset of size 1.6 GB (compressed, and 12 GB when uncompressed), with the records of nearly 120 million records. Our goal is to use map-reduce algorithm to get the **count** of **number of flights** for each carrier.

For simplicity, the code to make the dataset is already in the repository. I made it so that you can immediately start on map reduce section of the project. However, most of the data we are currently downloading is unneccessary. If you want to build your own dataset, you can do so.

## The Data
The data consists of flight arrival and departure details for all commercial flights within the USA, from October 1987 to April 2008. 

Each row represents an individual flight record with details of that flight in the row. The information are:

- Time and date of arrival
- Originating and destination of airports
- Amount of time for a plane from taxi to takeoff

You can find more information about this dataset in the website of [Statistical Computing](http://stat-computing.org/dataexpo/2009/).

PS: Don't get overwhelmed with the shape of the data, or the size of it, we are only interested in the number of records, and distinct number of carriers.

## The Assignment Instructions

In this assignment, you have to calculate the number of flights using map reduce algorithm. 

To help you out, the serial way of calculating the carrier flight count is built and added as an example. It is your duty to add the implementation of map reduce algorithm. 

How can you do this? Map reduce requires you to divide the task into 3 different pieces. For each algorithm, the following is the [pesudocode](https://en.wikipedia.org/wiki/Pseudocode) to write a map reduce way of python script.

1. Map Phase
    - For each line of flight data, extract the carrier code and make a key value pair. (ex: ('THY', 1))
2. Shuffle and Sort Phase
    - Read the list of pairs from the map phase.
    - Group all the values of each key together (ex: all THYs, Uniteds, etc.)
    - Sort the data by the key
3. Reduce Phase
    - Read each key and list of values from Shuffle and Sort phase.
    - Add the total # of ones in the carrier code's list together

You may come up with your own way of doing it, that's totally fine. The above pesudocode is only one way of solving it, it is up to you.

## What are all these other files?

Following table is will give it a meaning for each file.

File                | Description 
-------             | ----------- 
README.md **        | A descriptive file to give an introduction of current project/ assignment. 
Instructions.md **  | A copy of current README.md file. 
LICENCE **          | The licence of the file that every project should have.
.gitignore          | The file to control which files should be ignored by Git.
.gitkeep            | An empty file to keep folders under git.
data                | The flights dataset will be downloaded to this folder. (**You won't be adding your data to git**)
requirements.txt    | The packages needed to run this project. You may use `pip` to install these packages.
data_handler.py     | The helper module to download, and read data.
utils.py            | The helper module for some utiliy functions.
Assignment2.ipynb   | Assignment notebook. 

### Clarification on `data/` Folder

Once again, you won't be adding your data to your repository in GitHub. You cannot add it, but just as a warning, this is a warning that you should not add it. The way we control to not add the data into GitHub is the `.gitignore` file. 

``` .gitignore
...

# assignment specific ignores
data/
```

The above section in `.gitignore` file controls not to add the `data` folder to GitHub. Do not remove this addition.
