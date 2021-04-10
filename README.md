# Familiar-A-Study-In-Data-Analysis
Familiar: A Study In Data Analysis
Welcome to Familiar, a startup in the new market of blood transfusion! You’ve joined the team because you appreciate the flexible hours and extremely intelligent team, but the overeager doorman welcoming you into the office is a nice way to start your workday (well, work-evening).

Familiar has fallen into some tough times lately, so you’re hoping to help them make some insights about their product and help move the needle (so to speak).

Note that a solution.py file is also loaded for you in the workspace, which contains solution code for this project. We highly recommend that you complete the project on your own without checking the solution, but feel free to take a look if you get stuck or want to check your answers!

Tasks
13/13 Complete
Mark the tasks as complete by checking them off
What Can Familiar Do For You?
1.
The Familiar team has provided us with some data on lifespans for subscribers to two different packages, the Vein Pack and the Artery Pack! This data has been loaded for you as a dataframe named lifespans. Use the .head() method to print out the first five rows and take a look!


Stuck? Get a hint
2.
The first thing we want to know is whether Familiar’s most basic package, the Vein Pack, actually has a significant impact on the subscribers. It would be a marketing goldmine if we can show that subscribers to the Vein Pack live longer than other people.

Extract the life spans of subscribers to the 'vein' pack and save the data into a variable called vein_pack_lifespans.


Stuck? Get a hint
3.
Next, use np.mean() to calculate the average lifespan for Vein Pack subscribers and print the result. Is it longer than 73 years?


Stuck? Get a hint
4.
We’d like to find out if the average lifespan of a Vein Pack subscriber is significantly different from the average life expectancy of 73 years.

Import the statistical test from scipy.stats that we would use to test the following null and alternative hypotheses:

Null: The average lifespan of a Vein Pack subscriber is 73 years.
Alternative: The average lifespan of a Vein Pack subscriber is NOT 73 years.

Stuck? Get a hint
5.
Now that you’ve imported the function you need, run the significance test and print out the p-value! Is the average lifespan of a Vein Pack subscriber significantly longer than 73 years? Use a significance threshold of 0.05.


Stuck? Get a hint
Upselling Familiar: Pumping Life Into The Company
6.
In order to differentiate Familiar’s different product lines, we’d like to compare this lifespan data between our different packages. Our next step up from the Vein Pack is the Artery Pack.

Let’s get the lifespans of Artery Pack subscribers. Using the same lifespans dataset, extract the lifespans of subscribers to the Artery Pack and save them as artery_pack_lifespans.


Stuck? Get a hint
7.
Use np.mean() to calculate the average lifespan for Artery Pack subscribers and print the result. Is it longer than for the Vein Pack?


Stuck? Get a hint
8.
We’d like to find out if the average lifespan of a Vein Pack subscriber is significantly different from the average life expectancy for the Artery Pack.

Import the statistical test from scipy.stats that we would use to test the following null and alternative hypotheses:

Null: The average lifespan of a Vein Pack subscriber is equal to the average lifespan of an Artery Pack subscriber.
Alternative: The average lifespan of a Vein Pack subscriber is NOT equal to the average lifespan of an Artery Pack subscriber.

Stuck? Get a hint
9.
Now that you’ve imported the function you need, run the significance test and print out the p-value! Is the average lifespan of a Vein Pack subscriber significantly different from the average lifespan of an Artery Pack subscriber? Use a significance threshold of 0.05.


Stuck? Get a hint
Side Effects: A Familiar Problem
10.
The Familiar team has provided us with another dataset containing survey data about iron counts for our subscribers. This data has been pre-processed to categorize iron counts as “low”, “normal”, and “high” for each subscriber. Familiar wants to be able to advise potential subscribers about possible side effects of these packs and whether they differ for the Vein vs. the Artery pack.

The data has been loaded for you as a dataframe named iron. Use the .head() method to print out the first five rows and take a look!


Stuck? Get a hint
11.
Is there an association between the pack that a subscriber gets (Vein vs. Artery) and their iron level? Use the pandas crosstab() function to create a contingency table of the pack and iron columns in the iron data. Save the result as Xtab and print it out.


Stuck? Get a hint
12.
We’d like to find out if there is a significant association between which pack (Vein vs. Artery) someone subscribes to and their iron level.

Import the statistical test from scipy.stats that we would use to test the following null and alternative hypotheses:

Null: There is NOT an association between which pack (Vein vs. Artery) someone subscribes to and their iron level.
Alternative: There is an association between which pack (Vein vs. Artery) someone subscribes to and their iron level.

Stuck? Get a hint
13.
Now that you’ve imported the function you need, run the significance test and print out the p-value! Is there a significant association between which pack (Vein vs. Artery) someone subscribes to and their iron level? Use a significance threshold of 0.05.
