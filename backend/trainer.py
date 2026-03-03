from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

model_name = "xlm-roberta-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)

def tokenize(example):
    return tokenizer(example['text'], truncation=True, padding='max_length')

dataset = load_dataset("json", data_files="data.json")
dataset = dataset.map(tokenize, batched=True)
dataset = dataset.rename_column("label", "labels")
dataset.set_format("torch", columns=["input_ids", "attention_mask", "labels"])

model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
training_args = TrainingArguments(output_dir="./results", evaluation_strategy="epoch", num_train_epochs=3)

trainer = Trainer(model=model, args=training_args, train_dataset=dataset["train"])
trainer.train()
model.save_pretrained("saved_model")
tokenizer.save_pretrained("saved_model")
