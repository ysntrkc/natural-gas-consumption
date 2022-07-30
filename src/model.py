import pandas as pd
import xgboost as xgb

df = pd.read_csv("../data/data.csv")
df_nem = pd.read_csv("../data/nem_tahmin.csv")
df_sicaklik = pd.read_csv("../data/sicaklik_tahmin.csv")

df["yil"] = df["yil"].astype(str)
df["ay"] = df["ay"].astype(str)
df["tarih"] = df[["yil", "ay"]].agg("-".join, axis=1)

df["yil"] = df["yil"].astype(int)
df["ay"] = df["ay"].astype(int)
df["tarih"] = pd.to_datetime(df["tarih"])

# Setting the "Date" column's period as M (=monthly data)
df["tarih"] = df["tarih"].dt.to_period("M")

df = df.set_index("tarih")

df_nem.columns = ["tarih", "ortalama_nem"]
df_sicaklik.columns = ["tarih", "ortalama_sicaklik"]

df_nem["tarih"] = pd.to_datetime(df_nem["tarih"])
df_sicaklik["tarih"] = pd.to_datetime(df_sicaklik["tarih"])

df_nem["tarih"] = df_nem["tarih"].dt.to_period("M")
df_sicaklik["tarih"] = df_sicaklik["tarih"].dt.to_period("M")

df_merge = df_nem.merge(df_sicaklik, on="tarih", how="left")


def create_features(df):
    """
    Create time series features based on time series index.
    """
    df = df.copy()
    df["quarter"] = df.index.quarter
    df["month"] = df.index.month
    df["year"] = df.index.year
    return df


for ilce in df.ilce.unique():
    df_ilce = df[df.ilce == ilce]
    df_ilce = df_ilce[["tuketim", "ortalama_sicaklik", "ortalama_nem"]]

    if ilce == "ÇATALCA":
        df_ilce = df_ilce[df_ilce.index >= "2016-06"]

    train = df_ilce.loc[(df_ilce.index < "2020-04")]
    test = df_ilce.loc[(df_ilce.index >= "2020-04")]

    df_ilce = create_features(df_ilce)

    train = create_features(train)
    test = create_features(test)

    FEATURES = ["quarter", "month", "year", "ortalama_nem", "ortalama_sicaklik"]
    TARGET = "tuketim"

    X_train = train[FEATURES]
    y_train = train[TARGET]

    X_test = test[FEATURES]
    y_test = test[TARGET]

    reg = xgb.XGBRegressor(
        base_score=0.5,
        booster="gbtree",
        n_estimators=1000,
        early_stopping_rounds=50,
        objective="reg:squarederror",
        max_depth=3,
        learning_rate=0.01,
    )
    reg.fit(
        X_train, y_train, eval_set=[(X_train, y_train), (X_test, y_test)], verbose=100
    )

    test["prediction"] = reg.predict(X_test)
    df_all = pd.concat([train, test], sort=False)
    df_all[["tuketim", "prediction"]].to_csv(f"../data/train_test/{ilce}.csv")

    future = [
        "2021-11",
        "2021-12",
        "2022-01",
        "2022-02",
        "2022-03",
        "2022-04",
        "2022-05",
        "2022-06",
        "2022-07",
        "2022-08",
        "2022-09",
        "2022-10",
        "2022-11",
        "2022-12",
    ]

    df_new = pd.DataFrame(columns=["tuketim"])
    df_new["tarih"] = future
    df_new["tarih"] = pd.to_datetime(df_new["tarih"])
    df_new["tarih"] = df_new["tarih"].dt.to_period("M")
    df_new = df_new.merge(df_merge, on="tarih", how="left")
    df_new = df_new.set_index("tarih")
    df_new = create_features(df_new)

    X = df_new[FEATURES]
    y = df_new[TARGET]

    y = reg.predict(X)
    X[TARGET] = y

    X[["tuketim"]].to_csv(f"../data/tahmin/{ilce}_tahmin.csv")
