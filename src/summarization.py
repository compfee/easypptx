from transformers import MBartTokenizer, MBartForConditionalGeneration

class Summarizer():

    def __init__(self):
        pass

    def summ_text(self, text, model_name):
        tokenizer = MBartTokenizer.from_pretrained(model_name)
        model = MBartForConditionalGeneration.from_pretrained(model_name).to("cuda")
        # print(text['Text'])
        input_ids = tokenizer(
            text.to_list(),
            max_length=1000,
            truncation=True,
            return_tensors="pt",
        )["input_ids"].to("cuda")

        output_ids = model.generate(
            max_length=500,
            min_length=40,
            length_penalty=5,
            input_ids=input_ids,
            no_repeat_ngram_size=4
        )[0]
        summary = tokenizer.decode(output_ids, skip_special_tokens=True)

        return summary