**Rick Tesmond's Pyramid Word Analyzer**

3/4/2020

A microservice built on Flask that accepts single words as input in a GET request, and will return whether the given word is a pyramid word or not.

'A word is a ‘pyramid’ word if you can arrange the letters in increasing frequency, starting with 1 and continuing without gaps and without duplicates.'

Running the service:

0) create a venv and import the packages from requirements.txt
1) from your command line, run 'python app.py'
2) query the endpoint using curl (replacing 'your_local_host' and 'your_word' with your local host and the word to test)
        ex. curl http://your_local_host:9090/pyramid-word?word=your_word

You will be returned a json response indicating whether the word is or is not a pyramid word!

Example response if it is a pyramid:

{
  "response": "PYRAMID FOUND: The word passed is a pyramid word: 'banana'. Word pyramid output: [('b', 1), ('n', 2), ('a', 3)]", 
  "status": 200
}

If it is not a pyramid, some error occurs, or invalid characters are passed, you will be returned a corresponding error message.

**Bonus**

If you aren't well versed in curl, I also created a GUI for this process. Simply browse to 'http://your_local_host:9090/' and use the GUI!
