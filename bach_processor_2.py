# batch_processor_ml_version_2

import  random
random.seed(42)

def create_dataset(n_sample:int)->list[dict]:
    return [
        {
            "id": id,
            "feature" :[
                round(random.gauss(0,1),4) for _ in range(5)
            ]
            ,
            "label": random.choice([0,1])

        } for i in range(n_sample)

    ]

def create_shuffled_dataset(dataset:list)->list:
    # copie de mon dataset pour la comparaison
    shuffled_dataset = dataset[:]
    random.shuffle(shuffled_dataset)
    return shuffled_dataset


def create_batches(dataset:list, batch_size:int)->list:
    pass

