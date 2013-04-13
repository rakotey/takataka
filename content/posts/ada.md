Title: Ada 2012: Ada With Contracts
tags: ada, contracts
date: 17-04-2013


The most important new feature in Ada 2012 is support for contract-based programming, which adds more validation of mission-critical code to a language already famous for its focus on reliability.
The most recent version of the Ada standard, known as Ada 2012, brings contract-based programming to a mainstream language. Preconditions, postconditions, type invariants, and subtype predicates allow software developers to specify their programs' intent more clearly, in effect embedding requirements into the source code. This feature makes it easier to review and understand the program, and it facilitates verification by the compiler, static analysis tools, and/or runtime checks.

"New, Improved" or "No, Unproved"?
In the software world, we are used to getting new versions of things all the time. Nearly every software product undergoes frequent revision, and companies dutifully trot out press releases to trumpet the wonderful new features in each version. In practice, these updates are often not that significant or newsworthy.

Programming languages follow a similar revision pattern. For example, a new version of C, referred to as C11, was released last year. New versions of languages typically have many new features, and to those in the language design business, these always seem like major advances. However, the wonderful improvements often don't make that much difference in practice. Indeed the style of a lot of C coding has not much changed since the Kernighan and Ritchie days 35 years ago. Most C programmers don't use the new features in C99, let alone the ones that recently appeared in C11.
