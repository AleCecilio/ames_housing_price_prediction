from src import prepare_data
from src import feature_engineering
from src import train_model
# from src import predict 

def main():
    prepare_data()
    feature_engineering()
    train_model()
    
if __name__ == "__main__":
    main()