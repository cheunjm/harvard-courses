# Milestone 1

**Due: Thursday, October 18th at 11:59 PM**

## Submission Instructions
In the homework assignment this week, you should have created a GitHub organization with your
project group and invited the teaching staff.  The organization can consist of multiple
repositories, but one of those repositories must be your actual software project repo.  That 
repo is the one that will be graded for your final project and the project milestones.

Within your final project repo, you should create a directory called `docs`.  You can use this
directory to organize documentation and tutorials for your final package.  For this milestone, you
should have a file called `milestone1`.  The type of file is up to you and your group.  Two good 
choices are markdown (`milestone1.md`) or a Jupyter notebook (`milestone1.ipynb`).

To summarize, your submission should be in the following format:
```
project_repo/
             README.md
             docs/  
                  milestone1
             ...
```

**The teaching staff will only be able to give you a grade if you follow the exact structure just
outlined!**

## Requirements
There are three primary requirements for this first milestone.
1. Create project organization and invite teaching staff.
   * Within the project organization, create a project repo (make sure teaching staff has access).
2. Create a `README.md` inside the project repo.  At this point, the `README` should only include
the group name / number and list the members of the team.
3. The `docs/` directory should include a document called `milestone1` (the extension is up to you,
but `.md` or `.ipynb` are recommended.  Details on how to create `milestone1` are provided in the
`Milestone1` section below.

## Milestone1 Document
You must clearly outline your software design for the project.  Here are some possible sections to
include in your document along with some prompts that you may want to address.

### Introduction
Describe problem the software solves and why it's important to solve that problem

### Background
Describe (briefly) the mathematical background and concepts as you see fit.  You **do not** need to
give a treatise on automatic differentation or dual numbers.  Just give the essential ideas (e.g.
the chain rule, the graph structure of calculations, elementary functions, etc).

### How to Use *PackageName*
How do you envision that a user will interact with your package?  What should they import?  How can
they instantiate AD objects?

**Note: This section should be a mix of pseudo code and text.  It should not include any actual
operations yet.**

### Software Organization
Discuss how you plan on organizing your software package.
* What will the directory structure look like?  
* What modules do you plan on including?  What is their basic functionality?
* Where will your test suite live?  Will you use `TravisCI`? `Coveralls`?
* How will you distribute your package (e.g. `PyPI`)?

### Implementation
Discuss how you plan on implementing the forward mode of automatic differentiation.
* What are the core data structures?
* What classes will you implement?
* What method and name attributes will your classes have?
* What external dependencies will you rely on?
* How will you deal with elementary functions like `sin` and `exp`?

Be sure to consider a variety of use cases.  For example, don't limit your design to scalar
functions of scalar values.  Make sure you can handle the situations of vector functions of vectors and
scalar functions of vectors.  Don't forget that people will want to use your library in algorithms
like Newton's method (among others).

Try to keep your report to a reasonable length.  It will form the core of your documentation, so you
want it to be a length that someone will actually want to read.

## Additional Comments
There is no need to have an implementation started for this Milestone.  You are now in the planning
phase.  This means that you should feel free to have a `project_planning` repo in your project
organization for scratch work and code.  The actual implementation will start after Milestone 1.
