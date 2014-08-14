woman(jane).
woman(manlyn).
famous(manlin).
loves(john,X):-woman(X),famous(X).
hates(john,X):-not(loves(john,X)).

