
import math, sys


def vote(vote_file):
    cand_names = []
## how many voters? 
    nvoters = 0
    for line in open(vote_file):
        cols = line.split(',')
        if len(cols)<3: ## in case there are newlines at the end of the file
            continue
        if cols[0]=="Vote_id":
            cand_names.append(cols[1])
            cand_names.append(cols[2])
            cand_names.append(cols[3])
            cand_names.append(cols[4][:-1]) ## avoid carriage return
            continue
        nvoters+=1

    print "number of voters:", nvoters
    print "Candidate A is", cand_names[0]
    print "Candidate B is", cand_names[1]
    print "Candidate C is", cand_names[2]
    print "Candidate D is", cand_names[3]
    
## set up the votes
    votes = []
    for i in range(nvoters):
        votes.append([])
        for j in range(4):
            votes[i].append(0)

## votes now has dimensions [nvoters][3]

    voter=-1
    for line in open(vote_file):
        cols = line.split(',')
        if len(cols)<3:
            continue
        if cols[0]=="Vote_id":
            continue
        voter+=1
        for c in range(1,5):
            if c==1 or c==2 or c==3:
                if len(cols[c])>0:
                    v = int(cols[c])
                else:
                    v = 0
            elif c==4:
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

    a_1, b_1, c_1, d_1 = 0, 0, 0, 0
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
        elif votes[i][3]==1: ## a vote for candidate D!
            d_1+=1
            n1+=1
        else:
            n1no+=1

## Count second-pref votes.

    a_2, b_2, c_2, d_2 = 0, 0, 0, 0
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
        elif votes[i][3]==2: ## a vote for candidate D!
            d_2+=1
            n2+=1
        else:
            n2no+=1
               

## Count third-pref votes.

    a_3, b_3, c_3, d_3 = 0, 0, 0, 0
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
        elif votes[i][3]==3: ## a vote for candidate C!
            d_3+=1
            n3+=1
        else:
            n3no+=1
          
## Count fourth-pref votes.

    a_4, b_4, c_4, d_4 = 0, 0, 0, 0
    n4 = 0
    n4no = 0
    for i in range(nvoters):
        if votes[i][0]==4: ## a vote for candidate A!
            a_4+=1
            n4+=1
        elif votes[i][1]==4: ## a vote for candidate B!
            b_4+=1
            n4+=1
        elif votes[i][2]==4: ## a vote for candidate C!
            c_4+=1
            n4+=1
        elif votes[i][3]==4: ## a vote for candidate C!
            d_4+=1
            n4+=1
        else:
            n4no+=1
          

##################### right! who won?
    winner = -100
            
    print "# voters:", nvoters, ", # candidate first place votes:", n1, ", and # 'no preference' first place votes:", n1no

