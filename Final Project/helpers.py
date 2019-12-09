# Adds a column to df for the day by day change of col
def add_day_change(df, cols):
    for col in cols:
        try:
            df[col + '_Diff'] = pd.to_numeric(df[col]).pct_change()
        except:
            print(f"Unable to calculate diff for {col}")


def add_moving_avg(df, col, n):
    try:
        df[f"Moving_Avg_{col}_{n}"] = df[col].rolling(window=5).mean().shift(1)
    except:
        print(f"Unable to calculate moving avg for {col}")
