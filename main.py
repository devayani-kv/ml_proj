from src.ML_Proj import logger
from src.ML_Proj.pipeline.part_1_data_ingestion import DataIngestionTrainingPipeline
from src.ML_Proj.pipeline.part_2_data_validation import DataValidationTrainingPipeline
from src.ML_Proj.pipeline.part_3_data_transformation import DataTransformationTrainingPipeline
from src.ML_Proj.pipeline.part_4_model_trainer import ModelTrainingPipeline
from src.ML_Proj.pipeline.part_5_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"### stage {STAGE_NAME} started ###")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"### stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "Data Validation"

try:
    logger.info(f"### stage {STAGE_NAME} started ###")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f"### stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Data Transformation"

try:
    logger.info(f"### stage {STAGE_NAME} started ###")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f"### stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training"

try:
    logger.info(f"### stage {STAGE_NAME} started ###")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"### stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation"

try:
    logger.info(f"### stage {STAGE_NAME} started ###")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f"### stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e