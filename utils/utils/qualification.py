import pandas as pd

def analyze_qualification(points_table):
    """
    Takes points table data,
    returns qualification prediction.
    """
    df = pd.DataFrame(points_table)
    df.sort_values(["points", "netRunRate"], ascending=False, inplace=True)

    # simple logic
    qualifiers = df.head(4)  # top 4 usually
    return qualifiers.to_dict(orient="records")

def remaining_win_req(team, target_points, df):
    """
    Tells how many match wins required to reach target.
    """
    current = df.loc[df["team"] == team, "points"].values[0]
    needed = max(0, target_points - current)
    return needed
