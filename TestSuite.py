"""
Credits to Ned Batchelder https://stackoverflow.com/a/1732477/3672365
"""
import unittest


def main():
    test_modules = [
        'tests.test_parser',
        'tests.test_layer_elements',
    ]

    suite = unittest.TestSuite()

    for t in test_modules:
        try:
            # If the module defines a suite() function, call it to get the suite.
            mod = __import__(t, globals(), locals(), ['suite'])
            suitefn = getattr(mod, 'suite')
            suite.addTest(suitefn())
        except (ImportError, AttributeError):
            # else, just load all the test cases from the module.
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))
    result = unittest.TextTestRunner().run(suite)
    if not result.wasSuccessful():
        exit(1)


if __name__ == '__main__':
    main()
