import json
from pathlib import Path

LIST_FILE = Path("watchlist.json")

def view_watchlist(watchlist):
    #watchlist = load_watchlist()
    if not watchlist:
        print("Your watchlist is empty.")
    else:
        print("Your Watchlist:")
        for idx, anime in enumerate(watchlist, start=1):
            print(f"{idx}. Title: {anime['title']} - Completion Status: {anime['status']} - Episodes: {anime['episodes']} - Episodes Watched: {anime['episodes_watched']}")



def add_to_watchlist(watchlist):
    anime_title = input("Enter the title of the anime: ").strip()


    anime_episodes = input("Enter amount of episodes that the anime has: ")
    episodes_watched = input("How many episodes have you watched?: ")
        
    if not anime_episodes.isdigit() or not episodes_watched.isdigit():
        print("Please use a valid number. ")
        return
    anime_episodes = int(anime_episodes)
    episodes_watched = int(episodes_watched)

    if episodes_watched > 0:
        anime_episodes -= episodes_watched
        

    anime = {
        "title" : anime_title,
        "status" : "incomplete",
        "episodes": anime_episodes,
        "episodes_watched": episodes_watched
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
    #watchlist = load_watchlist()
    anime_title = input("What anime would you like to delete from your watchlist? ").strip()
    #Find title that matches user's input
    for anime in watchlist:
        if anime['title'].lower() == anime_title.lower():
            watchlist.remove(anime)
            save_watchlist(watchlist)
            print(f"{anime_title} has been successfully removed!")
            break
        else:
            print(f"{anime_title} not found in your watchlist!")

def update_episodes(watchlist):
    anime_title = input("Which anime do you want to update? ").strip()

    try:
        episodes_watched = int(input(f"How many episode have you watched of {anime_title}? "))
    except(ValueError):
        print("Please enter a valid number.")

    for anime in watchlist:
        if anime['title'].lower() == anime_title.lower():
            anime['episodes_watched'] += episodes_watched
            anime['episodes'] -= episodes_watched
            if anime['episodes'] <= 0:
                anime['status'] = "Complete"
                break
            save_watchlist(watchlist)
            print(f"You have watched {episodes_watched} episodes of {anime_title}. ")
            break
        else:
            print(f"{anime_title} was not found in your watchlist. ")

def main():
    watchlist = load_watchlist()
    while True:
        print("Anime Tracker")
        print("1. View Watchlist")
        print("2. Add to Watchlist")
        print("3. Update episodes that have been watched")
        print("4. Remove from Watchlist")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_watchlist(watchlist)
        elif choice == '2':
            add_to_watchlist(watchlist)
        elif choice == '3':
            update_episodes(watchlist)
        elif choice == '4':
            remove_from_watchlist(watchlist)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
