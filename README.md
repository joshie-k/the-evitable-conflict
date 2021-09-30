# The Evitable Conflict

A fairly contrived activity to practice some of the refactor methods described in Chapter 7 of Working Effectively With Legacy Code: _I Don't Have Much Time and I Have to Change It_. 

> "Our new worldwide robot economy may develop its own problems, and for that reason we
have the Machines. The Earth’s economy is stable, and will remain stable, because it is based upon
the decisions of calculating machines that have the good of humanity at heart through the
overwhelming force of the First Law of Robotics"

You're a team of AI developers that have to add some functionality to the machines running the world. 

## Step 1: SPROUT METHOD
If you take a look at `WorldEconomyAggregator` there's a function called `aggregate_spend()`. It does some aggregation on a dictionary. Take a look at the function in `SuperComputer` to see what data we're working with. The new feature we want to add **using the SPROUT METHOD strategy** is deduplication. There can be overlap between each of the regional super comptuers i.e. a duplicate country code can show up twice in the aggregation dictionary. Implement some way to get rid of the duplicates. 
Could be
- Always take the lowest
- Always take the highest
- Take the Average
- Vote if 3 or more 

## Step 2: WRAP METHOD
Turns out, your AI boss told you that now we not only have to deduplicate, but when we finish aggregating the data we have to also upload the list of super computers used and the data dict. Add this functionality in **using the WRAP METHOD strategy**. Note you don't have to actually implement anything, but properly name the functions. 

## Step 3: WRAP CLASS
Now, you want to have the option to send out a notification to all the humans that the robots are watching their spend. Do this **using the WRAP CLASS METHOD strategy**. You can use the function in `TerribleClassMadeByYouTenYearsAgo`. But note that the class you will be "wrapping" is `WorldEconomyAggregator`. You can use either the decorator version of Wrap Class, or the non-decorator version. 

## Step 4: SPROUT CLASS
Last step is, we want to add a cool header to our notification to all the humans. We're going to pretend that the code is so convoluted the only way we can add to this and make it testable is by **using the SPROUT CLASS strategy**. 
