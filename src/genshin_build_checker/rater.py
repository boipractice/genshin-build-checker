import random

# shuffle the builds the same way every run, then split them into train (75%) and test (25%)
def train_test_split(items, test_fraction=0.25, seed=0):
    order = list(range(len(items)))
    random.Random(seed).shuffle(order)
    n_test = round(len(items) * test_fraction)
    test = [items[i] for i in order[:n_test]]
    train = [items[i] for i in order[n_test:]]
    return train, test



