/**
[[5, 1, 9, 5],[7, 5, 3],[2, 4, 6, 8]]
**/


list_min([L|Ls], Min) :- foldl(num_num_min, Ls, L, Min).

num_num_min(X, Y, Min) :- Min is min(X, Y).

list_max([L|Ls], Max) :- foldl(num_num_max, Ls, L, Max).

num_num_max(X, Y, Max) :- Max is max(X, Y).

list_val(L, Val) :- 
    list_max(L,Max1), 
    list_min(L,Min1), 
    Val is Max1-Min1.

:- meta_predicate maplist(2, ?, ?).

answer(List, Answer) :-
    maplist(list_val, List, EachVal),
    sum_list(EachVal, Answer).
