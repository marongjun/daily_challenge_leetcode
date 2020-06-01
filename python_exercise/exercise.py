import numpy as np

def calculate_FPR(FP, TN):
    FPR = FP/(FP+TN)
    return FPR

def calculate_TPR(TP,FN):
    TPR = TP/(TP+FN)
    return TPR

y_true = [0, 1, 0, 1]
y_score = [0.1, 0.35, 0.4, 0.8]
# False Positive Rate
FPR  = [] 
# True Positive Rate
TPR = []
for ele in y_score:
    temp_pred  = []
    threshold  = ele
    for ele in y_score:
        if ele > threshold:
            temp_pred.append(1)
        else:
            temp_pred.append(0)
    FP  = 0
    TN = 0
    TP = 0
    FN  = 0
    temp = np.array(y_true) - np.array(temp_pred)
    for idx, num in enumerate(temp):
        if num < 0:
            FP += 1
        if num == 0  and y_true[idx] == 1:
            TP += 1
        if num == 0 and y_true[idx] == 0:
            TN += 1
        if num > 0:
            FN += 1
    print(FN,TP,TN,FP)

    FPR.append(calculate_FPR(FP,TN))
    TPR.append(calculate_TPR(TP,FN))

print(FPR,TPR)