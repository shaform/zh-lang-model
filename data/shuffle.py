import argparse
import os
import random

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--indir', required=True)
    parser.add_argument('--outdir', required=True)
    parser.add_argument('--seed', default=633)
    args = parser.parse_args()

    random.seed(args.seed)

    lines = []
    for i in range(1, 108 + 1):
        infile = '{}/{}.txt'.format(args.indir, i)
        with open(infile) as f:
            for l in f:
                lines.append(l.strip())

    random.shuffle(lines)

    total = len(lines)
    val_size = len(lines) // 10
    train_size = val_size * 8

    splits = [
        ('train.txt', lines[:train_size]),
        ('val.txt', lines[train_size:train_size + val_size]),
        ('test.txt', lines[train_size + val_size:]),
    ]

    for name, data in splits:
        with open(os.path.join(args.outdir, name), 'w', encoding='utf8') as f:
            f.write('\n'.join(data) + '\n')
