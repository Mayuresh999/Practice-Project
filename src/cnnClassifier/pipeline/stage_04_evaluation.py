from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier import logger
from cnnClassifier.components.evaluation import Evaluation


STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
 
if __name__ == "__main__":
    try:
        logger.info("********************")
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx===================x")
    except Exception as e:
        raise e