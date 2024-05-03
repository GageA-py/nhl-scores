import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)
response = requests.get('https://api-web.nhle.com/v1/scoreboard/now')
scores = response.json()


@app.route("/")
def index():
    latest_games_data = {}
    for date_info in scores['gamesByDate']:
        for game in date_info['games']:
            if 'score' in game['homeTeam'] and 'score' in game['awayTeam']:
                series_key = f"{game['homeTeam']['abbrev']} {game['awayTeam']['abbrev']}"
                game_number = game['seriesStatus']['game']
                home_team = f"{game['homeTeam']['abbrev']}"
                home_team_logo = f"{game['homeTeam']['logo']}"
                home_team_score = f"{game['homeTeam']['score']}"
                away_team = f"{game['awayTeam']['abbrev']}"
                away_team_logo = f"{game['awayTeam']['logo']}"
                away_team_score = f"{game['awayTeam']['score']}"
                series_game_number = f"Game {game_number}"
            
                if home_team_score > away_team_score:
                    scoreboard = f"{home_team} DEF. {away_team} {home_team_score}-{away_team_score}"
                elif away_team_score > home_team_score:
                    scoreboard = f"{away_team} DEF. {home_team} {away_team_score}-{home_team_score}"
                else:
                    scoreboard = f"Game is tied."

                latest_games_data[series_key] = {'home_team': home_team,
                'away_team': away_team,
                'series_game_number': series_game_number,
                'home_team_logo_url': home_team_logo,
                'home_team_score': home_team_score,
                'away_team_score': away_team_score,
                'away_team_logo_url': away_team_logo,
                'scoreboard': scoreboard}
    
    return render_template('scoreboard.html', latest_games_data=latest_games_data)

@app.route('/now')
def get_current_score():
    latest_games_data = {}
    for date_info in scores['gamesByDate']:
        for game in date_info['games']:
            if 'score' in game['homeTeam'] and 'score' in game['awayTeam']:
                series_key = f"{game['homeTeam']['abbrev']} {game['awayTeam']['abbrev']}"
                game_number = game['seriesStatus']['game']
                home_team = f"{game['homeTeam']['abbrev']}"
                home_team_logo = f"{game['homeTeam']['logo']}"
                home_team_score = f"{game['homeTeam']['score']}"
                away_team = f"{game['awayTeam']['abbrev']}"
                away_team_logo = f"{game['awayTeam']['logo']}"
                away_team_score = f"{game['awayTeam']['score']}"
                series_game_number = f"Game {game_number}"
            
                if home_team_score > away_team_score:
                    scoreboard = f"{home_team} DEF. {away_team} {home_team_score}-{away_team_score}"
                elif away_team_score > home_team_score:
                    scoreboard = f"{away_team} DEF. {home_team} {away_team_score}-{home_team_score}"
                else:
                    scoreboard = f"Game is tied."

                latest_games_data[series_key] = {'home_team': home_team,
                'away_team': away_team,
                'series_game_number': series_game_number,
                'home_team_logo_url': home_team_logo,
                'home_team_score': home_team_score,
                'away_team_score': away_team_score,
                'away_team_logo_url': away_team_logo,
                'scoreboard': scoreboard}
                
    return jsonify(latest_games_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
