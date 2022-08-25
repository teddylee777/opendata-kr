# 오픈 데이터셋(한글) Korean Open Data

다양한 샘플 데이터셋을 제공합니다.

various sample datasets for Data Science, Machine Learning, etc.

## 설치

```bash
pip install -U opendata-kr
```

## 사용

**데이터셋 목록 조회**

```python
from opendata import dataset

# 전체 데이터셋 목록 조회
dataset.list()
```

**데이터셋 다운로드**

```python
dataset.download('유가정보')
```

