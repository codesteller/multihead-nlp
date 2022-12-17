import utils.clean_data as dc
import tqdm
import utils.db as db


def main():
    # json_filelist = dc.get_all_json_files("./dataset_300k/2-3LFile/")
    # lines = dict()
    # num_lines = 0
    # for json_file in tqdm.tqdm(json_filelist):
    #     try:
    #         json_objects = dc.get_all_json_objects(json_file)
    #         num_lines += len(json_objects[0])
    #     except:
    #         print(json_file)
    #         continue
    
    # print(len(json_filelist), num_lines)

    nlp_db = db.NLP_Dataset(
        [
            "./dataset_300k/0-1Lfile/dataset_2022-07-16 13_10_42.434191.json",
            "./dataset_300k/0-1Lfile/dataset_2022-07-16 13_11_36.329972.json",
        ]
    )
    print(len(nlp_db.sentences))


if __name__ == "__main__":
    main()

