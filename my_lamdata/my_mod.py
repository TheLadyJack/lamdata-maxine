def enlarge(n):
    return n *100

def nully(df):
    return df.isnull().sum()

def time_split(X[dt_list]):
    X[dt_list] = pd.to_datetime(X[dt_list], infer_datetime_format=True)

  X['Year'] = X[dt_list].dt.year
  X['Month'] = X[dt_list].dt.month
  X['Day'] = X[dt_list].dt.day


if __name__ == "__main__":


    x = 5
    print(enlarge(x))

    y = int(input("Please choose a number:"))
    print(enlarge(y))