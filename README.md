# Stack-Exchange-Data-Dump
In this repository, we analyze data from Stack Exchange Data Dump. We use python and aim to find "good" questions, answers, users and visualize the flow of questions/answers over time.

# The data
We are using information from the Stack Exchange Data Dump. To start we are analizing the flow of the bitcoin, ethereum, and economics data bases. 

https://archive.org/details/stackexchange

# Requirements

We are coding in python 3. The xml files Users.xml and Posts.xml must be located in the same folder as the main code run.py

# Our aproach

The code is provided as a single file 

run.py

This code is dividede into different sections

* From xml to csv: In this section we use Apache Spark to read the xml files and transform those to csv files, of course this step is quick since we use distributed computing

* In the next step we read the users_csv files to find the top 10 questions/answers according to their score

* Then we find the questions associated with the top 10 responses

* Next we find the accepted answers (if they exists) of the top 10 questions

* We display (see examples below) the top 3 (of each cathegory) of our results: Top 3 questions, top 3 accepted answers, top 3 answers

* Then we focus in the flow of questions/answers of each data base over time (see graphs below)

* Next we focus in the users_csv files to find top responder according to our own metric

Individual Punctuation = Reputation + Up Votes -Down Votes

* Once we find the top 10 users we display relevant information for further analysis such as: Location, Age, and About Me 

* Finally, we track the activity of the top 3 users over time in terms of post history (see graphs below)

