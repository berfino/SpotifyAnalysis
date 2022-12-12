import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#Multiple Feature Plots
#It is used for the color of the axes.
sns.set_style("darkgrid")

#Load Dataset
df= pd.read_csv("D:\Projects\SpotifyDatasetAnalysis\data.csv") 
interest_feature_cols =["tempo","loudness","acousticness", "danceability", "duration_ms", "energy",
        "instrumentalness","liveness","speechiness","valence"]

for feature_col in interest_feature_cols:
     pos_data = df[df["target"] == 1][feature_col]
     neg_data = df[df["target"] == 0][feature_col]

     plt.figure(figsize=(10,7))
     sns.distplot(pos_data, bins=30, label="Positive", color="green")
     sns.distplot(neg_data, bins=30, label="Negative", color="red")
     
     plt.legend(loc="upper right")
     plt.title(f"Positive and Negative Histogram Plot For {feature_col}")
     print(plt.show())


