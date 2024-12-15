import unittest
import requests
from unittest.mock import patch, Mock
from webserv import WebService


class TestWebService(unittest.TestCase):
    @patch("requests.get")
    def test_get_data_success(self, mock_get):
        # Налаштування фейкової відповіді
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_get.return_value = mock_response

        service = WebService()
        result = service.get_data("http://example.com")

        self.assertEqual(result, {"data": "test"})
        mock_get.assert_called_once_with("http://example.com")

    @patch("requests.get")
    def test_get_data_not_found(self, mock_get):
        # Налаштування фейкової відповіді з кодом 404
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error: Not Found")
        mock_get.return_value = mock_response

        service = WebService()
        with self.assertRaises(requests.exceptions.HTTPError):
            service.get_data("http://example.com/notfound")

        mock_get.assert_called_once_with("http://example.com/notfound")

    @patch("requests.get")
    def test_get_data_server_error(self, mock_get):
        # Налаштування фейкової відповіді з кодом 500
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("500 Server Error: Internal Error")
        mock_get.return_value = mock_response

        service = WebService()
        with self.assertRaises(requests.exceptions.HTTPError):
            service.get_data("http://example.com/servererror")

        mock_get.assert_called_once_with("http://example.com/servererror")


if __name__ == "__main__":
    unittest.main()
    