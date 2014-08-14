overlap(S1,S2) :- member(X,S1),member(X,S2).
disjoint(S1,S2) :- \+(overlap(S1,S2)).
