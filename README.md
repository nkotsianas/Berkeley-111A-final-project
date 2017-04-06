# Berkeley-111A-final-project
Final project for Berkeley's 111A "basic semiconductor circuits" lab. 4-bit signed calculator with LabVIEW expression parser.



For the final project, a 4-bit (signed) adder with a LabVIEW interface was designed and built. This project attempts to emulate a modern processor by accepting an arbitrarily long (syntactically correct) input of additions, subtractions, and parentheses, then, using LabVIEW, parses and orders the input and sends each individual computation to the calculator, which then sends the result back to the VI. The process repeats until there are no more operations to be done, yielding the final answer. The calculator produces results admirably, provided that the input and outputs are kept between -8 and +7, with an estimated individual computation time of a rather high 10 ms.
