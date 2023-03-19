# Import the wikipedia library
import wikipedia

# Define the topic you want to search for on Wikipedia
search_topic = "Python (programming language)"

# Use the wikipedia library to search for the topic
search_results = wikipedia.search(search_topic)

# Choose the first search result
page_title = search_results[0]

# Use the wikipedia library to get the page for the chosen search result
page = wikipedia.page(page_title)

# Print out the page's title and summary
print("Title: ", page.title)
print("Summary: ", page.summary)
