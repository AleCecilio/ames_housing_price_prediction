from src import prepare_data
from src import feature_engineering


def main():
    df = prepare_data()
    df = feature_engineering()
    
if __name__ == "__main__":
    main()