from torch.utils.data import DataLoader
from tqdm.auto import tqdm
import json
import logging
from pathlib import Path
from clear_anonymization.extractors.llm import LLMExtractor
from clear_anonymization.ner_datasets.ler_dataset import LERSample, LERData, LERDataset
from clear_anonymization.extractors import factory
from clear_anonymization.extractors.cache import CacheManager
from clear_anonymization.extractors.base import BaseExtractor


def evaluate_char_level(extractor: LLMExtractor, samples)-> dict[str,float]:
    total_overlap = 0
    total_predicted = 0
    total_gold = 0

    for sample in tqdm(samples,desc= "Evaluation",leave = False):
        text = sample.sentences
        gold_spans = sample.labels
        predicted_spans = extractor.predict(text)
        #print(sample)
        # Compute total predicted span length for this sample.
        sample_predicted_length = sum(pred["end"] - pred["start"] for pred in predicted_spans)
        total_predicted += sample_predicted_length

        # Compute total gold span length once for this sample.
        sample_gold_length = sum(gold["end"] - gold["start"] for gold in gold_spans)
        total_gold += sample_gold_length

        # Now, compute the overlap between each predicted span and each gold span if the label was correctly predicted
        sample_overlap = 0
        for pred in predicted_spans:
            for gold in gold_spans:
                if pred["entity"]== gold["entity"]:
                    print(pred["entity"],gold["entity"])
                    overlap_start = max(pred["start"], gold["start"])
                    overlap_end = min(pred["end"], gold["end"])
                    if overlap_end > overlap_start:
                        sample_overlap += overlap_end - overlap_start
        total_overlap += sample_overlap
    precision = total_overlap / total_predicted if total_predicted > 0 else 0
    recall = total_overlap / total_gold if total_gold > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

    print({"precision": precision, "recall": recall, "f1": f1})
    return {"precision": precision, "recall": recall, "f1": f1}
                    



        

if __name__ == "__main__":
    
    input_dir = Path("data/ler/ler_data.json")
    prompt_path = Path("clear_anonymization/prompts/ner_task_2.txt")
    data = LERData.from_json(json.loads(input_dir.read_text()))
    LLMExtractor = factory.make_extractor("llm", model="google/gemma-3-27b-it", prompt_path=prompt_path)
    evaluate_char_level(LLMExtractor, data.samples[:100])

    
    
    
    
