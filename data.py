question_data = []
import requests

trivia_response=requests.get(url="https://opentdb.com/api.php",params={"amount":10,'difficulty':'medium',"type":'boolean'})
question_data=(trivia_response.json()['results'])

