#Create a program that allows you to search for images in gif 
#format. The program should allow you to enter a search word. 
#Using this word, search for GIFs using the Giphy API. 
#As a result, print the links to the GIFs.
#Optional: Add the Telegram bot to the previous exercise. 
#Ask the user to enter a search word in the Telegram interface 
#and get a gif image as a result.

#Homework should be submitted via GitHub
# api.giphy.com/v1/gifs/search	
import requests

giphy_key = 'eGaF4A503SRHbCndR7xbtYjn3GFNeJ2G'

def gifs_search(user_input):
    res = requests.get(f'https://api.giphy.com/v1/gifs/search?api_key={giphy_key}&q={user_input}&limit=1')
    data = res.json()
    if "data" in data:
        gifs = data["data"]
        for gif in gifs:
            gif_url = gif.get("url")
            if gif_url:
                print(gif_url)
            else:
                print("No GIF URL found.")

def main():
    user_input = input('Enter input: ')
    gifs_search(user_input)

if __name__ == "__main__":
    main()
