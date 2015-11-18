Jecture
-------
As in 'conjecture'.

The sub-projects of Jecture *look* like test suites for programming
APIs, but testing is not the purpose of the code. The main goal is to
have a collection of minimal examples of how each feature of an API is
used.

Other sources of information often prove inadequate.

* Man pages usually give no examples.

* Tutorials usually provide contrived applications, which just
  clutters subject matter.

* Searching production code bases is can take a lot of time, and the
  code found is entangled with uninteresting code.

* Real test suites need to combat copy-and-paste code, and provide
  elaborate scheduling and reporting facilities. Complying with these
  additional requirements makes it hard to see just the code that acts
  with the API.

I want this code to be easy to browse and easy to search.

The whole enterprise is structured as test suites because,

* it makes to easy to present an exhaustive exploration of an API, and

* I don't need to invent tiny demo applications. I just use asserts,
  and focus the exploration at the level of values and syntax.

Most of the tests are of the do-this and expect-that variety. I hope
to add more property based tests, because knowing the invariants is
the best way to understand and remember.
