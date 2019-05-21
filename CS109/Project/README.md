# CS109FinalProject

## Introduction 
League of Legends (LoL) is currently the most popular game in the world. LoL is a fast-paced, competitive online game that blends the speed and intensity of an RTS with RPG elements. Two teams of 5 powerful champions, each with a unique design and playstyle, battle head-to-head across multiple battlefields and game modes. With an ever-expanding roster of champions, frequent updates and a thriving tournament scene, League of Legends offers endless replayability for players of every skill level.

The main objective of the game is to knock down the enemies' towers using the champions, while the enemy team is trying to do the same to ours. Towers are difficult to destroy with the enemy defending them, so most of the game revolves around killing enemy champions in order to buy the necessary time to bring down enemy towers.

Team composition is extremely important in the game. Each champion out of the roster of 128 (and growing!) carries its own unique abilities, utility, and play style that it can contribute to the team. Simply put, a team of 5 champions that share similar roles in the game would be very ineffective against a well-balanced team. 

Given our motivation:
1. Find common characteristics of champions and group them
2. Predict which team will win in a match based on the clusters the players belong to

In order to achieve these goals, we used a variety of techniques:
1. Principal Component Analysis
2. k Nearest Neighbors
3. Support Vector Machine
4. Logistic with Lasso
5. DP-means

## File Structure 

final_unnormalized.csv: contains the parsed data of the JSON files 

centroid.csv: contains mean values of 8 clusters

test.csv: contains proabablities each champion being assigned to a particular cluster

wombocombo.ipynb: the master ipython notebook file that contains all the code and explanation in a typical CS109 homework format

Standard Riot Game’s API was used to download 90000 match data

Includes EDA, clustering algorithms, and match prediction based on team composition
