import sys
import os
import unittest

class TestSearchKeyword(unittest.TestCase):

    def setUp(self):
        self.route = os.getcwd() + '/Test_Folder'
        self.regex = '.txt'

    def test_missing_arguments(self):
        result = os.popen('python ../search_keyword.py').readline()
        self.assertEqual(result, '{}\n')

    def test_too_many_arguments(self):
        result = os.popen('python ../search_keyword.py').readline()
        self.assertEqual(result, '{}\n')


    def test_non_existent_dir(self):
        result = os.popen('python ../search_keyword.py ./Tes_Folder .txt').read()
        self.assertRegexpMatches(result, 'No such file or directory')

    def test_working_route(self):
        command = "python ../search_keyword.py " + self.route + " test" 
        result = os.popen(command).read()
        self.assertRegexpMatches(result, "('(\/([a-zA-Z_-])+)+': \d(,)?)+")

    '''
        Number of files with match .txt should be either 1, 6, or 7 from root_dir: Test_Folder
    '''
    def test_matching_regex(self):
        command = "python ../search_keyword.py " + self.route + " .txt"
        result = os.popen(command).read()
        self.assertRegexpMatches(result, "('(\/([a-zA-Z_-])+)+': [167],?)+")

    def test_check_if_svg_chart_is_generated(self):
        command = "python ../search_keyword.py " + self.route + " .txt"
        result = os.popen(command).read()
        svg_path = os.getcwd() + "/keyword_chart.svg"
        self.assertTrue(os.path.exists(svg_path))
    
if __name__ == '__main__':
    unittest.main()


