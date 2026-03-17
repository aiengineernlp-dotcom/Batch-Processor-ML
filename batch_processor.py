# batch_processor.py

"""
ML Mini Batch processor.
Use case: Simulate the corps training loop batch logic used in Pytorch Dataloader, before using the framework

#=========
Petit Batch processor.
Cas usage: Ici on veut simmuler le dataloader de Pytorch. cella permet ce comprendre comment les donnees
sont DECOUPEES et MELANGEES avant d'entrer dans le modele. L'idee est de transformmer un dataset complet
en petit morceau (mini batches) pour obtimiser la memoire et l'apprentissage [2,3]


"""

import random

random.seed(42)


def create_dataset(n_samples: int) -> list[
    dict]:  # cette fonction retourne une liste de dictionnaires avec un id,les features et le label (0/1)
    '''Generate a synthetic classification dataset'''
    return [
        {
            "id": i,
            "features": [round(random.gauss(0, 1), 4) for _ in range(5)],  #
            "label": random.choice([0, 1])
            # je crois que vu que c'est la classification (oui ou non), on doit avoir cette cette ligne mais qui doit etre aleatoire
        }
        for i in range(n_samples)
    ]


def shuffle_dataset(dataset: list) -> list:  # cette fonction melange les donnnes crees
    '''Shuffle dataset - standart before each epoch '''
    shuffled = dataset[:]  # copie independante
    random.shluffle(shuffled)
    return shuffled


def create_batches(dataset: list, batch_size: int) -> list[list]:
    '''
    split dataset into mini batches:

    Args:
        datasets : Full dataset as a list
        batch_size: Size of each batch
    Returns:
        List of Batches (each batch is a list of samples)
    '''

    return [
        dataset[i:i + batch_size]
        for i in range(0, len(dataset), batch_size)
    ]  # avant le for je ne comprend pas


def simulate_forward_pass(batch: list) -> float:
    pass














