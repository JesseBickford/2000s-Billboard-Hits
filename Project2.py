# Project 2
# Step 1: Exploring your data.
# Load your data in using Pandas and start to explore. Save all of your early exploration code here and include in your final submission.


#load the pandas library

import numpy as np
import pandas as pd
#import the csv and call it
data = pd.read_csv('billboard.csv')
data
# Write a brief description of your data, and any interesting observations you've made thus far.
# The data lists billboard hits from the 00's, giving details about when each song peaked.

# Step 2: Clean your data.
# Do some rudimentary cleaning. Rename any columns that are poorly named, shorten any strings that may be too long, fill in any missing values. Explain your rationale for the way you choose to "impute" the missing data.


# strip the week columns down to just their #
data.columns = data.columns.str.replace('x','')
data.columns = data.columns.str.replace('th','')
data.columns = data.columns.str.replace('rd','')
data.columns = data.columns.str.replace('.week','')
data.columns = data.columns.str.replace('st','')
data.columns = data.columns.str.replace('nd','')

# change 'artist.inverted' to 'artist'
new_column = data.columns.values
new_column[1] = 'artist'
data.columns = new_column


data.columns

#remove all columns that are filled with only nulls
data = data.drop(data.columns[-11:], axis = 1)

#We need to change the data type of the 'date.entered' and 'date.peaked' fields from objects to datetime
data['date.entered'] = data['date.entered'].apply(pd.to_datetime)
data['date.peaked'] = data['date.peaked'].apply(pd.to_datetime)

#change the 'time' field from object to seconds
def time_to_secs(timeStr):
    mins = int(timeStr[0])
    secs = int(timeStr[2:])
    return mins*60 + secs
# Converting the time column to seconds and making it an int
data.time = data.time.apply(time_to_secs)
data.time = pd.to_numeric(data.time)





# ##### Using Pandas' built in `melt` function, pivot the weekly ranking data to be long rather than wide. As a result, you will have removed the 72 'week' columns and replace it with two: Week and Ranking. There will now be multiple entries for each song, one for each week on the Billboard rankings.
#come back to this

#create a list of the week columns
week_cols = []
for col in data.iloc[:,7:]:
    week_cols.append(col)

week_cols


data

#melt the data by week and rank
data_melted = pd.melt(data, id_vars=['track', 'artist', 'time', 'genre', 'date.entered', 'date.peaked'], value_vars=week_cols, var_name='Week', value_name='Rank')
data_melted

data_melted.to_csv('tableau.csv')


#datapiv = pd.pivot_table(data_melted, index = ['track', 'Week'], values = ['Rank'])
#datapiv

# ## Step 3: Visualize your data.
#create some useful variables for use during visualizations

#calculate average track length in seconds
print "The average track length in seconds is %d" % data['time'].mean()

#calculate the average billboard ranking by song as long as it was on the top 100 list
#calculate avg genre performance over time

#calculate the average of the last week of every song on the chart to see when you get kicked off

### Step 4: Create a Problem Statement.
#
# ##### Having explored the data, come up with a problem statement for this data set. You can feel free to introduce data from any other source to support your problem statement, just be sure to provide a link to the origin of the data. Once again- be creative!





# ## Step 5: Brainstorm your Approach.
# ##### In bullet-list form, provide a proposed approach for evaluating your problem statement. This can be somewhat high-level, but start to think about ways you can massage the data for maximum efficacy.





# ## Step 6: Create a blog post with your code snippets and visualizations.
# ##### Data Science is a growing field, and the Tech industry thrives off of collaboration and sharing of knowledge. Blogging is a powerful means for pushing the needle forward in our field. Using your blogging platform of choice, create a post describing each of the 5 steps above. Rather than writing a procedural text, imagine you're describing the data, visualizations, and conclusions you've arrived at to your peers. Aim for roughly 800-1,000 words.





# ## BONUS: The Content Managers working for the Podcast Publishing Company have recognized you as a thought leader in your field. They've asked you to pen a white paper (minimum 600 words) on the subject of 'What It Means To Have Clean Data'. This will be an opinion piece read by a wide audience, so be sure to back up your statements with real world examples or scenarios.
#
# ##### Hint: To get started, look around on the internet for articles, blog posts, papers, youtube videos, podcasts, reddit discussions, anything that will help you understand the challenges and implications of dealing with big data. This should be a personal reflection on everything you've learned this week, and the learning goals that have been set out for you going forward.
