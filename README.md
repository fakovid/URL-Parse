# URL-Parse
Help to fact check links using Python!

# Usage
Judging if a URL can provide helpful information about COVID is easy. Just put this folder into your project.

Here is an example of how you can check if an inputted URL is providing good information
```py
from judge import Message, check_safe

my_url = input() # Let the user input a URL
result = check_safe(my_url) # Inspects URL return Object of type Message

print(result.load_message()) # Prints helpful feedback message based on the content of the url
result.base_url # Base URL
result.long_url # Final URL (Traverses through link shorteners)
result.status # 'false' 'mixed' 'true'
result.category # Returns what category of COVID it responds to