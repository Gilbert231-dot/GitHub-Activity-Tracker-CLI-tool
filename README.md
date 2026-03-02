# Github User Activity 

A command-line interface app that gets you, recent information about your github activities.

## Features
- Response from GitHub's API is stored in  `User_Data.json` file
- It returns the event type and the name of the repository where that event happened.
- It also shows you a dictionary of each event and the number of times it happened.

- It shows you each event and the number of times it happened.

1. Clone the repository.
2. Install: `pip install requests` if you already don't have it installed.

### Usage

python main.py github-activity `username`

### Output
'PushEvent' event type in 'Gilbert231-dot/Task-Tracker-CLI-App'

'PushEvent' event type in 'Gilbert231-dot/Task-Tracker-CLI-App'

'PushEvent' event type in 'Gilbert231-dot/Task-Tracker-CLI-App'

'CreateEvent' event type in 'Gilbert231-dot/Task-Tracker-CLI-App'

{'CreateEvent': 1, 'PushEvent': 3}

https://roadmap.sh/projects/github-user-activity
