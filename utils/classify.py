class Classifier():

    def __init__(self):
        with open('./saves/pos_bag.txt') as f:
            self.pos_words = set(f.read().split('\n'))
        with open('./saves/neg_bag.txt') as f:
            self.neg_words = set(f.read().split('\n'))

    def classify_text(self, text):
        sentence = set(text.split(' '))
        pos=0
        neg=0

        # count_pos = abs(len(sentence) + len(self.pos_words) - len(set(sentence.add(self.pos_words))))
        # count_neg = abs(len(sentence) + len(self.neg_words) - len(set(sentence.add(self.neg_words))))
        count_pos = len(set(sentence) & set(self.pos_words))
        count_neg = len(set(sentence) & set(self.neg_words))

        # count_pos = len([i for i in sentence if i.lower() in self.pos_words])
        # count_neg = len([i for i in sentence if i.lower() in self.neg_words])
        if count_pos > 0:
            pos = count_pos/(count_neg+count_pos)
        if count_neg > 0:
            neg = count_neg/(count_neg+count_pos)
        
        # print(pos, neg)
        return pos, neg
        


# classifier = Classifier()
# import time
# start=time.time()
# for i in range(100):
#     classifier.classify_text('')
# print("time elapsed", time.time() - start)
