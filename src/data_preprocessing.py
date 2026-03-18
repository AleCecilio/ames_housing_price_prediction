from src.data_io import load_raw, save_processed


"""
Módulo responsável pela preparação dos dados.

Etapas:
- Remoção de outliers
- Tratamento de valores ausentes
- Geração do dataset final limpo
"""


def remove_outliers(df):
    """Remove observações com área muito grande e preço anormalmente baixo."""

    mask = (df['Gr Liv Area'] > 4000) & (df['SalePrice'] < 400000)
    df = df.drop(df[mask].index)

    return df


def handle_missing_data(df):
    """Aplica tratamento de valores ausentes."""

    # Remover coluna de identificação
    df = df.drop(columns='PID')

    # Remover linhas com dados críticos faltantes
    df = df.dropna(subset=['Electrical', 'Garage Cars'])

    # Basement 

    bsmt_num_cols = [
        'Bsmt Full Bath',
        'Bsmt Half Bath',
        'Bsmt Unf SF',
        'BsmtFin SF 1',
        'BsmtFin SF 2',
        'Total Bsmt SF'
    ]

    df[bsmt_num_cols] = df[bsmt_num_cols].fillna(0)

    bsmt_str_cols = [
        'Bsmt Qual',
        'Bsmt Cond',
        'Bsmt Exposure',
        'BsmtFin Type 1',
        'BsmtFin Type 2'
    ]

    df[bsmt_str_cols] = df[bsmt_str_cols].fillna('None')

    # Masonry Veneer 

    df['Mas Vnr Type'] = df['Mas Vnr Type'].fillna('None')
    df['Mas Vnr Area'] = df['Mas Vnr Area'].fillna(0)

    # Garage 

    garage_cols = [
        'Garage Type',
        'Garage Qual',
        'Garage Finish',
        'Garage Cond'
    ]

    df[garage_cols] = df[garage_cols].fillna('None')
    df['Garage Yr Blt'] = df['Garage Yr Blt'].fillna(0)

    #  Colunas com muitos NaN 

    df = df.drop(columns=['Pool QC', 'Misc Feature', 'Alley', 'Fence'])

    df['Fireplace Qu'] = df['Fireplace Qu'].fillna('None')

    # Lot Frontage 
    # Preencher usando mediana do bairro

    median_by_neigh = df.groupby('Neighborhood')['Lot Frontage'].transform('median')
    df['Lot Frontage'] = df['Lot Frontage'].fillna(median_by_neigh)

    # Caso ainda reste missing
    df['Lot Frontage'] = df['Lot Frontage'].fillna(0)

    return df


def prepare_data():
    # 1 Carregar dados brutos
    df = load_raw("Ames_Housing_Data.csv")

    # 2 Remover outliers
    df = remove_outliers(df)
    save_processed(df, "Ames_outliers_removed.csv")

    # 3 Tratar valores ausentes
    df = handle_missing_data(df)
    save_processed(df, "Ames_NO_missing_data.csv")

    return df