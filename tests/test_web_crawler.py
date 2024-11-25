import unittest
from unittest.mock import patch, Mock
from io import StringIO
from alessandro_c_mod1_atsiskaitymas.web_crawler import web_crawler
import sys


# Assuming the web_crawler function is in a module called crawler
# from crawler import web_crawler

class TestWebCrawler(unittest.TestCase):

    @patch('requests.get')
    @patch('sys.stdout', new_callable=StringIO)  # This will capture print statements
    def test_web_crawler(self, mock_stdout, mock_get):
        # Sample HTML content to be returned by the mock `get` request
        html_content = """
        <html>
            <body>
                <div class="product-item">
                    <input name="productName" value="SWANSON L-ARGININAS, 500 mg, 100 kapsulių"/>
                    <input name="productPrice" value="13.49"/>
                    <input name="productBrand" value="Swanson"/>
                </div>
                <div class="product-item">
                    <input name="productName" value="ICONFIT, Dietinis kokteilis - Šokolado, 495g"/>
                    <input name="productPrice" value="14.99"/>
                    <input name="productBrand" value="Iconfit"/>
                </div>
            </body>
        </html>
        """

        # Mock the response of requests.get
        mock_response = Mock()
        mock_response.text = html_content
        mock_get.return_value = mock_response

        # Call the web_crawler function
        web_crawler()

        # Check if the print statements were called correctly
        output = mock_stdout.getvalue()

        # Assert the correct output is printed
        self.assertIn("Product Name: SWANSON L-ARGININAS, 500 mg, 100 kapsulių", output)
        self.assertIn("Product Price: 13.49", output)
        self.assertIn("Product Brand: Swanson", output)
        self.assertIn("Product Name: ICONFIT, Dietinis kokteilis - Šokolado, 495g", output)
        self.assertIn("Product Price: 14.99", output)
        self.assertIn("Product Brand: Iconfit", output)


if __name__ == '__main__':
    unittest.main()