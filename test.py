from src.utils.config import config
from src.utils.logger import default_logger as logger
from src.data.data_loader import DataLoader
from src.data.data_processor import DataProcessor

if __name__ == "__main__":
    try:
        config
        logger.info("Initialize class")
        data_loader = DataLoader()
        data_processing = DataProcessor()
        
        logger.info("Start load data")
        df_train, df_test = data_loader.load_data()
        logger.info("Data loaded successfully")
        
        logger.info("Start preprocessing data")
        X,y = data_processing.fit_transform(df_train)
        logger.info("Preprocessing completed successfully")
    except Exception as e:
        logger.info(f"Failed load data: {e}")