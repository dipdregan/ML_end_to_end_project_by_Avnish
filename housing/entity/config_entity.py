from collections import namedtuple

DataIngestionConfig = namedtuple('DataIngestionConfig',
                                 ['dataset_download_url','raw_data_dir','tgz_download_dir',
                                  'ingested_dir','ingested_train_dir','ingested_test_dir'])

DataValidationConfig = namedtuple('DataValidationConfig',['schema_file_path','report_file_path',
                                                          'report_page_file_path'])

# DataTransformationConfig = namedtuple()

# ModelTrainerConfig = namedtuple()

# ModelEvaluationConfig = namedtuple()

# ModelPusherConfig = namedtuple()

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",['artifact_dir'])