



class SUT:
    GREP  = 0
    GZIP  = 1
    SED   = 2
    TCAS  = 3




# run a mutant on a test case
def run_x_on_y(x, y):
    if sut == SUT.GREP:
        return commands.getstatusout('{0} {1} grep1.dat'.format(x,y))

# runs a mutant on test cases
def run_testcases(mutant, testcases):
    for tc in testcases:
        run_x_on_y(mutant, tc)
 

# run mutants on the test cases
def tests_mutants(mutants, testcases):
    for m in mutants:
        run_testcases(m, testcases)





