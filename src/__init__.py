import os
from pathlib import Path

MODEL_URL = 'https://drive.google.com/drive/folders/1-Sw27Qk8jNpiC-Vf8vAaZy3Qwm0MVBB9'

MODEL_DIR = Path(os.getcwd()).parent / 'models'

BERT_FOLDER = 'bert_topic_modeling'

id2label = {0: '0d817400-3f5d-41e0-929c-c31fdbe75d31',
            1: '39822b5f-e37e-43e8-b997-7142fe55c3ea',
            2: 'ca197b81-ca86-4792-8c25-2ba7cd4195b5',
            3: 'b49207eb-96eb-4b73-b534-adc0ef85022a',
            4: '6fbf954a-03f9-4782-a65f-783271c9c447',
            5: '9ff54ded-904b-4e0c-85ce-a3617f5cb913',
            6: '74e2fab8-689f-4e17-9a1c-e1f92e084f55',
            7: '9a06646a-e1df-4fca-888e-69658420556b',
            8: '96326734-fd82-4350-b45c-513e7eb9147c',
            9: 'f5cdd7f2-9d4d-4ba5-9925-00c1701e30fa',
            10: 'e7cbe38d-c987-4113-aa94-fd77eda451d5',
            11: 'aa1edc37-1a01-414a-bcf7-8517e7c7053d',
            12: 'ebf2991e-4b7d-44c6-927b-a261a7b21d2c',
            13: 'a58b4b70-1b59-4240-917d-a2165a0ce2f0',
            14: '83a09c6b-5f2f-421f-ae50-b38acca7e008'}
