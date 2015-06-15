    def check(self, t, testsuite, k):
        for t in testsuite:
            id = self.index_test_suite(t, k)
            try:
                self.index_testcase(t["testcase"], id)
            except KeyError:
                print "no testcase found"
