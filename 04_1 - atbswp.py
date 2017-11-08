spam = ['apples',
        'bananas',
        'tofu',
        'cats',
        'mermaids',
        'dogs',
        'tests',
        ]

for i in range(0, len(spam)-2):
    print(spam[i], end=', ')

print(spam[-2] + " and " + spam[-1])
