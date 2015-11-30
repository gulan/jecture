-module(convert).
-export([as_centimeter/2, x_as_y/2, factors/2, x_to_y/2, rnd/1, test/0]).

as_centimeter(N, inch) -> N / 2.54;
as_centimeter(N, centimeter) -> N;
as_centimeter(N, foot) -> as_centimeter(12 * N, inch);
as_centimeter(N, yard) -> as_centimeter(3 * N, foot);
as_centimeter(N, mile) -> as_centimeter(1760 * N, yard).

x_as_y({N, inch}, centimeter) -> {as_centimeter(N, inch), centimeter};
x_as_y({N, centimeter}, inch) -> {2.54 * N, inch};
x_as_y({N, mile}, centimeter) -> {as_centimeter(N, mile), centimeter};
x_as_y({N, centimeter}, mile) -> {N / (2.54 * 12 *3 * 1760), mile}.

factors(inch, centimeter) -> 2.54;
factors(foot, centimeter) -> 12 * 2.54;
factors(yard, centimeter) -> 3 * 12 * 2.54;
factors(mile, centimeter) -> 1760 * 3 * 12 * 2.54;
factors(milimeter, centimeter) -> 0.1;
factors(meter, centimeter) -> 100;
factors(kilometer, centimeter) -> 100 * 1000;
factors(centimeter, centimeter) -> 1;
factors(centimeter, X) -> 1.0 / factors(X, centimeter).

x_to_y({N, X}, Y) ->
    C = N * factors(X,centimeter),
    {C * factors(centimeter, Y), Y}.

rnd({N, U}) ->
    {round(N), U}.

test() ->
    (convert:x_to_y({1,foot}, inch) == {12.0,inch})
	and (convert:x_to_y({1,foot}, inch) == {12.0, inch})
	and (convert:x_to_y({1,inch}, foot) == {1/12, foot})
	and (rnd(convert:x_to_y({5,mile}, kilometer)) == {8, kilometer}).
	




