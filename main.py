import pandas as pd
import sys

class League_game_analyse():

    def catch_csv(self, file: str) -> pd.DataFrame:
        return pd.read_csv(file)

    def display_n_line_csv(self, file: pd.DataFrame, n: int) -> int:
        return file.head(n)

    def number_of_games(self, file: pd.DataFrame) -> int:
        return pd.DataFrame(file).shape[0]

    def number_of_games_lfl(self, file: pd.DataFrame) -> int:
        return self.number_of_games(file.loc[file['league'] == 'LFL'])

    def redside_winrate(self, df: pd.DataFrame) -> float:
        total: int = self.number_of_games(df)
        red_win: int = self.number_of_games(df.loc[df['result'] == 0])

        return red_win / total

    def list_equip_lfl(self, df: pd.DataFrame) -> pd.DataFrame:
        new_df: pd.DataFrame = df[df["league"] == "LFL"]

        return new_df["blueteam"].drop_duplicates()

    def top_pick_mid(self, df: pd.DataFrame):
        tmp = pd.concat([df["redmid"], df["bluemid"]])
        element_counts = tmp.value_counts()

        return element_counts.idxmax()

    def ranking_all_pick(self, df: pd.DataFrame):
        frames: list = [
            df["bluemid"],
            df["redmid"],
            df["redtop"],
            df["bluetop"],
            df["redjungle"],
            df["bluejungle"],
            df["redadc"],
            df["blueadc"],
            df["redsupport"],
            df["bluesupport"]]

        return pd.concat(frames).value_counts()[:5].index.tolist()


if __name__ == "__main__":
    analyse: League_game_analyse = League_game_analyse()
    file: pd.DataFrame = analyse.catch_csv(sys.argv[1])
    # number = int(sys.argv[2])
    # print(analyse.display_n_line_csv(file, number))
    # print(analyse.number_of_games(file))
    # print(analyse.number_of_games_lfl(file))
    # print(analyse.redside_winrate(file))
    # print(analyse.list_equip_lfl(file))
    # print(analyse.top_pick_mid(file))
    print(analyse.ranking_all_pick(file))