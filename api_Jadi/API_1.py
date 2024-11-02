#first attempt, API learning, Thanks to JAdi Youtube
import requests
from datetime import datetime
import base64

# Configurations
FOOTBALL_API_KEY = "b278ea71e89649db95cddc1a258019e6"
TEAM_IDS = [86, 81, 65, 5, 64, 524, 108, 98, 109, 61, 78]
# Your ClickSend credentials
username = 'a.saeidanezhad@gmail.com'
api_key = '3E3DAE54-8AC1-06EA-BF22-B2415D4211C2'
TO_PHONE_NUMBER = "+447308761632"
FROM_PHONE_NUMBER = "+447308761632"

def get_todays_matches():
    headers = {"X-Auth-Token": FOOTBALL_API_KEY}
    today = datetime.today().date()
    matches_today = []

    for team_id in TEAM_IDS:
        url = f"https://api.football-data.org/v4/teams/{team_id}/matches?dateFrom={today}&dateTo={today}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            matches = response.json().get("matches", [])
            for match in matches:
                match_info = {
                    "team_id": team_id,
                    "utcDate": match["utcDate"],
                    "homeTeam": match["homeTeam"]["name"],
                    "awayTeam": match["awayTeam"]["name"]
                }
                matches_today.append(match_info)
        else:
            print(f"Error fetching matches for team {team_id}: {response.status_code}")
    
    return matches_today

# Encode credentials
credentials = f'{username}:{api_key}'
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# SMS details
def send_sms(message):
    sms_data = {
        'messages': [
            {
                'source': 'python',
                'body': message,
                'to': TO_PHONE_NUMBER,
                'from': FROM_PHONE_NUMBER
            }
        ]
    }

    # Headers
    headers = {
        'Authorization': f'Basic {encoded_credentials}',
        'Content-Type': 'application/json'
    }

    # Send SMS
    response = requests.post('https://rest.clicksend.com/v3/sms/send', json=sms_data, headers=headers)

    # Handle response
    if response.status_code == 200:
        print('SMS sent successfully!')
        print('Response:', response.json())
    else:
        print('Failed to send SMS.')
        print('Status Code:', response.status_code)
        print('Response:', response.json())


def main():
    matches_today = get_todays_matches()
    if matches_today:
        for match in matches_today:
            match_time = match["utcDate"]
            home_team = match["homeTeam"]
            away_team = match["awayTeam"]
            message = f"Match today at {match_time}: {home_team} vs {away_team}. Don't miss it!"
            send_sms(message)
    else:
        print("No matches today for your favorite teams.")
if __name__ == "__main__":
    main()

