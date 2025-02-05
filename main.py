import pandas as pd

df = pd.read_csv("dados_subsidio_onibus.csv")

df = df.sort_values("data")

clean_df = df.loc[
    :,
    [
        "data",
        "consorcio",
        "viagens",
        "km_apurada",
        "km_planejada",
        "perc_km_planejada",
        "valor_subsidio_pago",
        "valor_penalidade",
    ],
].assign(  # Aplicar transformações nas colunas
    data=lambda df: df["data"].apply(pd.to_datetime, format="%Y-%m-%d"),
    viagens=lambda df: df["viagens"].astype(float),
    km_apurada=lambda df: df["km_apurada"].astype(float),
    km_planejada=lambda df: df["km_planejada"].astype(float),
    perc_km_planejada=lambda df: df["perc_km_planejada"].astype(float),
    valor_subsidio_pago=lambda df: df["valor_subsidio_pago"].astype(float),
    valor_penalidade=lambda df: df["valor_penalidade"].astype(float),
)
print(clean_df.head())

# clean_df.loc[:, ["data", "consorcio", "valor_subsidio_pago"]].groupby(
#     [pd.Grouper(key="data", freq="M"), "consorcio"]
# ).sum().to_csv('sub_mensal.csv')

grouped_df = clean_df.groupby([pd.Grouper(key="data", freq="ME"), "consorcio"]).sum()

# grouped_def["data"] = grouped_def["data"].apply(lambda x: x.strftime("%Y-%m"))
# print(grouped_df.head())
grouped_df.to_csv("sub_mensal.csv", date_format="%Y-%m")

# print(clean_df.loc[:,"data", "consorcio", "valor_subsidio_pago"].groupby(["data", "consorcio"]).sum())
