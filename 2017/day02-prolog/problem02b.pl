:- meta_predicate maplist(2, ?, ?).

answer(List, Answer) :-
    maplist(list_val_b, List, EachVal),
    sum_list(EachVal, Answer).


list_val_b(L, Val) :-
    member(El1,L),
    member(El2,L),
    El1>El2,
    number(El1),
    number(El2),
    divmod(El1,El2,_,0),
    Val is El1/El2.


/**
[[5,9,2,8],[9,4,7,3],[3,8,6,5]]

**/