## is there a clear first-round winner?
    majority = math.ceil((n1+1)/2.) ## rounding up.
    
    print "the majority required to win in round 1 of the election is", majority
    
    
    print "\n############## first round of voting"
    
    print "first round votes: A:", a_1, ", B:", b_1, ", C:", c_1, ", D:", d_1
    if a_1>=majority:
        print "*** Candidate A ("+cand_names[0]+") is the clear winner! *** \n (with", a_1, "votes)"
    elif b_1>=majority:
        print "*** Candidate B ("+cand_names[1]+") is the clear winner! ***\n (with", b_1, "votes)"
    elif c_1 >=majority:
        print "*** Candidate C ("+cand_names[2]+") is the clear winner! ***\n (with", c_1, "votes)"
    elif d_1 >=majority:
        print "*** Candidate D ("+cand_names[3]+") is the clear winner! ***\n (with", d_1, "votes)"
    else:
        print "no candidate has the overall majority! Let's drop one of them. "


        
    
        ########################################################################## Who do we drop?
        cands = ["A", "B", "C", "D"]
        round1 = [a_1, b_1, c_1, d_1]
        round2 = [a_2, b_2, c_2, d_2]
        round3 = [a_3, b_3, c_3, d_3]
        round4 = [a_4, b_4, c_4, d_4]
        drop_no = 0
        ## who has the minimum first-round votes?
        idx = [i for i, x in enumerate(round1) if x == min(round1)]
        if len(idx)==1: ## let's hope it's this simple
            print "dropping candidate ", cands[idx[0]]
            drop_no = idx[0]
        elif len(idx)==2:
            print "conflict! Tie for who to drop between ", cands[idx[0]], " and ", cands[idx[1]]
            print "going to second-place votes for these two..."
            round22 = [round2[idx[0]], round2[idx[1]]]
            idx2 = [i for i, x in enumerate(round22) if x == min(round22)]
            print "dropping candidate ", cands[idx2[0]]
            drop_no = idx2[0]
            
            
        elif len(idx)==3:
            print "conflict! Tie for who to drop between ", cands[idx[0]], " and ", cands[idx[1]], " and ", cands[idx[2]]
            print "going to second-place votes for these three..."
            round23 = [round2[idx[0]], round2[idx[1]], round2[idx[2]]]
            idx3 = [i for i, x in enumerate(round23) if x == min(round23)]
            print "dropping candidate ", cands[idx3[0]]
            drop_no = idx3[0]

        ################ OK! Now we drop someone, and re-assign votes.
        
        print "\n############## second round of voting"
        
        ## 
        ## if someone voted for the dropped candidate, we're going to reassign their votes to their second choice cnadidate.
        ## we want to retain teh initial first-round votes.
        a_11 = a_1
        b_11 = b_1
        c_11 = c_1
        d_11 = d_1
        
        for i in range(nvoters):
            if votes[i][drop_no]==1:
                print "this voter chose the dropped candidate:", votes[i]
                if votes[i][0]==2 and drop_no!=0: ## second choice vote for A
                    a_11+=1
                elif votes[i][1]==2 and drop_no!=1: ## second choice vote for B
                    b_11+=1
                elif votes[i][2]==2 and drop_no!=2: ## second choice vote for C
                    c_11+=1
                elif votes[i][3]==2 and drop_no!=3: ## second choice vote for D
                    d_11+=1

        
        ### note: majority is different from before. Needs to be majority of *remaining* votes, after a candidate has been dropped. There may now be some no-preference votes
        count1 = [a_11, b_11, c_11, d_11]
        count2 = []
        round2_2nd = [] ## 2nd-place votes are just carried forward
        round2_3rd = [] ## 3rd-place votes are just carried forward
        cands2 = []
        for i in range(4):
            if i==drop_no:
                continue
            else:
                count2.append(count1[i])
                cands2.append(cands[i])
                round2_2nd.append(round2[i])
                round2_3rd.append(round3[i])
                
        print "remaining candidates: ", cands2
        print "second round votes: ", count2
        majority2 = math.ceil( (sum(count2)+1) /2.)
        print "the majority required to win in this round is:", majority2
        if count2[0]>majority2:
            print "**** winner is: ", cands[0]
        elif count2[1]>majority2:
            print "**** winner is: ", cands[1]
        elif count2[2]>majority2:
            print "**** winner is: ", cands[2]
        else:
            print "no clear winner in second round - dropping the candidate with the least votes..."
            ## OK, there's no clear winner with the re-assigned votes. Someone needs to get dropped!
            ## Who has the least 2nd-tier votes?

            idx = [i for i, x in enumerate(count2) if x == min(count2)]
            if len(idx)==1: ## let's hope it's this simple
                print "dropping candidate ", cands2[idx[0]]
                drop_no_2 = idx[0]
                
            elif len(idx)==2:
                print "conflict! Tie for who to drop between ", cands2[idx[0]], " and ", cands2[idx[1]]
                cands2_2nd = [cands2[idx[0]], cands2[idx[1]] ]
                
                print "who has the least second-place votes (in the first round)?..."
                ## This might not be the correct thing. I haven't re-dsitributed second-place votes, only first-place votes from voters who voted for the eliminated candidate.
               
                
                round23 = [round2_2nd[idx[0]], round2_2nd[idx[1]]]
                print "second-place candidates:", cands2_2nd
                print "second-place votes:", round23
                idx2_2 = [i for i, x in enumerate(round23) if x == min(round23)]
                print "dropping candidate ", cands2_2nd[idx2_2[0]]
                

            ## #OK - who is left?
            ################# Third round of vote re-distribution
            print "\n############## Third round of voting"

            ## make sure I get the right cand idx that was dropped - looking at the full list of cands
            drop_no2 = 0
            for kk in range(4):
                if cands[kk]==cands2_2nd[idx2_2[0]]:
                    drop_no2 = kk

            a_21 = a_11
            b_21 = b_11
            c_21 = c_11
            d_21 = d_11


            ## who do we have left?
            
            count2 = [a_21, b_21, c_21, d_21]
            tmp, tmp2 = [], []
            for i in range(4):
                if i==drop_no or i==drop_no2:
                    continue
                else:
                    tmp.append(count2[i])
                    tmp2.append(cands[i])
            print "Remaining candidates: ", tmp2
            print "They have votes:", tmp
            print "Looking for second-place votes to take from candidate", cands2_2nd[idx2_2[0]], " and give to candidates", tmp2
            
            for i in range(nvoters):
                if  votes[i][drop_no2]==1:
                    print "this voter chose the dropped candidate:", votes[i]
                    if votes[i][0]==2 and drop_no2!=0: ## second choice vote for A
                        a_21+=1
                    elif votes[i][1]==2 and drop_no2!=1: ## second choice vote for B
                        b_21+=1
                    elif votes[i][2]==2 and drop_no2!=2: ## second choice vote for C
                        c_21+=1
                    elif votes[i][3]==2 and drop_no2!=3: ## second choice vote for D
                        d_21+=1

            count2 = [a_21, b_21, c_21, d_21]
            round3_2nd = [] ## 2nd-place votes are just carried forward
            round3_3rd = [] ## 3rd-place votes are just carried forward
            cands2 = []
            cands3 = []
            count3 = []

            
            for i in range(4):
                if i==drop_no or i==drop_no2:
                    continue
                else:
                    count3.append(count2[i])
                    cands3.append(cands[i])
                    round3_2nd.append(round2[i]) ## again, not transferring 2nd/3rd place votes
                    round3_3rd.append(round3[i])
                
            print "remaining candidates: ", cands3
            print "third round votes: ", count3
            
            majority3 = math.ceil( (sum(count3)+1) /2.)
            print "the majority required to win in this round is:", majority3
            if count3[0]>majority3:
                print "**** winner is: ", cands3[0]
            elif count3[1]>majority3:
                print "**** winner is: ", cands3[1]
            else:
                print "tie-break in third round - dropping the candidate with the least second-place votes..."
                ## OK, there's no clear winner with the re-assigned votes. Someone needs to get dropped!

                print "second-place votes are:", round3_2nd
                idx3 = [i for i, x in enumerate(round3_2nd) if x == min(round3_2nd)]
                if len(idx3)==1: ## let's hope it's this simple
                    print "dropping candidate ", cands3[idx3[0]]
                    if idx3[0]==0:
                        win = 1
                    else:
                        win=0
                    print "********* AND THE WINNER IS CANDIDATE ", cands3[win]
                    print "( who is ", cand_names[idx3[0]], ")"
                else:
                    print "well, they have identical second-place votes in teh first round! Let's look at third-place votes in teh first round..."
                    
                    idx3_3 = [i for i, x in enumerate(round3_3rd) if x == min(round3_3rd)]
                    if len(idx3_3)==1: ## let's hope it's this simple
                        print "dropping candidate ", cands3[idx3_3[0]]
                        print idx3_3[0]
                        if idx3_3[0]==0:
                            win = 1
                        else:
                            win=0
                        print "********* AND THE WINNER IS CANDIDATE ", cands3[win]
                
            
            


            
            
        
        ####

# ======================================================================

if __name__ == '__main__':

         
    vote_file = sys.argv[1]

    vote(vote_file)

# ======================================================================
