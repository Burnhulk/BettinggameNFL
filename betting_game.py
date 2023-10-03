import requests
#get NFL Boxscores through API
def get_weekly_scores(week):
    url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLScoresOnly"

    querystring = {"gameWeek": str(week),"season":"2023"}

    headers = {
        "X-RapidAPI-Key": "716fb2ca88mshf756797310b748bp1b72c3jsn856097f3bd81",
        "X-RapidAPI-Host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to retrieve data for week {week}. Status code {response.status_code}")
        return None


#find out Winners/losers of the Week
def results(response):
    winners_list = []
    losers_list = []
    draw_list = []

    games = response["body"]

    for game_id, details in games.items():
        away_team = details['away']
        home_team = details['home'] 
        away_score = details['awayPts']
        home_score = details['homePts']   

        if int(home_score) > int(away_score):
            winners_list.append(home_team)
            losers_list.append(away_team)

        elif int(home_score) == int(away_score):
            draw_list.append([home_team, away_team])

        else:
            winners_list.append(away_team)
            losers_list.append(home_team) 

    return winners_list, losers_list

response_data = get_weekly_scores(1)
if response_data:
    winners_list, losers_list = results(response_data)

    print("Winner:", winners_list)
    print("Loser:", losers_list)




