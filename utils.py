import os
import pickle


def file_extension(p):
    return os.path.splitext(p)[1]


def save_pickle(obj, file_name: str, verbose=False):
    if file_extension(file_name) != '.pkl':
        file_name += '.pkl'

    directory = os.path.dirname(file_name)
    if not os.path.isdir(directory) and directory != '':
        os.makedirs(directory)
        if verbose: print("Created directory:", directory)

    with open(file_name, 'wb') as f:
        pickle.dump(obj, f)
        if verbose: print("Saved as:", file_name)


def load_pickle(file_name: str, verbose=False):
    if file_extension(file_name) != '.pkl':
        file_name += '.pkl'

    with open(file_name, 'rb') as f:
        p = pickle.load(f)
        if verbose: print("Loaded file:", f)
        return p