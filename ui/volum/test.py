# import shellinford
#
# fm = shellinford.FMIndex()
# fm.build(['Milky Holmes', 'Sherlock "Sheryl" Shellingford', 'Milky'], 'milky.fm')
#
# for doc in fm.search('Milky'):
#     print('doc_id:', doc.doc_id)
#     print('count:', doc.count)
#     print('text:', doc.text)
#
# for doc in fm.search(['Milky', 'Holmes']):
#     print('doc_id:', doc.doc_id)
#     print('count:', doc.count)
#     print('text:', doc.text)
# fm.count('Milky')
# fm.count(['Milky', 'Holmes'])

def rotations(t):
    """	Return	list	of	rotations	of	input	string	t	"""
    tt = t * 2
    return [tt[i:i + len(t)] for i in range(0, len(t))]


def bwm(t):
    """	Return	lexicographically	sorted	list	of	t’s	rotations	"""
    return sorted(rotations(t))


def bwtViaBwm(t):
    """	Given	T,	returns	BWT(T)	by	way	of	the	BWM	"""
    return ''.join(map(lambda x: x[-1], bwm(t)))


b = "Tomorrow_and_tomorrow_and_tomorrow$"
for i in range(50):
    b = bwtViaBwm(b)
    print(f"{i} | {b}")
