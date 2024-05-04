from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import pandas as pd

def get_player_stats_by_name(player_name):
    # Find players by name
    player_dict = players.get_players()
    player = [player for player in player_dict if player['full_name'].lower() == player_name.lower()]
    
    if not player:
        print("Player not found.")
        return

    # Fetch career stats for the found player
    career = playercareerstats.PlayerCareerStats(player_id=player[0]['id'])
    career_stats_df = career.get_data_frames()[0]
    
    # Display specific statistics such as PPG, RPG, etc.
    print(f"Career stats for {player_name}:")
    print(career_stats_df[['SEASON_ID', 'TEAM_ID', 'PLAYER_AGE', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']].tail())

def main():
    player_name = input("Enter the player's name to retrieve stats: ")
    get_player_stats_by_name(player_name)

if __name__ == "__main__":
    main()
