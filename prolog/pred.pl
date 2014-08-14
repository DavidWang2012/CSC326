h([X,_],[X]).
h([X],[X]).
h([X,_ | Rx],[X | Ry]) :- h(Rx,Ry).
