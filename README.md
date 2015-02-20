Simple code to calculate the results of an election. 
Thus far, I've implemented a specific form of Instant Runoff voting for an election with three candidates and a 'no preference' option. 
How it works:

1) If one candidate has a clear majority (>50%) of the first-place votes. then they are the winner and the election ends there. 

2) If there is no clear majority, then the candidate with the fewest first-place votes is elimininated. The voters who picked this candidate as first-place have their second-place votes assigned to the remaining two candidates (or not, in the case of a 'no preference' vote). 

	a) If there are two candidates with equally low first-place votes (or if all three have equal first-place votes), the candidate with the fewest second-place votes is eliminated. 
	b) If this doesn't work, then we have to re-start the election. 

3) The remaining two candidates now face-off, with new vote totals based on the additional second-place votes. If one has a clear majority now, then they are the winner. 
	a) If both have equal votes, then we again look to the second-place votes and eliminate the candidate with the fewest second-place votes. 
