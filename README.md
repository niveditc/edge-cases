#Effect of Edge Cases on Coding Practices

An experiment was performed to test the effect of giving thought to edge cases before begininng coding. For more information see [details on the experiment](https://www.dropbox.com/s/7mme81otm1bpytc/EdgeCases.pdf?dl=0)
and [instructions for the control group](http://www.cs.cmu.edu/~rjsimmon/15122-s15/lab/lab6.pdf)

##States of the program

To compute a progress to solution metric, we classified each submission to be in one of many states, based on the effect of the code when compiled and tested against various test cases.

###Delete

**A** – Compile error

**B** – Runtime error (LOSSY)

**C** – Nontermination (LOSSY)

**D** – No effect

**E** – Neither beginning nor end (*unsure*)

**F** – Deletion works at nodes that are neither beginning nor end

**G** – Only deletion at end works

**H** – Deletion at beginning doesn’t work

**I** – Deletion at end doesn’t work

**J** – Cannot delete from beginning of a non-singleton list

**K** – Cannot delete anything except beginning of non-singleton list

**L** – Cannot deleting anything except beginning of non-singleton list (empties list)

**M** – Works on all lists of length <= 2, but cannot delete from middle of list of length >= 3

**N** – Can only delete from beginning of non-singleton list (all singleton lists are fine)

**O** – Deletion of an element from a list of length >=3 deletes the entire list after it

**P** – Failing one case (deletion of second element of a list of length >= 3

**Q** – Cannot delete from end of a non-singleton list?

**Y** – FAILURE (no students reached solution once they entered this state)

**Z** – SUCCESS
