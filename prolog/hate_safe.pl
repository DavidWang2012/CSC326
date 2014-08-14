woman(jane).
woman(manlyn).
famous(manlin).
loves(john,X):-woman(X),famous(X).
hates(john,X):-woman(X),not(loves(john,X)).

