import tmdb_client
from unittest.mock import Mock
from main import app
import pytest

#test z przykladu
def test_get_movies_list(monkeypatch):
   # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   # Wynik wywołania zapytania do API
   response = requests_mock.return_value
   # Przysłaniamy wynik wywołania metody .json()
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)


   movies_list = tmdb_client.get_movies_list(list_name="popular")
   assert movies_list == mock_movies_list



def test_get_single_movie_cast(monkeypatch):
   mock_cast = ["Cast"]
   request_mock = Mock()
   response = request_mock.return_value
   response.json.return_value = mock_cast
   monkeypatch.setattr("tmdb_client.requests.get", request_mock)

   cast = tmdb_client.get_single_movie_cast(5)
   assert cast['cast'] == mock_cast

#FAILED test_tmdb.py::test_get_single_movie_cast - TypeError: list indices must be integers or slices, not str

@pytest.mark.parametrize('list_name', (
   ('popular'),
   ('latest'),
   ('now_playing'),
   ('top_rated'),
   ('upcoming')
))

def test_homepage(monkeypatch, list_name):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)



   with app.test_client() as client:
      #nie wiem, co tu wpisac, gdzie klient ma sie dostac
       response = client.get('/')
       assert response.status_code == 200
       api_mock.assert_called_with(f'movie/{list_name}')

   #naprawde nie umiem tego przykladu :(



