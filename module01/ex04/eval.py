class Evaluator:
    @staticmethod
    def zip_evaluate(words, coefs):
        if (len(words) == len(coefs)):
            zipped = zip(words, coefs)
            res = 0.0
            for i in zipped:
                res += len(i[0]) * i[1] 
            return res
        else:
            return -1
    def enumerate_evaluate(words, coefs):
        if (len(words) == len(coefs)):
            res = 0.0
            for idx, value in enumerate(words):
                res += len(value) * coefs[idx]
            return res 
        else:
            return -1
