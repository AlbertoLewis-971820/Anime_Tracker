import json
from pathlib import Path

LIST_FILE = Path("watchlist.json")

def view_watchlist(watchlist):
    watchlist = load_watchlist()
    if not watchlist:
        print("Your watchlist is empty.")
    else:
        print("Your Watchlist:")
        for idx, anime in enumerate(watchlist, start=1):
            print(f"{idx}. {anime['title']} - {anime['status']} - {anime['episodes']}")



def add_to_watchlist(watchlist):
    anime_title = input("Enter the title of the anime: ")
    anime_episodes = int(input("Enter amount of episodes that the anime has: "))

    anime = {
        "title" : anime_title,
        "status" : "incomplete",
        "episodes": anime_episodes
    }

    watchlist.append(anime)

    save_watchlist(watchlist)
    print(f"{anime_title} added to your watchlist!")




def load_watchlist():
    if LIST_FILE.exists():
        with(open(LIST_FILE, 'r')) as file:
            return json.load(file)
    return []

def save_watchlist(watchlist):
    with(open(LIST_FILE,'w')) as file:
        json.dump(watchlist, file, indent=4)

def remove_from_watchlist(watchlist):
    pass

def update_watchlist(watchlist):
    pass

def main():
    watchlist = load_watchlist()
    while True:
        print("Anime Tracker")
        print("1. View Watchlist")
        print("2. Add to Watchlist")
        print("3. Remove from Watchlist")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_watchlist(watchlist)
        elif choice == '2':
            add_to_watchlist(watchlist)
        elif choice == '3':
            remove_from_watchlist(watchlist)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
