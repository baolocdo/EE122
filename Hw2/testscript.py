#!/usr/bin/env python
from __future__ import print_function


import sys
import re


patterns = (
            # Q1-5: Layers
            '^[a-e]$', '^[a-e]$', '^[a-e]$', '^[a-e]$', '^[a-e]$',
            # Q6: Routing Validity
            '^[a-d]{0,4}$',
            # Q7: Transport Algorithms
            '^[a-d]{0,4}$',
            # Q8-12: Self-Learning Switch
            '^[a-h]{0,8}$',
            '^[a-h]{0,8}$',
            '^[a-h]{0,8}$',
            '^[a-h]{0,8}$',
            '^[a-h]{0,8}$',
            # Q13-16: Distance-Vector Routing
            '^([0-9]+|inf),([0-9]+|inf),([0-9]+|inf)$',
            '^([0-9]+|inf),([0-9]+|inf),([0-9]+|inf)$',
            '^([0-9]+|inf),([0-9]+|inf),([0-9]+|inf)$',
            '^([0-9]+|inf),([0-9]+|inf),([0-9]+|inf)$',
            # Q17-20: Link-State Routing
            '^[a-h]{2,12}$', '^[a-h]{2,12}$', '^[a-h]{2,12}$', '^[a-h]{2,12}$'
           )


def main(args):
    if len(args) != 2:
        print (str.format("Usage: {0} answer_file\n", args[0]))
        sys.exit (1);
    answerFile = args[1];
    ans = open(answerFile)
    print ("Answers found:")
    print ("Question\tAnswer")
    separator_found = False

    expectedQ = 1
    for l in ans:
        l = l.strip()
        if l.startswith("-----"):
            separator_found = True
            break

        if len(l.split()) != 2:
            print (str.format("Unexpected line {0} found", l))
        (actualQ, actualA) = l.split()
        print (str.format("{0}\t\t{1}", actualQ, actualA))
        if (actualQ != str (expectedQ)):
            print (str.format ("Expected question {0}!", expectedQ), \
                   file=sys.stderr);
            sys.exit (1);

        if (expectedQ > len (patterns)):
            print >> sys.stderr, "Too many answers!"
            sys.exit (1)

        pattern = re.compile (patterns [expectedQ - 1], re.IGNORECASE)
        if (pattern.match (actualA) == None):
           print ("Unexpected answer " + actualA + "!", \
                  file=sys.stderr)
           sys.exit (1);

        expectedQ += 1

    if (expectedQ <= len (patterns)):
        print ("Insufficient number of answers!", \
               file=sys.stderr);
        sys.exit (1);

    print ("")
    if separator_found:
        print ("We found a section containing your reasoning.")
        print ("The format and content of this section were not checked.")
    else:
        print ("We did not find a section containing your reasoning.")
        print ("Please add this to your file, or submit a txt or pdf file named hw2work")

    if (answerFile != "hw2.txt"):
        print ("", file=sys.stderr);
        print (str.format ("Warning: {0} specified as input, expected 'hw2.txt'!", \
                           answerFile), file=sys.stderr);
        print ("(You should upload a file named 'hw2.txt' to bSpace.)", file=sys.stderr);

if __name__ == "__main__":
    main(sys.argv)