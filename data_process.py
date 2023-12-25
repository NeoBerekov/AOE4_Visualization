import pandas as pd
import requests
import json


# import plotly.express as px
def format_civ_name(civ_name):
    return civ_name.replace('_', ' ').title()
def refresh_overall_solo_data():
    url = 'https://aoe4world.com/api/v0/stats/rm_solo/civilizations'
    response = requests.get(url)
    path = 'data/overall_solo_data.json'
    if response.status_code == 200:
        with open(path, 'w') as f:
            f.write(response.text)
    else:
        print('Error: ', response.status_code)

def get_overall_solo_data():
    with open('data/overall_solo_data.json', 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    # Normalize the 'data' column
    df_normalized = pd.json_normalize(df['data'])

    # Concatenate the normalized DataFrame with the original DataFrame
    df = pd.concat([df, df_normalized], axis=1)

    # Drop the original 'data' column
    df = df.drop(columns=['data'])
    if 'civilization' in df.columns:
        df['Civilization Name'] = df['civilization'].apply(format_civ_name)
    else:
        raise KeyError("Column 'civilization' not found in the data")
    return df

def refresh_Bronze_solo_data():
    url = 'https://aoe4world.com/api/v0/stats/rm_solo/civilizations?rank_level=bronze'
    response = requests.get(url)
    if response.status_code == 200:
        with open('data/Bronze_solo_data.json', 'w') as f:
            f.write(response.text)
    else:
        print('Error: ', response.status_code)

def get_Bronze_solo_data():
    with open('data/Bronze_solo_data.json', 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    # Normalize the 'data' column
    df_normalized = pd.json_normalize(df['data'])

    # Concatenate the normalized DataFrame with the original DataFrame
    df = pd.concat([df, df_normalized], axis=1)

    # Drop the original 'data' column
    df = df.drop(columns=['data'])
    # Add 'civ_name' column with formatted civilization names
    if 'civilization' in df.columns:
        df['Civilization Name'] = df['civilization'].apply(format_civ_name)
    else:
        raise KeyError("Column 'civilization' not found in the data")

    return df

def refresh_Silver_solo_data():

    url = 'https://aoe4world.com/api/v0/stats/rm_solo/civilizations?rank_level=silver'
    response = requests.get(url)
    if response.status_code == 200:
        with open('data/Silver_solo_data.json', 'w') as f:
            f.write(response.text)
    else:
        print('Error: ', response.status_code)

def get_Silver_solo_data():
    with open('data/Silver_solo_data.json', 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    # Normalize the 'data' column
    df_normalized = pd.json_normalize(df['data'])

    # Concatenate the normalized DataFrame with the original DataFrame
    df = pd.concat([df, df_normalized], axis=1)

    # Drop the original 'data' column
    df = df.drop(columns=['data'])
    if 'civilization' in df.columns:
        df['Civilization Name'] = df['civilization'].apply(format_civ_name)
    else:
        raise KeyError("Column 'civilization' not found in the data")

    return df

def refresh_Gold_solo_data():
    url = 'https://aoe4world.com/api/v0/stats/rm_solo/civilizations?rank_level=gold'
    response = requests.get(url)
    if response.status_code == 200:
        with open('data/Gold_solo_data.json', 'w') as f:
            f.write(response.text)
    else:
        print('Error: ', response.status_code)

def get_Gold_solo_data():
    with open('data/Gold_solo_data.json', 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    # Normalize the 'data' column
    df_normalized = pd.json_normalize(df['data'])

    # Concatenate the normalized DataFrame with the original DataFrame
    df = pd.concat([df, df_normalized], axis=1)

    # Drop the original 'data' column
    df = df.drop(columns=['data'])
    if 'civilization' in df.columns:
        df['Civilization Name'] = df['civilization'].apply(format_civ_name)
    else:
        raise KeyError("Column 'civilization' not found in the data")

    return df

def refresh_Platinum_solo_data():
    url = 'https://aoe4world.com/api/v0/stats/rm_solo/civilizations?rank_level=platinum'
    response = requests.get(url)
    if response.status_code == 200:
        with open('data/Platinum_solo_data.json', 'w') as f:
            f.write(response.text)
    else:
        print('Error: ', response.status_code)

def get_Platinum_solo_data():
    with open('data/Platinum_solo_data.json', 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    # Normalize the 'data' column
    df_normalized = pd.json_normalize(df['data'])

    # Concatenate the normalized DataFrame with the original DataFrame
    df = pd.concat([df, df_normalized], axis=1)

    # Drop the original 'data' column
    df = df.drop(columns=['data'])
    if 'civilization' in df.columns:
        df['Civilization Name'] = df['civilization'].apply(format_civ_name)
    else:
        raise KeyError("Column 'civilization' not found in the data")

    return df

def refresh_Diamond_solo_data():
    url = 'https://aoe4world.com/api/v0/stats/rm_solo/civilizations?rank_level=diamond'
    response = requests.get(url)
    if response.status_code == 200:
        with open('data/Diamond_solo_data.json', 'w') as f:
            f.write(response.text)
    else:
        print('Error: ', response.status_code)

def get_Diamond_solo_data():
    with open('data/Diamond_solo_data.json', 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    # Normalize the 'data' column
    df_normalized = pd.json_normalize(df['data'])

    # Concatenate the normalized DataFrame with the original DataFrame
    df = pd.concat([df, df_normalized], axis=1)

    # Drop the original 'data' column
    df = df.drop(columns=['data'])
    if 'civilization' in df.columns:
        df['Civilization Name'] = df['civilization'].apply(format_civ_name)
    else:
        raise KeyError("Column 'civilization' not found in the data")

    return df


def refresh_Conqueror_solo_data():
    url = 'https://aoe4world.com/api/v0/stats/rm_solo/civilizations?rank_level=conqueror'
    response = requests.get(url)
    if response.status_code == 200:
        with open('data/Conqueror_solo_data.json', 'w') as f:
            f.write(response.text)
    else:
        print('Error: ', response.status_code)


def get_Conqueror_solo_data():
    with open('data/Conqueror_solo_data.json', 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    # Normalize the 'data' column
    df_normalized = pd.json_normalize(df['data'])

    # Concatenate the normalized DataFrame with the original DataFrame
    df = pd.concat([df, df_normalized], axis=1)

    # Drop the original 'data' column
    df = df.drop(columns=['data'])
    if 'civilization' in df.columns:
        df['Civilization Name'] = df['civilization'].apply(format_civ_name)
    else:
        raise KeyError("Column 'civilization' not found in the data")

    return df


def refresh_Top_solo_data():
    url = 'https://aoe4world.com/api/v0/stats/rm_solo/civilizations?rank_level=≥conqueror_4'
    response = requests.get(url)
    if response.status_code == 200:
        with open('data/Top_solo_data.json', 'w') as f:
            f.write(response.text)
    else:
        print('Error: ', response.status_code)


def get_Top_solo_data():
    with open('data/Top_solo_data.json', 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    # Normalize the 'data' column
    df_normalized = pd.json_normalize(df['data'])

    # Concatenate the normalized DataFrame with the original DataFrame
    df = pd.concat([df, df_normalized], axis=1)

    # Drop the original 'data' column
    df = df.drop(columns=['data'])
    if 'civilization' in df.columns:
        df['Civilization Name'] = df['civilization'].apply(format_civ_name)
    else:
        raise KeyError("Column 'civilization' not found in the data")
    return df



def refresh_games_data():
    all_games = []
    for page in range(1, 21):
        url = f'https://aoe4world.com/api/v0/games?leaderboard=rm_1v1&page={page}&per_page=50&order=updated_at'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            games = data.get('games', [])
            all_games.extend(games)
            print(f'Page {page} done')
        else:
            print('Error: ', response.status_code)
    with open('data/games_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_games, f)
        print('Games data refreshed')

def get_games_data():
    with open('data/games_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    df = df.drop(columns=['started_at', 'updated_at', 'duration', 'map', 'leaderboard', 'kind', 'patch'])
    df = df.loc[df['ongoing'] == False]
    return df

def refresh_all_solo_data():
    refresh_overall_solo_data()
    refresh_Bronze_solo_data()
    refresh_Silver_solo_data()
    refresh_Gold_solo_data()
    refresh_Platinum_solo_data()
    refresh_Diamond_solo_data()
    refresh_Conqueror_solo_data()
    refresh_Top_solo_data()
    # refresh_games_data()


class SoloData:
    def __init__(self, refresh=False):
        if refresh:
            self.refresh_all()
            print('Data refreshed from API')
        self.ranks_pd = {
            'overall': get_overall_solo_data(),
            'Bronze': get_Bronze_solo_data(),
            'Silver': get_Silver_solo_data(),
            'Gold': get_Gold_solo_data(),
            'Platinum': get_Platinum_solo_data(),
            'Diamond': get_Diamond_solo_data(),
            'Conqueror': get_Conqueror_solo_data(),
            'Top': get_Top_solo_data()
        }
        self.attach_image_url()
        self.add_avg_games_count()
        # self.games_pd = get_games_data()

    def attach_image_url(self):
        for df in self.ranks_pd:
            self.ranks_pd[df]['image_url'] = self.ranks_pd[df]['civilization'].apply(lambda x: f'images/{x}.png')

    def add_avg_games_count(self):
        for rank, df in self.ranks_pd.items():
            avg_games_count = df['games_count'].mean()
            df['avg_games_count'] = avg_games_count

    def refresh_all(self):
        refresh_all_solo_data()
        for rank in self.ranks_pd:
            self.ranks_pd[rank] = globals()[f'get_{rank}_solo_data']()
        # self.games_pd = get_games_data()
        self.attach_image_url()
        self.add_avg_games_count()

    def refresh_rank(self, rank):
        if rank in self.ranks_pd:
            globals()[f'refresh_{rank}_solo_data']()
            self.ranks_pd[rank] = globals()[f'get_{rank}_solo_data']()
            self.attach_image_url()
        else:
            print('Wrong rank name')

    def get_rank(self, rank):
        if rank in self.ranks_pd:
            return self.ranks_pd[rank]
        else:
            print('Wrong rank name')
            return None
    def Sort_by_winrate(self,rank):
        if rank in self.ranks_pd:
            return self.ranks_pd[rank].sort_values(by='win_rate',ascending=False)
        else:
            print('Wrong rank name')
            return None
    def Sort_by_pickrate(self,rank):
        if rank in self.ranks_pd:
            return self.ranks_pd[rank].sort_values(by='pick_rate',ascending=False)
        else:
            print('Wrong rank name')
            return None

    def Sort_by_gamescount(self,rank):
        if rank in self.ranks_pd:
            return self.ranks_pd[rank].sort_values(by='games_count',ascending=False)
        else:
            print('Wrong rank name')
            return None
    # def get_games(self):
    #     return self.games_pd

    def print_all_heads(self):
        for rank, df in self.ranks_pd.items():
            print(f'Rank: {rank}')
            print(df.head())
            print('\n')

