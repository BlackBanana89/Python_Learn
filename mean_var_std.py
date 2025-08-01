import numpy as np

def calculate(list):
    
    if len(list) < 9  :
        raise ValueError('List must contain nine numbers.')
    else:
        calc_array = np.array (list)
        calc_array = calc_array.reshape(3, 3)
        calculations = {
  'mean': [calc_array.mean(axis=0).tolist(), calc_array.mean(axis=1).tolist(), calc_array.flatten().mean().tolist()],
  'variance': [calc_array.var(axis=0).tolist(), calc_array.var(axis=1).tolist(), calc_array.flatten().var().tolist()],
  'standard deviation': [calc_array.std(axis=0).tolist(), calc_array.std(axis=1).tolist(), calc_array.flatten().std().tolist()],
  'max': [calc_array.max(axis=0).tolist(), calc_array.max(axis=1).tolist(), calc_array.flatten().max().tolist()],
  'min': [calc_array.min(axis=0).tolist(), calc_array.min(axis=1).tolist(), calc_array.flatten().min().tolist()],
  'sum': [calc_array.sum(axis=0).tolist(), calc_array.sum(axis=1).tolist(), calc_array.flatten().sum().tolist()]
}
    return calculations