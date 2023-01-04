import tkinter as tk
from tkinter import *
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Create the GUI window
window = tk.Tk()
window.title("My Browser")

# Add a text field for the user to enter a URL
url_field = Entry(window)
url_field.pack()

# Add a button to navigate to the URL
def go_to_url():
  # Get the URL from the text field
  url = url_field.get()
  
  # Fetch the HTML source code of the webpage
  try:
    html = urlopen(url).read()
  except:
    # Display an error message if the URL is invalid
    label = Label(window, text="Error: Invalid URL")
    label.pack()
    return
  
  # Parse the HTML to extract the content of the webpage
  soup = BeautifulSoup(html, "html.parser")
  
  # Remove script and style elements
  for element in soup(["script", "style"]):
    element.decompose()
    
  # Extract the text of the webpage
  text = soup.get_text()
  
  # Display the text in the GUI window
  label = Label(window, text=text, justify=LEFT)
  label.pack()

button = Button(window, text="Go", command=go_to_url)
button.pack()

# Run the GUI
window.mainloop()
