sumlist([],0).
sumlist([X|Rest],Ans) :- sumlist(Rest,Partial),
                          Ans is Partial+X.
