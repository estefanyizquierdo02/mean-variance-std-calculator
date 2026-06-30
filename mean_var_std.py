import numpy as np

def calculate(lista):
    if len(lista) != 9:
        raise ValueError("La lista debe contener nueve números")
    
    a = np.array(lista).reshape(3, 3)
    
    return {
        'mean': [a.mean(axis=0).tolist(), a.mean(axis=1).tolist(), a.mean()],
        'variance': [a.var(axis=0).tolist(), a.var(axis=1).tolist(), a.var()],
        'standard deviation': [a.std(axis=0).tolist(), a.std(axis=1).tolist(), a.std()],
        'max': [a.max(axis=0).tolist(), a.max(axis=1).tolist(), a.max()],
        'min': [a.min(axis=0).tolist(), a.min(axis=1).tolist(), a.min()],
        'sum': [a.sum(axis=0).tolist(), a.sum(axis=1).tolist(), a.sum()]
    }
