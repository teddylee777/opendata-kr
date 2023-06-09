from tqdm.notebook import tqdm
import pandas as pd
import requests
import os
import zipfile


class Dataset():
    def __init__(self, name, desc, _id, data_dir='data', alt_url=True):
        self.name = name
        self.desc = desc
        self.data_dir = data_dir
        self.id = _id
        self.alt_url = alt_url
        
        # Dropbox Dataset
        self.dataset_url = 'https://www.dropbox.com/s/dmk6sti3m254w6o/dataset.csv?dl=1'
        if alt_url:
            # Jaen Dataset
            self.dataset_url = 'http://data.jaen.kr/download?download_path=%2Fdata%2Ffiles%2FmySUNI%2Fdatasets%2F000-metadata%2Fdataset.csv'

        # data 폴더 생성
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        self.load_metadata()

    def load_metadata(self):
        metadata_url = 'https://www.dropbox.com/s/gjeoilz9bm8lzgg/metadata.csv?dl=1'
        cols = ['filename', 'url']
        if self.alt_url:
            metadata_url = 'http://data.jaen.kr/download?download_path=%2Fdata%2Ffiles%2FmySUNI%2Fdatasets%2F000-metadata%2Fmetadata.csv'
            cols = ['filename', 'alt_url']
            
        metadata = pd.read_csv(metadata_url)
        self.meta = {i: v for i, v in metadata.loc[metadata['id'] == self.id, cols].values}

    def download(self, path=None):
        print('======= 다운로드 시작 =======\n')
        if path is None:
            dir_name = os.path.join(self.data_dir, self.name)
        else:
            dir_name = path
            
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)
            
        for idx, (filename, url) in enumerate(self.meta.items()):
            r = requests.get(url, stream=True)
            filepath = os.path.join(dir_name, filename)

            ## 다운로드 progress bar 추가 ##
            total_size_in_bytes = int(r.headers.get('content-length', 0))
            block_size = 1024

            print(f'{filepath}')

            progress_bar = tqdm(total=total_size_in_bytes, unit='B', unit_scale=True)

            with open(filepath, 'wb') as file:
                for data in r.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)

            progress_bar.close()

            if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
                print("ERROR: 다운로드 도중 에러가 발생하였습니다.")
            else:
                if filepath.endswith('.zip'):
                    print(f'압축 해제 및 프로젝트 파일 구성중...')
                    zipfile.ZipFile(filepath).extractall(dir_name)
                    if os.path.isfile(filepath):
                        os.remove(filepath)

        print('\n======= 다운로드 완료 =======')


def list(alt_url=True):
    download_url = 'https://www.dropbox.com/s/95wzfrmoc4qrfvw/dataset.csv?dl=1'
    if alt_url:
        download_url = 'http://data.jaen.kr/download?download_path=%2Fdata%2Ffiles%2FmySUNI%2Fdatasets%2F000-metadata%2Fdataset.csv'
    print(download_url)
    ret = pd.read_csv(download_url).iloc[:, :-1]
    ret.columns = ['데이터셋', '설명']
    return ret


def download(name, data_dir='data', alt_url=True, path=None):
    download_url = 'https://www.dropbox.com/s/95wzfrmoc4qrfvw/dataset.csv?dl=1'
    if alt_url:
        download_url = 'http://data.jaen.kr/download?download_path=%2Fdata%2Ffiles%2FmySUNI%2Fdatasets%2F000-metadata%2Fdataset.csv'
        print('[서버] Jaen')
    else:
        print('[서버] Dropbox')
    
    ds = pd.read_csv(download_url)
    row = ds.loc[ds['data'] == name]
    if len(row) > 0:
        dataset = Dataset(row['data'].values[0], row['data_desc'], row['id'].iloc[0], data_dir=data_dir)
        dataset.download(path=path)