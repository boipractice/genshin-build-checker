import random

# shuffle the builds the same way every run, then split them into train (75%) and test (25%)
def train_test_split(items, test_fraction=0.25, seed=0):
    order = list(range(len(items)))
    random.Random(seed).shuffle(order)
    n_test = round(len(items) * test_fraction)
    test = [items[i] for i in order[:n_test]]
    train = [items[i] for i in order[n_test:]]
    return train, test

def crit_value(build):
    return build.crit_rate * 2 + build.crit_dmg

def learn_cutoff(train):
    good = [b for b in train if b.good == 1]
    weak = [b for b in train if b.good == 0]

    good_avg = sum(crit_value(b) for b in good) / len(good)
    weak_avg = sum(crit_value(b) for b in weak) / len(weak)
    return (good_avg + weak_avg) / 2

    



