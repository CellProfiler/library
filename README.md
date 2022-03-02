# library

ARCHIVED - we still plan to do this but will be doing it in the main CellProfiler repository instead. 

cellprofiler-library was an experiment - use at your own risk.

The idea is to collect all of CellProfiler's "discrete functions" into a single library.
This allows import in places like napari or jupyter or any other python place you like.
It will hopefully help the maintainers as well as we upgrade algorithms towards CellProfiler 5.

Most of these, as will be evident to a code reviewer, are going to be wrappers around calls to other libraries.
Wherever possible, the goal will be for the only inputs to be arrays and setting values, and the only outputs arrays.

Our hope is that by collecting CellProfiler's "discrete functions" in a single place, with friendly function names and setting names, that it will be useful to new image analysts.
We expect that in at least some places, reasonable users may disagree about which step(s) of a module's code comprise a "discrete function". We'll use our best judgement.

Many decisions still need to be made, such as
- Should functions be grouped at the module level (ie ExpandOrShrinkObjects) or category level (ObjectProcessing)? The former is probably better for CellProfiler-the-program users, the latter for non-users.  
