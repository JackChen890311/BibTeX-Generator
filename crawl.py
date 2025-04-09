import argparse
from tqdm import tqdm
import difflib
from title2bib.crossref import get_bib_from_title
from contextlib import suppress

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='input.txt')
    parser.add_argument('--output', type=str, default='output.txt')
    args = parser.parse_args()

    with open(args.input, 'r', encoding='utf-8') as f:
        titles = f.read().splitlines()

    failed_cnt = 0
    result = []

    for title in tqdm(titles):
        if title.startswith("#") or not title.strip():
            result.append(title + "\n")
            continue
        if title.startswith("@") or not title.strip():
            result.append(title + "\n")
            continue

        with suppress(Exception):
            bib = get_bib_from_title(title, True)[1]
            start = bib.find("title={")
            end = bib.find("}", start)
            title_from_bib = bib[start + len("title={"):end]
            # print(f"Title from input: {title}")
            # print(f"Title from bib  : {title_from_bib}")


            similarity = difflib.SequenceMatcher(None, title.lower().strip(), title_from_bib.lower().strip()).ratio()
            if similarity > 0.9:
                result.append(bib.strip() + "\n")
            else:
                raise ValueError("Title mismatch")

            continue  # skip fail count

        failed_cnt += 1
        result.append(f"=== Failed === {title}\n")

    with open(args.output, 'w', encoding='utf-8') as f:
        f.writelines(result)

    total = len(titles)
    print(f"All: {total}  Failed: {failed_cnt}  Successful: {total - failed_cnt}")

if __name__ == '__main__':
    main()