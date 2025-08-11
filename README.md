# Notion Onboarding Automation

A Python script that connects to your existing Notion workspace to automate creator and agency onboarding.

## What it does

- Reads a CSV list of onboardees with their roles (creator or agency)  
- Creates pages for each onboardee in your Notion **Current Onboarding** database  
- Adds role-specific onboarding tasks linked to each onboardee in a separate **Tasks** database  

## Notion Setup

1. **Create a Notion database** called `Current Onboarding` with at least these properties:  
   - `Onboardee` — type: **Title** (text)

2. **Create another database** called `Tasks` with these properties:  
   - `Task` — type: **Title** (text)  
   - `Checkbox` — type: **Checkbox**  
   - `Onboardee` — type: **Relation** (linked to the `Onboardee` property in the `Current Onboarding` database)

3. (Optional) Add a **Progress Bar** property to the `Current Onboarding` database using a **Rollup** of the task completion checkboxes.

4. **Get the database IDs:**  
   - Share the databases publicly (or via integration)  
   - From the shared URL, copy the 32-character alphanumeric ID between the workspace name and any query parameters (before any `?`)
     <img width="1502" height="128" alt="image" src="https://github.com/user-attachments/assets/4eeba417-7ee1-4137-8750-cb008aaf047b" />


## Getting Started

1. Clone the repository  
2. Create a `.env` file with your Notion API token and the database IDs:  
```
NOTION_TOKEN=your_secret_token
CURRENT_ONBOARDING_DB=your_current_onboarding_db_id
TASKS_DB=your_tasks_db_id
```

3. Put your onboardees in `data/to_be_onboarded.csv` with columns:  
- `onboardee` (username)  
- `role` (`creator` or `agency`)  
4. Run the script:  
```bash
python main.py
```
## Project Structure
```
.
├── config.py           # Config and onboarding tasks per role
├── csv_helpers.py      # CSV reading utilities
├── notion_helpers.py   # Notion API helper functions
├── data/               # CSV data files
│   └── to_be_onboarded.csv
├── main.py             # Main script
├── .env                # Notion API tokens (not committed)
└── .gitignore
```

