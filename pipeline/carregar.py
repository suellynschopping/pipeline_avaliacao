"""
Pipeline - Etapa 1: Carregar e Explorar Dados
"""

import pandas as pd


def carregar_dados(caminho_arquivo):
    """
    Carrega o dataset de clientes.
    
    Args:
        caminho_arquivo: caminho para o CSV
        
    Returns:
        DataFrame com os dados
    """
    # TODO 1: Use pd.read_csv() para carregar o arquivo
    # Inserido o carregamento dos dados em um bloco de try-catch para tratar eventuais erros
    try:
        df = pd.read_csv(caminho_arquivo)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return None
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return None    
    return df


def explorar_dados(df):
    """
    Mostra informações básicas sobre o dataset.
    
    Args:
        df: DataFrame a ser explorado
    """
    print("=" * 50)
    print("EXPLORAÇÃO DOS DADOS")
    print("=" * 50, end="\n\n")
    
    # TODO 2: Mostre o shape do DataFrame (linhas, colunas)
    print("*" * 50)
    print("\nSHAPE DO DATAFRAME\n")
    
    print(f"Shape: {df.shape}")
    print("=" * 50, end="\n\n")
    
    # TODO 3: Mostre os tipos de cada coluna
    print("*" * 50)
    print("\nTIPOS DAS COLUNAS\n")
    print("*" * 50)
    print(df.dtypes)
    print("=" * 50, end="\n\n")
    
    # Extra1: investiga Valores nulos por coluna 
    print("*" * 50)
    print("\nVALORES NULOS POR COLUNA\n")
    print("*" * 50)
    print(df.isna().sum())
    print("=" * 50, end="\n\n")

    # Extra2: Estatística descritiva
    print("*" * 50)
    print("\nESTATÍSTICAS DESCRITIVAS (VARIÁVEIS NUMÉRICAS)\n")
    print("*" * 50)
    
    numericas = df.select_dtypes(include=["int64", "float64"])
    print(numericas.describe())  # count, mean, std, min, quartis, max
    
    print("=" * 50, end="\n\n")
    
    # Extra3: Detecção de Outliers
    print("*" * 50)
    print("\nOUTLIERS POR COLUNA (CRITÉRIO IQR 1.5)\n")
    print("*" * 50)

    numericas = df.select_dtypes(include=["int64", "float64"])
    if not numericas.empty:
        q1 = numericas.quantile(0.25)
        q3 = numericas.quantile(0.75)
        iqr = q3 - q1

        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr

        mask_outliers = (numericas < limite_inferior) | (numericas > limite_superior)
        outliers_por_coluna = mask_outliers.sum()

        print(outliers_por_coluna)
    else:
        print("Nenhuma coluna numérica encontrada para análise de outliers.")

    print("=" * 50, end="\n\n")


    # TODO 4: Mostre as 5 primeiras linhas
    print("*" * 50)
    print("\nPrimeiras 5 linhas\n")
    print("*" * 50)
    print(df.head())
    print("=" * 50, end="\n")
    
    print("=" * 50)
    print("FIM DA EXPLORAÇÃO DOS DADOS")
    print("=" * 50, end="\n\n")
   

def verificar_target(df, coluna_target='respondeu_campanha'):
    """
    Verifica a distribuição da variável target.
    
    Args:
        df: DataFrame
        coluna_target: nome da coluna target
    """
    print("=" * 50)
    print("\nDISTRIBUIÇÃO DO TARGET")
    print("-" * 30)
    
    # TODO 5: Mostre a contagem de cada valor do target
    print("*" * 50)
    print("\nCONTAGEM DE CADA VALOR DO TARGET\n")
    print("*" * 50)
    print(df[coluna_target].value_counts())
    print("=" * 50, end="\n")
    
    
    # TODO 6: Mostre a proporção (percentual) de cada valor
    print("*" * 50)
    print("\nCONTAGEM DE CADA VALOR DO TARGET\n")
    print("*" * 50)
    print(df[coluna_target].value_counts(normalize=True))
    print("=" * 50, end="\n")    
    
    
    print("\nFIM DA DISTRIBUIÇÃO DO TARGET")
    print("-" * 30)
    print("=" * 50)


# Teste local (executar este arquivo diretamente)
if __name__ == "__main__":
    df = carregar_dados("data/clientes_campanha.csv")
    if df is not None:
        explorar_dados(df)
        verificar_target(df)
    else:
        print("ERRO: DataFrame não foi carregado. Complete o TODO 1!")
