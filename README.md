Simple code to calculate the results of an election. 
Thus far, I've implemented a specific form of Instant Runoff voting for an election with three candidates and a 'no preference' option. 
How it works (based on the [LSST DESC spokesperson election rules][rules]):

1) If one candidate has a clear majority (>50%) of the first-place votes. then they are the winner and the election ends there. 

2) If there is no clear majority, then the candidate with the fewest first-place votes is elimininated. The voters who picked this candidate as first-place have their second-place votes assigned to the remaining two candidates (or not, in the case of a 'no preference' vote). 

  a) If there are two candidates with equally low first-place votes (or if all three have equal first-place votes), the candidate with the fewest second-place votes is eliminated. 
  
  b) If this doesn't work, then we have to re-start the election. 

3) The remaining two candidates now face-off, with new vote totals based on the additional second-place votes. If one has a clear majority now, then they are the winner. 

  a) If both have equal votes, we look at which candidate had the most initial first-place votes.  
  
  b) If both still have equal votes, then we again look to the second-place votes and eliminate the candidate with the fewest second-place votes. 


The vote file formats are quite specific - they should be in csv format with the first line giivng the candidate names, and subsequent lines giving the voter ID, and their preferences. A 'no preference' vote is a 0 or no entry. 
For example:

	Voter_ID,CandA,CandB,CandC
	Voter1,1,2,3
	Voter2,3,1,2
	Voter3,2,3,1
	Voter4,1,,, 
	Voter5,3,,,

I have included one simple example of election results (test_votes.csv) which illustrates a couple of tie-break scenarios: Candidate A is eliminated in the first round, then candidates B and C are tied for first place in the second round. C wins that tiebreaker based on the number of initial first-round votes. 

To run:

	python InstantRunoff.py test_votes.csv

[rules]:https://confluence.slac.stanford.edu/display/LSSTDESC/2015+Spokesperson+Election+Rules
