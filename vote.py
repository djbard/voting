
import math, sys


def vote(vote_file):
    
## how many voters? 
    nvoters = 0
    for line in open(vote_file):
        cols = line.split(',')
        if len(cols)<4: ## in case there are newlines at the end of the file
            continue
        if cols[0]=="Vote_id":
            continue
        nvoters+=1

    print "number of voters:", nvoters

## set up the votes
    votes = []
    for i in range(nvoters):
        votes.append([])
        for j in range(3):
            votes[i].append(0)

## votes now has dimensions [nvoters][3]

    voter=-1
    for line in open(vote_file):
        cols = line.split(',')
        if len(cols)<4:
            continue
        if cols[0]=="Vote_id":
            continue
        voter+=1
        for c in range(1,4):
            if c==1 or c==2:
                if len(cols[c])>0:
                    v = int(cols[c])
                else:
                    v = 0
            elif c==3:
                if len(cols[c])==2: ## number + carriage return
                    v = int(cols[c][0])
                elif len(cols[c])==1: ## carriage return, OR could be last line in which case it's a vote!
                    try:
                        v = int(cols[c])
                    except:
                        v = 0

            else:
                print "gah! something has gone horribly wrong and you voted for more than three candidates!"
            votes[voter][c-1] = v
            
    print "votes:"
    print votes, "\n"

    
################################### count votes
## Count first-pref votes.

    a_1, b_1, c_1 = 0, 0, 0
    n1 = 0
    n1no = 0
    for i in range(nvoters):
        if votes[i][0]==1: ## a vote for candidate A!
            a_1+=1
            n1+=1
        elif votes[i][1]==1: ## a vote for candidate B!
            b_1+=1
            n1+=1
        elif votes[i][2]==1: ## a vote for candidate C!
            c_1+=1
            n1+=1
        else:
            print "no preference for a first place!"
            n1no+=1

## Count second-pref votes.

    a_2, b_2, c_2 = 0, 0, 0
    n2 = 0
    n2no = 0
    for i in range(nvoters):
        if votes[i][0]==2: ## a vote for candidate A!
            a_2+=1
            n2+=1
        elif votes[i][1]==2: ## a vote for candidate B!
            b_2+=1
            n2+=1
        elif votes[i][2]==2: ## a vote for candidate C!
            c_2+=1
            n2+=1
        else:
            print "no preference for a second place!"
            n2no+=1
               

## Count third-pref votes.

    a_3, b_3, c_3 = 0, 0, 0
    n3 = 0
    n3no = 0
    for i in range(nvoters):
        if votes[i][0]==3: ## a vote for candidate A!
            a_3+=1
            n3+=1
        elif votes[i][1]==3: ## a vote for candidate B!
            b_3+=1
            n3+=1
        elif votes[i][2]==3: ## a vote for candidate C!
            c_3+=1
            n3+=1
        else:
            print "no preference for a third place!"
            n3no+=1
          

##################### right! who won?

    print "n voters:", nvoters, "# candidate first place votes:", n1, " and # 'no preference' first place votes:", n1no

