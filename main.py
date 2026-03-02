import requests
import sys
import json
import pprint

# Show the command the user should use
print("\nCommand👇")
print("="*17)
print("|github-activity|")
print("="*17)

def Github_Activity():

    # Load .json file if the file does not exist.
    try:
        with open("User_Data.json", "r", encoding='utf-8') as f:
            Data = json.load(f)
    except FileNotFoundError:
        Data = {}

    # Get user input through sys.argv
    user = sys.argv[2]

    # Get Github's API response in json formate
    response = requests.get(f"https://api.github.com/users/{user}/events")
    Data = response.json()

    # Write the API's response  to 'User_Data.json' file.
    with open("User_Data.json", "w", encoding='utf-8') as f:
        json.dump(Data, f, indent=2)
    
    # Get the type and name of the events from the response one by one.
    event_type_list = [
        "PushEvent",          
        "CreateEvent",       
        "DeleteEvent",        
        "ForkEvent",          
        "WatchEvent",      
        "IssuesEvent",       
        "IssueCommentEvent",  
        "PullRequestEvent",  
        "ReleaseEvent"
    ]

    types_list = []
    for info in Data:
        event_type = info["type"]
        types_list.append(event_type)
        event_repo_name = info["repo"]["name"]
        print(f"'{event_type}' event type in '{event_repo_name}'\n")
    
     # Show user each event and the number of times it happened.
    for i in event_type_list:
        if i in types_list:
            print(f"{i} : {types_list.count(i)}")
            print('-'*15)
      
    

def main():
    if len(sys.argv) < 2:
        print('Please try again...')
        return

    command = sys.argv[1]

    if command == "github-activity":
        Github_Activity()
    else:
        print("Nope...")
    
if __name__ == "__main__":
    main()