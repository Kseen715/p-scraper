import source.parser as pr
from pprint import pprint
import colorama as cl
import pandas as pd
import numpy as np


def save_tags_as_csv(list, filename):
    with open(filename, 'w') as f:
        f.write('tags,\n')
        for item in list:
            f.write('\"%s\",\n' % item)
    print('Tags saved to %s' % filename)


def read_tags_as_csv(filename):
    with open(filename, 'r') as f:
        f.readline()
        list = []
        for line in f:
            list.append(line.strip().replace('\"', '').replace(',', ''))
        return list
    print('Tags read from %s' % filename)


def save_df_as_csv(df, filename):
    df.to_csv(filename, sep=',', encoding='utf-8', index=False)
    print('Dataframe saved to %s' % filename)


def read_df_as_csv(filename):
    df = pd.read_csv(filename, sep=',', encoding='utf-8')
    print('Dataframe read from %s' % filename)
    return df


def main():
    parser = pr.XhamsterParser()

    # print(parser.getAllTags())
    # save_tags_as_csv(parser.getAllTagsThreaded(), 'temp/tags.csv')
    # print(read_tags_as_csv('temp/tags.csv'))

    tags = read_tags_as_csv('temp/tags.csv')
    # tags is columns of dataframe
    # 0 rows
    df = pd.DataFrame(columns=['video_id'] + tags)

    for item in pr.test_xhamster_videos:
        # first column is video_id, other columns set to 0
        row = [item] + [0] * len(tags)
        df = df._append(pd.Series(row, index=df.columns), ignore_index=True)

    save_df_as_csv(df, 'temp/dataframe.csv')
    print(df.head())


if __name__ == '__main__':
    main()
