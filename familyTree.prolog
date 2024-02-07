male(harivansh).   %harivansh is male
male(amitabh).
male(abhishek).
female(teji).      %teji is female
female(jaya).
female(swetha).
female(aishwarya).
female(aradhya).


%connections
parent(harivansh, amitabh).    %harivansh is amitabh's parent
parent(teji, amitabh)..
parent(amitabh, abhishek).
parent(amitabh, swetha).
parent(jaya, abhishek).
parent(jaya, swetha).
parent(abhishek, aradhya).
parent(aishwarya, aradhya).


%relations
mother(M,C):-female(M), parent(M,C).
father(F,C):-male(F), parent(F,C).
grandfather(GF,C):-male(GF), parent(GF,P), parent(P,C).
grandmother(GM,C):-female(GM), parent(GM,P), parent(P,C).
son(S,P):-male(S), parent(P,S).
daughter(D,P):-female(D), parent(P,D).
brother(B,S):-male(B), parent(P,B), parent(P,S).
sister(S,B):-female(S), parent(P,S), parent(P,B).
