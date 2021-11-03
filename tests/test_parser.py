import unittest
from pyqtlet2.leaflet.core.Parser import Parser


class ParserTestCase(unittest.TestCase):
    def test_dict_to_js_parsing(self):
        test_dict = {"bool_test_true": True, "bool_test_false": False, "string_test_true": "true"}
        parsed_dict = Parser.dict_for_js(test_dict)
        self.assertEqual(parsed_dict.get("bool_test_true"), "true")
        self.assertEqual(parsed_dict.get("bool_test_false"), "false")
        self.assertEqual(parsed_dict.get("string_test_true"), "true")

    def test_js_to_dict_parsing(self):
        test_dict = {"bool_test_true": "true", "bool_test_false": "false", "test_number": 12.34}
        parsed_dict = Parser.js_for_dict(test_dict)
        self.assertEqual(parsed_dict.get("bool_test_true"), True)
        self.assertEqual(parsed_dict.get("bool_test_false"), False)
        self.assertEqual(parsed_dict.get("test_number"), 12.34)


if __name__ == '__main__':
    unittest.main()
