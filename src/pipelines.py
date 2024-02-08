from tqdm import tqdm
from pipelines.summarization import Summarizer
import config
import pandas as pd
from pipelines.pdf_parse import PDFParser

def pipeline_sum(data, model, max_length=70):
    '''Summarization pipeline'''
    result_text = []
    summa = Summarizer()
    for i in tqdm(range(0, len(data))):
        new_text = data['Text'][i:i+1]
        result_text.append(summa.summ_text(new_text, model))
    print(result_text)
    df = pd.DataFrame(result_text, columns=['Summary'])
    df.to_csv(f"{config.PATH_DATA}/{config.NAME_DATA_SUMMARY}", index=False)
    return result_text

def pipeline_parse(file):
    parser = PDFParser()
    text, file_name = parser.parse_text(file)
    return text, file_name