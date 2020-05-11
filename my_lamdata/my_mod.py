def enlarge(n):
    return n *100

def nully(df):
    return df.isnull().sum()

def time_split(dt_list):
    dt_list = pd.to_datetime(dt_list, infer_datetime_format=True)
    X['Year'] = dt_list.dt.year
    X['Month'] = dt_list.dt.month
    X['Day'] = dt_list.dt.day
    return (X['Year'])
    return X['Month']
    return X['Day']


if __name__ == "__main__":


    x = 5
    print(enlarge(x))

    y = int(input("Please choose a number:"))
    print(enlarge(y))