## is there a clear first-round winner?
    majority = math.ceil((n1+1)/2.) ## rounding up.
    
    print "the majority required to win in round 1 of the election is", majority
    
    
    print "\n############## first round of voting"
    
    print "first round votes: ", a_1, b_1, c_1
    if a_1>=majority:
        print "*** Candidate A is the clear winner! *** \n (with", a_1, "votes)"
    elif b_1>=majority:
        print "*** Candidate B is the clear winner! ***\n (with", b_1, "votes)"
    elif c_1 >=majority:
        print "*** Candidate C is the clear winner! ***\n (with", c_1, "votes)"
    else:
        print "no candidate has the overall majority! Let's drop one of them. "


        
    
    ########################## Who do we drop?
        drop = "x"
        if a_1>b_1:
            if b_1>c_1: ## c is lowest
                print "Candidate C has the least first-place votes"
                drop = "c"
            elif c_1>b_1: ## b is the lowest
                print "Candidate B has the least first-place votes"
                drop = "b"
            elif c_1==b_1: ## tie-break between b and c! 
                print "A has most votes, but we have a tie-break between B and C for who to drop..."
            ## who has the fewst 2nd place votes?
                if c_2>b_2:
                    print "Candidate B has the least second-place votes"
                    drop = "b" 
                elif b_2>c_2:
                    print "Candidate C has the least second-place votes"
                    drop = "c"
                elif b_2==c_2: ## tie-break for second place!
                    print "B and C have the same second-place votes"
                    print "!!!!!!!!!!!!!!! need a new election!!!!!!!!!!!!!!!"
                
        elif b_1>c_1:
            if a_1>c_1: ## c is lowest
                print "Candidate C has the least first-place votes"
                drop = "c"
            elif c_1>a_1: ## a is lowest
                print "Candidate A has the least first-place votes"
                drop = "a"
            elif a_1==c_1: ## tie-break between a and c!
                print "B has most votes, but we have a tie-break between A and C for who to drop..."
            ## who has fewest 2nd place votes? 
                if a_2>c_2:
                    print "Candidate C has the least second-place votes"
                    drop = "c"
                elif c_2>a_2:
                    print "Candidate A has the least second-place votes"
                    drop = "a"
                elif c_2==a_2: ## tie-break for second place! 
                    print "A and C have the same second-place votes"
                    print "!!!!!!!!!!!!!! need a new election!!!!!!!!!!!!!!!"
                
        elif c_1>a_1:
            if a_1>b_1: ## b is lowest
                print "Candidate B has the least first-place votes"
                drop = "b"
            elif b_1>a_1:
                print "Candidate A has the least first-place votes"
                drop = "a"
            elif a_1==b_1: ## ties-break between a and b!
                print "C has most votes, but we have a tie-break between A and B for who to drop..."
            ## who has fewest 2nd-pref votes? 
                if a_2>b_2:
                    print "Candidate B has the least second-place votes"
                    drop = "b"
                elif b_2>a_2:
                    print "Candidate A has the least second-place votes"
                    drop = "a"
                elif a_2==b_2: ## tie-break for second place! 
                    print "A and B have the same second-place votes"
                    print "!!!!!!!!!!!!!! need a new election!!!!!!!!!!!!!!!"

                
        elif a_1==b_1==c_1: ## it's entirely possilbe we'll get a three-way tie. 
            print "three-way tie! how exciting. We will eliminate whoever had the least second-place votes. "
        ### we drop whoever got the least second-place votes. 
            if a_2>b_2:
                if b_2>c_2:
                    print "Candidate C has the least second-place votes"
                    drop = "c"
                elif c_2>b_2:
                    print "Candidate B has the least second-place votes"
                    drop = "b"
                else:
                    "!!!!!!!!!!!!!!!! B and C have equal second-place votes! New election please!!!!!!!!!!!!"
            elif b_2>c_2:
                if a_2>c_2:
                    print "Candidate C has the least second-place votes"
                    drop = "c"
                elif c_2>a_2:
                    print "Candidate A has the least second-place votes"
                    drop = "a"
                else:
                    "!!!!!!!!!!!!!!!! A and C have equal second-place votes! New election please!!!!!!!!!!!!"
            elif c_2>a_2:
                if a_2>b_2:
                    print "Candidate B has the least second-place votes"
                    drop = "b"
                elif b_2<a_2:
                    print "Candidate A has the least second-place votes"
                    drop = "a"
                else:
                    "!!!!!!!!!!!!!!!! A and B have equal second-place votes! New election please!!!!!!!!!!!!"
            
        
        ### by now we should have decided what to drop. 
        if drop=="a":
            print "-> we're dropping candidate A"
            drop_no = 0
        elif drop=="b":
            print "-> we're dropping candidate B"
            drop_no = 1
        elif drop=="c":
            print "-> we're dropping candidate C"
            drop_no = 2
        else:
            print "!!!!!!!!!!!!!!!!!!!!!!!!!! unbeatable tie for first place! Start again!!!!!!!!!!!!!!!!!"
            return 
       
        print "\n############## second round of voting"

    ############################# second round
    ## if someone voted for the dropped candidate, we're going to reassign their votes to their second choice cnadidate.
    ## we want to retain teh initial first-round votes.
        a_11 = a_1
        b_11 = b_1
        c_11 = c_1
        for i in range(nvoters):
            if votes[i][drop_no]==1:
                print "this voter chose the dropped candidate:", votes[i]
                if votes[i][0]==2: ## second choice vote for A
                    a_11+=1
                elif votes[i][1]==2: ## second choice vote for B
                    b_11+=1
                elif votes[i][2]==2: ## second choice vote for C
                    c_11+=1
                    
    ### note: majority is different from before. Needs to be majority of *remaining* votes, after a candidate has been dropped. There may now be some no-preference votes

        if drop=="a":
            print "second round votes: ", b_11, c_11
            majority2 = math.ceil((b_11 + c_11+1)/2.)
            print "the majority required to win in this round is:", majority2
            if b_11>=majority2:
                print "*** Candidate B is the winner! ***\n (with", b_11, "votes)"
            elif c_11>=majority2:
                print "*** Candidate C is the winner! ***\n (with", c_11, "votes)"
            else:
                print "no candidate has the overall majority! which one had the least first-round votes? "
        ## find which cand had the most first round votes - they win.
        ####
                if b_1>c_1:
                    print "*** Candidate B is the winner! *** \n (with", b_11, " total votes and", b_1, "initial first-round votes)"
                elif c_1>b_1:
                    print "*** Candidate C is the winner! *** \n (with", c_11, " total votes and", c_1, "initial first-round votes)"
                else:
                ## go to second-place initial votes.
                    print "Both B and C have the same inital first-place votes; moving to second-place votes"
                
                    if b_2>c_2:
                        print "*** Candidate B is the winner! *** \n (with", b_11, " total votes,", b_1, "initial first-round votes and", b_2, "initial second-round votes)"
                    elif c_2>b_2:
                        print "*** Candidate C is the winner! *** \n (with", c_11, " total votes,", c_1, "initial first-round votes and", c_2, "initial second-place votes)"
                    else:
                        print "B and C have the same second-place votes"
                        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! need another election!!!!!!!!!!!!!!!!!!!!!!"
                        return

    ####
        elif drop=="b":
            print "second round votes: ", a_11, c_11
            majority2 = math.ceil((a_11 + c_11+1)/2.)
            print "the majority required to win in this round is:", majority2
            if a_11>=majority2:
                print "*** Candidate Ais the winner! ***\n (with", a_11, "votes)"
            elif c_11>=majority2:
                print "*** Candidate C is the winner! ***\n (with", c_11, "votes)"
            else:
                print "no candidate has the overall majority! which one had the least first-round votes? "
            
        ## find which cand had the most first round votes - they win.
        ####
                if a_1>c_1:
                    print "*** Candidate A is the winner! *** \n (with", a_11, " total votes and", a_1, "initial first-round votes)"
                elif c_1>a_1:
                    print "*** Candidate C is the winner! *** \n (with", c_11, " total votes and", c_1, "initial first-round votes)"
                else:
                ## go to second-place initial votes.
                    print "Both A and C have the same inital first-place votes; moving to second-place votes"
                    
                    if a_2>c_2:
                        print "*** Candidate A is the winner! *** \n (with", a_11, " total votes,", a_1, "initial first-round votes and", a_2, "initial second-round votes)"
                    elif c_2>a_2:
                        print "*** Candidate C is the winner! *** \n (with", c_11, " total votes,", c_1, "initial first-round votes and", c_2, "initial second-place votes)"
                    else:
                        print "A and C have the same second-place votes"
                        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! need another election!!!!!!!!!!!!!!!!!!!!!!"
                        return

    ####
        elif drop =="c":
            print "second round votes: ", a_11, b_11
            majority2 = math.ceil((a_11 + b_11+1)/2.)
            print "the majority required to win in this round is:", majority2
            if a_11>=majority2:
                print "*** Candidate Ais the winner! ***\n (with", a_11, "votes)"
            elif b_11>=majority2:
                print "*** Candidate B is the winner! ***\n (with", b_11, "votes)"
            else:
                print "no candidate has the overall majority! which one had the least first-round votes? "
            
        ## find which cand had the most first round votes - they win.
        ####
                if a_1>b_1:
                    print "*** Candidate A is the winner! *** \n (with", a_11, " total votes and", a_1, "initial first-round votes)"
                elif b_1>a_1:
                    print "*** Candidate B is the winner! *** \n (with", b_11, " total votes and", b_1, "initial first-round votes)"
                    
                else:
                ## go to second-place initial votes.
                    print "Both A and B have the same inital first-place votes; moving to second-place votes" 
                    
                    if a_2>b_2:
                        print "*** Candidate A is the winner! *** \n (with", a_11, " total votes,", a_1, "initial first-round votes and", a_2, "initial second-round votes)"
                    elif b_2>a_2:
                        print "*** Candidate B is the winner! *** \n (with", b_11, " total votes,", b_1, "initial first-round votes and", b_2, "initial second-place votes)"
                    else:
                        print "A and B have the same second-place votes"
                        print "!!!!!!!!!!!!!!!!!!!!!!!!!!! need another election!!!!!!!!!!!!!!!!!!!!!!"
                        return


                

# ======================================================================

if __name__ == '__main__':

         
    vote_file = sys.argv[1]

    vote(vote_file)

# ======================================================================
