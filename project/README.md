# Project

## Due Date ##

The due date is Wednesday, December 12th 2018 at 9:00 AM.  We will have group 
presentations on that day.

## Course Project:  Overview

**The Goal**

You will develop a software library for a client (the teaching staff).  
The development of this library will leverage modern software development 
practices covered in the course.  By the end of the semester, 
the client should be able to easily install and run your package.

**The Topic**

The project topic is **automatic differentiation** (AD).  AD is a very broad area spanning computer science and 
mathematics with applications in fields across science and engineering.  We will only briefly graze the surface 
of this fascinating technique; indeed, AD is broad enough that it could form an entire course in its own right.  
Even so, your final project is to write a `python` automatic differentiation library.  Your library is not 
required to contain all aspects of AD; that would simply be too much for a single semester.  However, your library 
should meet the basic project expectations outlined in the following sections.

**Groups** 

You will work in groups of 3-4 students.  The teaching staff will assign you to groups.  Some members of the group will 
be stronger than others.  It is expected that you *work together* and help each other out as needed.  This is an 
opportunity for less experienced coders to drastically improve by working with more experienced coders.  On the other 
hand, the more experienced coders will gain valuable experience in guiding a small development team.  Every person must 
contribute.  No single person should dominate the group.

## Expectations 
This project has a few non-negotiable expectations, which are outlined in **basic expectations**.  The project also 
has a more open-ended component, which is described in **additional expectations**.

### Basic Expectations:
- [ ] `python` library that can be used for forward automatic differentiation.
- [ ] The client should be able to easily install the library, run the tests, access the documentation, and use the 
library for their application.
- [ ] Documentation for every subsystem in the project should be provided.
- [ ] Link to the docs from the ``README.md`` in each folder.
- [ ] The top level ``README.md`` should contain an overview, links to other docs, and an installation guide which 
will help us install and test your system.
- [ ] For those parts of the project which are modules, ``python setup.py test`` should 
suffice.
- [ ] For all other parts, include instructions on how to test your code. 
- [ ] Where possible, provide links to Travis-CI test runs and Coveralls coverage.
 
### Additional Expectations
AD is extremely versatile.  It finds applications in optimization, machine learning, and numerical methods (e.g. 
time integration, root-finding).  There are also many different ways of implementing an AD package.  In addition to 
the base-requirment of writing a forward mode AD library, you must also extend your package in some way.  There are 
many options here and the teaching staff will have to approve your proposed extension.  Here are a few general ideas 
(you will need to specialize them):
* Implement the reverse mode
* Implement a mixed mode
* Implement back propagation
* Write an application that uses your AD library
  - Implicit time-integrator
  - Optimization
  - Root-finder
* Option for higher-order derivatives (Hessians and beyond)

Note:  If you elect to write an application that uses your AD library, then you must speak to the teaching staff 
first.  There are certain instances where it might make sense to package your application together with your AD 
library (e.g. `pytorch`).  However, it may be a better idea to keep the two libraries separate.  In such a case, 
the teaching staff will need to approve your proposed extention and assess its efficacy.

You are more than welcome to pitch your own idea.

<!--
As you will see during the semester, automatic differentiation has two primary modes of operation: forward and 
reverse mode.  Each mode has its benefits and shortcomings, but the forward mode is generally easier to implement.  
-->

<!--
You are required to add a non-trivial feature to your library of your choosing.  
If you are having difficulty coming up with a compelling new feature, please 
set up an appointment with me to discuss possible ideas.  The teaching staff 
will be able to give you a few suggestions if need be.
-->

## Milestones
There will be two milestones in addition to the final project presentation and report.

### Milestone 1
Milestone 1 will be released simultaneously with HW3 on Thursday, October 4th and will be due on Thursday, October 18th.  
Specific details and requirements will be released with the milestone statement in the `project` directory.  This milestone 
will require you to clearly outline your proposed software design.  You are not required to implement any specific 
components at this point.  This milestone will form the precursor to your library documentation. 

### Milestone 2
Milestone 2 will be released simultaneously with HW4 on Thursday, October 18th and will be due on Thursday, November 15th.  
Specific details and requirements will be released with the milestone statement in the `project` directory.  This milestone 
will require a working library for forward automatic differentiation.  The library does not need to be 100% complete at this 
time, but the client (teaching staff) should be able install your package and use it for some simple use-cases.  
Some of the use-cases will be provided in the milestone 2 statement when it is released.

### Final Presenation
The final presentation will occur on Wednesday, December 12th.  This presentation will 
be a demo of your entire library.  The final deliverable will be in the form of 
documentation of your library including instructions on how to install, run the tests, 
and examples for new users.

## Assessment
The final project is worth 50% of your course grade. Here is a breakdown of the components of the project:

* Milestone 1 (10/18): 10% 
  - Project repo / organization set up; teaching staff invited
  - Repository README set up
  - Report detailing proposed software design; will form the beginning of the software documentation

* Milestone 2 (11/15): 15%
  - Working forward mode implementation
    - May be incomplete, but should meet basic requirements (to be outlined later)
  - Packaging and Installation
  - Test suite
  - Documentation
  - Proposal for additional features and extensions
* Final deliverables (12/12 9:00 AM): 25%
  - Forward mode complete
    - Specifics will be provided at a later date
  - Documentation complete
  - Library complete
    - This includes any additional features
  - Final presentation
  - Self and peer evaluation

**Note:** Most of the forward mode will be complete by the end of Milestone 2.  Therefore, a fair portion of the grade for the 
final deliverables will come from any additional features that you propose.  For example, it is not sufficient to simply 
overload one more function for the forward mode implementation beyond what you did for Milestone 2.
