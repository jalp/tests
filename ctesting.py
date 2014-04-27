# Usage:
# nosetests ctesting.py -m '(?:^|[b_./-])c[Tt]est'
from nose import with_setup


class cTest(object):

    def __init__(self):
        self.m = None

    def setup(self):
        print self.setup.__name__
        self.m = 'Arrancado'
        print self.m

    def teardown(self):
        print self.teardown.__name__
        self.m = 'Parado'
        print self.m

    def ctest_evens(self):
        for i in range(0, 5):
            yield self.check_even, i, i * 3

    @with_setup(setup, teardown)
    def check_even(self, n, nn):
        print self.check_even.__name__
        assert n % 2 == 0 or nn % 2 == 0
