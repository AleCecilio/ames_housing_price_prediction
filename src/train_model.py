from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from src.data_io import load_processed, save_model

 

def train_model():
    df = load_processed("Ames_Final_DF.csv")
 
    X = df.drop('SalePrice', axis=1)
    y = df['SalePrice']
 
 
    # Dividir em treino e teste 
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.1, random_state=101
    )
    
    
    # ── 3. Treinar modelo 
    # Hiperparâmetros definidos com base na exploração do notebook 03_modeling.ipynb
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', Lasso(alpha=100, max_iter=100000))
    ])
    
    pipeline.fit(X_train, y_train)

    save_model(pipeline, "lasso_model.joblib")