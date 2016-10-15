import argparse
import re

from bs4 import BeautifulSoup


def transform(text):
    # destroy nested sentences
    text = text.replace('　', '').replace('『', '「').replace('』', '」')
    # clean comments
    text = re.sub('（.*）', '', text)
    # break sentences
    text = re.sub(r'([。！？；]|……)', '\\1\n', text)
    # clean text
    sentences = [re.sub(r'^.*：「', '', s.strip()) for s in text.split()]
    # clean more text
    sentences = [re.sub(r'^」+', '', s) for s in sentences]
    # destroy incomplete sentences
    sentences = [s for s in sentences if s and '…' not in s]

    # filter strange sentences
    cleaned_sentences = []
    for s in sentences:
        if s.startswith('「') and s.count('」') == 0:
            s = s[1:]
        if not s.count('「') == s.count('」'):
            continue
        if len(s) > 3 and len(s) < 50 and re.search('[a-zA-Z]', s) is None:
            cleaned_sentences.append(s)

    text = '\n'.join(cleaned_sentences) + '\n'
    return text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--indir', required=True)
    parser.add_argument('--outdir', required=True)
    args = parser.parse_args()

    for i in range(1, 108 + 1):
        infile = '{}/{}.html'.format(args.indir, i)
        outfile = '{}/{}.txt'.format(args.outdir, i)
        with open(infile) as f:
            with open(outfile, 'w', encoding='utf8') as out:
                soup = BeautifulSoup(f.read(), 'lxml')
                for br in soup.find_all('br'):
                    br.replace_with('\n')

                text = transform(soup('p')[0].text)

                out.write(text)
