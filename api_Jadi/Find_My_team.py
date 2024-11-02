import requests

API_KEY = "b278ea71e89649db95cddc1a258019e6"
COMPETITIONS = ["PL", "PD", "SA", "BL1", "FL1"]  # Premier League, La Liga, Serie A, Bundesliga, Ligue 1

headers = {"X-Auth-Token": API_KEY}

team_ids = {}

for competition in COMPETITIONS:
    url = f"https://api.football-data.org/v4/competitions/{competition}/teams"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        teams = response.json().get("teams", [])
        for team in teams:
            team_ids[team['name']] = team['id']
    else:
        print(f"Error fetching teams for competition {competition}: {response.status_code}")

print(team_ids)
