Simple code to calculate the results of an election. 
Thus far, I've implemented a specific form of Instant Runoff voting for an election with three candidates and a 'no preference' option. 
How it works:
1) If one candidate has a clear majority (>50%) of the first-place votes. then they are the wonnder and the election ends there, 
2) If there is no clear majority, then the candidate with teh  fewest first-place votes is elimininated. The voters who picked this candidate as fiorst-place have their second-place votes assigned to the remaining teo candidates (or nonot, if they have prvnce)
