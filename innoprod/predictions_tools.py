import pandas
from transformers.trainer_utils import PredictionOutput

def prediction_output_to_df(prediction_output: PredictionOutput,) -> pandas.DataFrame:
    n_labels = prediction_output.predictions.shape[1]
    data_dict = {f"Prediction:{i}": prediction_output.predictions[:,i] for i in range(n_labels)}
    data_dict['True label'] = prediction_output.label_ids
    return pandas.DataFrame(data_dict)
