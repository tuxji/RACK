:- module(unidentified_hazard, [check_unidentified_hazards/0]).

:- use_module(library(semweb/rdf11)).
:- use_module('../rack_model').

prolog:message(unidentified_hazard(Class)) -->
    [ 'Unidentified hazard ~w'-[Class] ].

% Copied from check_rack.pl, ideally should be in some shared module
warn_if_nonzero(What, Count) :-
    Count > 0, !,
    print_message(warning, num_classes(What, Count)).
warn_if_nonzero(_, _).

check_unidentified_hazard(Hazard) :-
    rack_instance('HAZARD#HAZARD', Hazard),
    \+ rdf(Hazard, owl:identified, _),
    print_message(warning, unidentified_hazard(Hazard)).

check_unidentified_hazards :-
    findall(UH, check_unidentified_hazard(UH), UHS),
    length(UHS, UHSLen),
    warn_if_nonzero("with unidentified hazards", UHSLen),
    (UHSLen == 0, !,
     format('No unidentified hazard found~n') ; format('FOUND UNIDENTIFIED HAZARD(S)~n')),
    true.