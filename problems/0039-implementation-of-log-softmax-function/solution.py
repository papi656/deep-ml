import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code
	max_score = max(scores)
	scores_exp = [np.exp(score-max_score) for score in scores]
	log_term = np.log(sum(scores_exp))
	lg_sftmx = [score - max_score - log_term for score in scores]
	return lg_sftmx

	pass
