# import json
# from pathlib import Path
# from transformers import DistilBertTokenizerFast, TFDistilBertForQuestionAnswering
# import tensorflow as tf
# from datasets import load_dataset, load_metric
# from transformers import AutoTokenizer
# from transformers import AutoModelForQuestionAnswering, TrainingArguments, Trainer

from datasets import load_dataset
data = load_dataset('squad2.py', data_files={
                    'train': 'train-v2.0.json', 'dev': 'dev-v2.0.json'})
print(data)
