"""

    We build software to solve problems. But programmers are often too focused on
solving a problem to determine whether a solution to the problem already exists.
Even if the programmer knows the problem has been solved in similar cases, it’s not
clear that the existing code will actually fit the specific problem facing the program‐
mer. Ultimately, it isn’t easy to find code in a given programming language that can
be readily modified to solve the problem.
    We can think of algorithms in different ways. Many practitioners are content to look
up an algorithm in a book or on some website, copy some code, run it, maybe even
test it, and then move on to the next task. In our opinion, this process does not
improve one’s understanding of algorithms. In fact, this approach can lead you
down the wrong path where you select a specific implementation of an algorithm.
In this chapter, we present the format we
use to describe the algorithms in this book. We also summarize the common algo‐
rithmic approaches used to solve problems.

******************* Algorithm Template Format ******************
The real power of using a template to describe each algorithm is that you can
quickly compare and contrast different algorithms and identify commonalities in
seemingly different algorithms. Each algorithm is presented using a fixed set of sec‐
tions that conform to this template.

************** Name

A descriptive name for the algorithm. We use this name to communicate concisely
the algorithm to others

************** Input/Output
Describes the expected format of input data to the algorithm and the resulting val‐
ues computed.

************* Context
A description of a problem that illustrates when an algorithm is useful and when it
will perform at its best.
A description of the properties of the problem / solution that
must be addressed and maintained for a successful implementation. They are the
things that would cause you to choose this algorithm specifically.
********** Solution
The algorithm description using real working code with documentation. All code
solutions can be found in the associated code repository.

*********** Analysis
A synopsis of the analysis of the algorithm, including performance data and infor‐
mation to help you understand the behavior of the algorithm. Although the analysis
section is not meant to “prove” the described performance of an algorithm, you
should be able to understand why the algorithm behaves as it does. We will provide
references to actual texts that present the appropriate lemmas and proofs to explain
why the algorithms behave as described.

******* Variations
Presents variations of the algorithm or different alternatives.

********************* Pseudocode Template Format
********************* Empirical Evaluation Format
Floating-Point Computation
Performance

***************** Common Approaches
**** Greedy
A Greedy strategy completes a task of size n by incrementally solving the problem
in steps. At each step, a Greedy algorithm will make the best local decision it can
given the available information, typically reducing the size of the problem being
solved by one. Once all n steps are completed, the algorithm returns the computed
solution.

****** Divide and Conquer
A Divide and Conquer strategy solves a problem of size n by dividing it into two
independent subproblems, each about half the size of the original problem. Quite
often the solution is recursive, terminating with a base case that can be solved triv‐
ially. There must be some resolution computation that can determine the solution
for a problem when given two solutions for two smaller subproblems.
Note that you can more rapidly find the
largest element in a collection by scanning each element and storing the largest one
found. Let this be a brief reminder that Divide and Conquer will not always provide
the fastest implementation

************** Dynamic Programing
Dynamic Programming is a variation on Divide and Conquer that solves a problem
by subdividing it into a number of simpler subproblems that are solved in a specific
order. It solves each smaller problem just once and stores the results for future
use to avoid unnecessary recomputation. It then solves problems of increasing size,
composing together solutions from the results of these smaller subproblems.
In many cases, the computed solution is provably optimal for the problem being
solved

Dynamic Programming is frequently used for optimization problems where the
goal is to minimize or maximize a particular computation.

"""