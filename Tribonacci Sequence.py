def tribonacci(signature, n):
    
    for sequence in range(n - len(signature)):
        signature.append(sum((list(reversed(signature))[:3])))
    
    return signature[:n]
