import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

#It is used for the color of the axes.
sns.set_style("darkgrid")

#Load Dataset
df= pd.read_csv("D:\Projects\SpotifyDatasetAnalysis\data.csv") 

#inplace=True : means the operation would work on the original object. 
#axis=1 means we are dropping the column, not the row.
df.drop("Unnamed: 0", axis=1, inplace=True) 

#Returns the first 5 rows of the dataframe. To override the default, 
#you may insert a value between the parenthesis to change the number of rows returned.
print(df.head())

#Data Cleaning
#you can count NaN values, returns the number of missing values in each column
print(df.isna().sum())

print(df.info())
print(df.shape)
#Printing the column names will help us in our next analysis.
print(df.columns)

#DATA ANALYSIS

#TOP 5 POPULAR ARTIST
top_five_artists = df.groupby("artist").count().sort_values(by="song_title",ascending=False)["song_title"][:5]
print(top_five_artists)

#barh function is used to draw horizontal bars
top_five_artists.plot.barh()
print(plt.show())


#TOP 5 LOUDEST TRACKS
top_five_loudest_tracks = df[["loudness","song_title"]].sort_values(by="loudness")[:5]
print(top_five_loudest_tracks)

plt.figure(figsize=(12,7 ))
sns.barplot(x="loudness", y="song_title",data=top_five_loudest_tracks)
print(plt.show())


#ARTIST WITH THE MOST DANCEABILITY SONG
top_five_danceable_song = df[["danceability","song_title","artist"]].sort_values(by="danceability",ascending=False)[:5]
print(top_five_danceable_song)
plt.figure(figsize=(12,7))
sns.barplot(x="danceability",y="artist", data=top_five_danceable_song)

# giving a title to my graph
plt.title("Artist with the most danceability song")
print(plt.show())


#TOP 10 INSTRUMENTALNESS TRACKS
top_ten_instrumentalness_track = df[["instrumentalness","song_title","artist"]].sort_values(by="instrumentalness",ascending=False)[:10]
print(top_ten_instrumentalness_track)
plt.figure(figsize=(12,7))

#plt.pie is used to create pie charts.
plt.pie(x="instrumentalness", data=top_ten_instrumentalness_track, autopct='%1.2f%%',labels=top_ten_instrumentalness_track.song_title)
plt.title("Top 10 instrumentalness tracks")

#loc= to determine which side of the tile to add
#bbox_to_anchor= the position of the tile around the chart
plt.legend(title= "Songs", loc="center left",bbox_to_anchor=(1,0,1,0.2))
print(plt.show())


#TOP 10 ENERGETIC SONGS 
top_ten_energetic_songs = df[["energy","song_title","artist"]].sort_values(by="energy", ascending=False)[:10]
print(top_ten_energetic_songs)

x=top_ten_energetic_songs['energy']
y=top_ten_energetic_songs['song_title']

plt.plot(x, y, color='green',linestyle='dashed',linewidth=3,marker='o',
    markerfacecolor='blue',markersize=12)
  
# naming the x axis
plt.xlabel('Energy')
# naming the y axis
plt.ylabel('song_title')

plt.title('Energetic Songs')
plt.legend()
print(plt.show())


#TOP 10 COMMON DURATIONS
top_ten_common_durations=  df[["duration_ms","song_title","artist"]].sort_values(by="duration_ms",ascending=False)[:10]
print(top_ten_common_durations)

sns.barplot(x="duration_ms",y="song_title", data=top_ten_common_durations)

plt.title("Most Durations Songs")
print(plt.show())



