import argparse
from tqdm import tqdm
from title2bib.crossref import get_bib_from_title

def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='input.txt')
    parser.add_argument('--output', type=str, default='output.txt')
    args = parser.parse_args()
    return args

def main():
    args = parse_arg()
    file = args.input
    with open(file, 'r') as f:
        titles = f.read()
    titles = titles.split('\n')

    failed_cnt = 0
    result = []

    for title in tqdm(titles):
        try:
            bib = get_bib_from_title(title, True)
            result.append(bib[1])
        except:
            failed_cnt += 1
            result.append("=== Failed === " + title + "\n")

    with open(args.output, 'w+', encoding='utf-8') as f:
        f.write(''.join(result))
    
    print("All: ", len(titles), " Failed: ", failed_cnt, " Successful: ", len(result))
    
if __name__ == '__main__':
    main()