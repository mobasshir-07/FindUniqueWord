import requests
import json
from bs4 import BeautifulSoup
# Requests helps in getting content from URL
# Json helpos in getting output list of words in JSON format 
# BeautifulSoup helps in easily scraping information from the webpages


# Fisrtly, we will get content by requesting the wepage and afer that parse that HTML content
# Convert that content in terms of string of words using inbuild functions.
# We will take that string and preferably use map data structure for counting the frequency of words in that particular string. 

# Function which is going to return list of words in JSON format along with the frequency of occurrence
def count_words_on_webpage(url):
    # Make request to webpage
    response = requests.get(url)

    # Parse HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract text from HTML content
    soup = soup.get_text() 

    # Split text into words
    words = soup.split()
 
    # Count frequency of each word
    uniqueWords = {}
    for word in words:
        word = word.lower()
        if word in uniqueWords:
            uniqueWords[word] += 1
        else:
            uniqueWords[word] = 1

    # Convert dictionary to JSON format
    final_output = json.dumps(uniqueWords)
    return final_output

# Example usage
url = 'https://www.geeksforgeeks.org/python-map-function/'
json_output = count_words_on_webpage(url)
print(json_output)
