male(charlie).
male(bob).
female(eve).
female(alice).
parent(charlie,bob).
parent(eve,bob).
parent(charlie,alice).
parent(eve,alice).
sibling(X,Y):-
    parent(P,X),parent(P,Y).
    /*X =\= Y.*/
