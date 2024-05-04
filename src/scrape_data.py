from nba_api.stats.endpoints import playercareerstats
import pandas as pd

def fetch_player_stats(player_id):
    # Fetch player career stats using the NBA API
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    
    # Getting DataFrames
    career_stats_df = career.get_data_frames()[0]

    # Getting JSON data
    career_stats_json = career.get_json()

    # Getting dictionary
    career_stats_dict = career.get_dict()

    # Displaying data (You can choose to do different things with these data forms)
    print("Player Career Stats DataFrame:")
    print(career_stats_df.head())  # Shows the top entries in the DataFrame

    print("\nPlayer Career Stats JSON:")
    print(career_stats_json[:500])  # Shows first 500 characters of the JSON string

    print("\nPlayer Career Stats Dictionary:")
    print(list(career_stats_dict.keys()))  # Shows the keys of the dictionary

    # Optionally, you can return these if you need to use the data outside this function
    return career_stats_df, career_stats_json, career_stats_dict

# Example usage
if __name__ == "__main__":
    # Nikola Jokić's player ID
    nikola_jokic_id = '203999'
    fetch_player_stats(nikola_jokic_id)
