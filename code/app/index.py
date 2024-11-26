# -*- coding: utf-8 -*-
"""
Codigo para testar o PySpark (API em Python do Spark)
"""

# Importar as funcoes do PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Criar uma SparkSession, o ponto de entrada para o PySpark
spark = SparkSession.builder.getOrCreate()

seed = 42

# Dataframe do PySpark com dados do cliente
# 100 linhas aleatorias representando o ID do cliente e a sua idade
# Colunas:
# * id_cliente
# * idade
df_cliente = (
    spark.range(100)
    .select(
        F.col("id").alias("id_cliente"),
        (F.randn(seed=seed) * 3 + 35).cast("int").alias("idade")
    )
)

# Dataframe do PySpark com dados de compras do cliente
# 100.000 linhas aleatorias relacionando o ID do cliente com uma compra
# Colunas:
# * id_cliente
# * valor
df_compra = (
    spark.range(100000)
    .select(
        (F.rand(seed=seed) * 100).cast("int").alias("id_cliente"),
        (F.abs((F.randn(seed=seed) * 50) + (F.rand(seed=seed) * 1000))).cast("decimal(16,2)").alias("valor")
    )
)

# Dataframe do PySpark
# Realiza a juncao dos dataframes de cliente com compras
# Em seguida, realiza um agrupamento para calcular algumas metricas de compras por idade
# Colunas:
# * idade
# * qtd
# * min_valor
# * avg_valor
# * max_valor
df_compra_idade = (
    df_cliente.alias("a")
    .join(
        other=df_compra.alias("b"),
        how="left",
        on=[F.col("a.id_cliente") == F.col("b.id_cliente")]
    )
    .select(
        "a.id_cliente",
        "a.idade",
        "b.valor",
    )
    .groupBy("idade").agg(
        F.count("*").alias("qtd"),
        F.min("valor").alias("min_valor"),
        F.avg("valor").alias("avg_valor"),
        F.max("valor").alias("max_valor"),
    )
    .orderBy("idade")
)

# Mostra os dados do dataframe final
df_compra_idade.show(250, truncate=False)