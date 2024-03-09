import os
import config
import uvicorn
import pandas as pd
from src.pipelines import pipeline_parse, pipeline_sum, pipeline_gen_slide
from fastapi import FastAPI, UploadFile, File
from transformers import MBartTokenizer, MBartForConditionalGeneration

tokenizer = MBartTokenizer.from_pretrained(config.model_sum)
model = MBartForConditionalGeneration.from_pretrained(config.model_sum).to("cuda")

app = FastAPI()

@app.post('/file')
async def upload_file(file: UploadFile = File(...)):
    data, parsed_file_name = pipeline_parse(file.filename)
    data.to_csv(f"{config.PATH_DATA}/{config.NAME_DATA_DF}", index=False)
    return {'message': 'Файл загружен'}

@app.post('/get_summarize')
def get_summarize():
    if f"{config.NAME_DATA_DF}" in os.listdir(f"{config.PATH_DATA}"):
        data = pd.read_csv(f"{config.PATH_DATA}/{config.NAME_DATA_DF}")
        return pipeline_sum(data, config.model_sum)

@app.post('/get_slides')
def get_slides():
    # data = pd.read_csv(f"{config.PATH_DATA}/{config.NAME_DATA_SUMMARY}")

    return pipeline_gen_slide(f"{config.PATH_DATA}/{config.NAME_DATA_PARSED}", config.NAME_PATTERN)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=80)