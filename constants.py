NUM_FEATURES = 10
NUM_CLASSES = 2
PRIOR_PROBABILITY = 0.5
LAMDBA = 0.000001
M = 8
CFN = 1
CFP = 10
EFFECTIVE_PRIOR = (PRIOR_PROBABILITY * CFN)/((PRIOR_PROBABILITY * CFN) + (1-PRIOR_PROBABILITY) * CFP) 