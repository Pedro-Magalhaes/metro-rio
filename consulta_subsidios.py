import basedosdados as bd

# Para carregar o dado direto no pandas
df = bd.read_sql(
    "SELECT * FROM `datario.transporte_rodoviario_municipal.subsidio_onibus`",
    billing_project_id="<id-projeto->",
)

df.to_csv('dados_subsidio_onibus.csv')