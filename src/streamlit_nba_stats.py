import streamlit as st
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import pandas as pd

def fetch_player_stats(player_name):
    # Search for the player by name
    player_dict = players.get_players()
    player = [player for player in player_dict if player['full_name'].lower() == player_name.lower()]

    if not player:
        return None, "Player not found."

    # Fetch the career stats for the found player
    career = playercareerstats.PlayerCareerStats(player_id=player[0]['id'])
    career_stats_df = career.get_data_frames()[0]
    return career_stats_df, None

def main():
    st.title('NBA Player Statistics Viewer')
    
    # User input for player name
    player_name = st.text_input("Enter the name of the player:", '')

    if st.button('Show Stats'):
        if player_name:
            stats_df, error = fetch_player_stats(player_name)
            if error:
                st.error(error)
            else:
                st.write(f"Displaying career stats for {player_name}:")
                st.dataframe(stats_df)
        else:
            st.error("Please enter a valid player name.")

if __name__ == '__main__':
    main()
