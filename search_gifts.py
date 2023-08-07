import requests

def search_gifs(search_term, limit=5):
    api_key = "YOUR_GIPHY_API_KEY"
    base_url = "https://api.giphy.com/v1/gifs/search"
    params = {
        "q": search_term,
        "limit": limit,
        "api_key": api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        gif_links = [gif["images"]["original"]["url"] for gif in data["data"]]
        return gif_links
    else:
        print("Error:", data.get("message", "Unknown error"))

def main():
    search_term = input("Enter a search word for GIFs: ")
    limit = 5  # You can adjust the number of GIFs to retrieve
    gif_links = search_gifs(search_term, limit)

    if gif_links:
        print("GIFs found:")
        for link in gif_links:
            print(link)
    else:
        print("No GIFs found for the given search term.")

if __name__ == "__main__":
    main()