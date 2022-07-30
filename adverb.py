def isAdverb(data):
    if data.typeArb == "RB" or data.typeArb == "RBR" or data.typeArb == "RBS" or data.typeArb == "WRB":
        return True
    else:
        return False