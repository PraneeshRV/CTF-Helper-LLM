from transformers import TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model

# Apply LoRA fine-tuning (Low-Rank Adaptation)
peft_config = LoraConfig(
    r=8,
    lora_alpha=16,
    lora_dropout=0.1,
    target_modules=["q_proj", "v_proj"],
    bias="none",
    task_type="CAUSAL_LM"
)

# Apply PEFT model
model = get_peft_model(model, peft_config)

# Define training parameters
training_args = TrainingArguments(
    output_dir="./lily-ctf-finetuned",
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    num_train_epochs=3,
    save_steps=500,
    save_total_limit=2,
    evaluation_strategy="epoch",
    logging_dir="./logs",
    report_to="wandb",
    fp16=True,
    gradient_accumulation_steps=4,
    optim="adamw_torch"
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    tokenizer=tokenizer
)

# Train the model
trainer.train()
model.save_pretrained("./ctf-writeup-model")
tokenizer.save_pretrained("./ctf-writeup-model")
