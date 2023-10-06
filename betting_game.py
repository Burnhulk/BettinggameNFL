import requests
import tkinter as tk

week = str(input("Which week?"))
#Get Box Scores through API
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

#show all the games and the scores
def show_games(response):
    
    games = response["body"]

    for game_id, details in games.items():
        away_team = details["away"]
        home_team = details["home"] 
        away_score = details["awayPts"]
        home_score = details["homePts"] 

        try: 
            print(f"{away_team} {away_score} - {home_score} {home_team}")
        except:
            print(f"{away_team} - {home_team}")

#find the winners from games
def winner(response):
    
    winners_list = []
    draw_list = []

    games = response["body"]

    for game_id, details in response["body"].items():

        away_team = details["away"]
        home_team = details["home"] 
        away_score = details["awayPts"]
        home_score = details["homePts"] 
        
        try:#logic to find the winners. int is necessary otherwise it wont work
            if int(home_score) > int(away_score):
                winners_list.append(home_team)
            
            elif int(home_score) == int(away_score):
                draw_list.append(home_team, away_team)
            
            else:
                winners_list.append(away_team)
        except ValueError:
            print("No Games played yet")
        
    return winners_list, draw_list


#WiP to show results
response = get_weekly_scores(week)
show_games(response)
winners_list, draw_list = winner(response)
print(winners_list)


    
    



class Player:
    def __init__(self, name):
        self.name = name
        self.win_tips = {}
        self.points = 0
    def add_win_tip(self, details, tip):
        pass
    def player_points(self):
        pass


    

