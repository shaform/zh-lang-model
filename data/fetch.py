import argparse
import time

import requests

url_format = 'http://open-lit.com/showlit.php?gbid=140&cid={cid}&bid=6367&start=0&search1=&search2='

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--outdir', required=True)
    args = parser.parse_args()

    for i in range(1, 108 + 1):
        print('download {}'.format(i))
        url = url_format.format(cid=i)
        response = requests.get(url)
        with open('{}/{}.html'.format(args.outdir, i),
                  'w',
                  encoding='utf8') as f:
            f.write(response.content.decode('big5', 'ignore'))
        time.sleep(0.1)
