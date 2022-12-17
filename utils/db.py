import nltk
# import tensorflow as tf
import json
import tqdm


class NLP_Dataset:
    def __init__(self, json_paths) -> None:
        self.data = None
        self.tokenizer = None
        self.vocab_size = None
        self.max_length = None
        self.embedding_dim = None
        self.lang = ["english", "bengali", "hindi"]
        self.json_paths = json_paths
        self.sentences = self.get_sentences()

    @staticmethod
    def _load_json(j_path):
        """
        Returns a dictionary of data loaded from the json file.
        """
        with open(j_path, "r") as f:
            data = json.load(f)
        return data

    def get_sentences(self):
        """
        Returns a list of sentences from the json files.
        """
        sentences = []
        for j_path in tqdm.tqdm(self.json_paths):
            data = self._load_json(j_path)
            for id in data:
                if self._clean_sentence(data[id]):
                    sentences.append(data[id])
        return sentences
    
    @staticmethod
    def _clean_sentence(i_sentence):
        """
        Returns True if the sentence is clean, False otherwise.
        """
        _status = True

        # Add logic to check if the sentence is clean.
        # If not, set _status to False.


        return _status
        


if __name__ == "__main__":
    nlp_db = NLP_Dataset(
        [
            "./dataset_300k/0-1Lfile/dataset_2022-07-16 13_10_42.434191.json",
            "./dataset_300k/0-1Lfile/dataset_2022-07-16 13_11_36.329972.json",
        ]
    )
    print(nlp_db.data)
