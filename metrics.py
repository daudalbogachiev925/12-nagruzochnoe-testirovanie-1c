import statistics

def apdex(times, threshold=0.5):
    satisfied = sum(1 for t in times if t <= threshold)
    tolerating = sum(1 for t in times if threshold < t <= 4*threshold)
    return (satisfied + tolerating/2) / len(times)
