[![Tests](https://github.com/gisman/ckanext-embedding/workflows/Tests/badge.svg?branch=main)](https://github.com/gisman/ckanext-embedding/actions)

# ckanext-embedding

This is a CKAN extension that allows you to create vector embeddings of your datasets. It uses the all-MiniLM-L6-v2 transformer to generate embeddings and stores them in a Solr Search index.)

이 익스텐션은 데이터셋의 벡터 임베딩 생성을 지원하는 CKAN 플러그인입니다. all-MiniLM-L6-v2 트랜스포머를 사용하여 임베딩을 생성하고, 이를 Solr 검색 인덱스에 저장합니다.

다양한 벡터 데이터베이스가 존재하지만, CKAN은 검색 엔진으로 Solr를 사용하므로 벡터 임베딩 데이터를 Solr에 저장하는 것이 적절한 통합 방식입니다. 
참고로 Solr는 버전 9.0부터 벡터 검색을 지원합니다. CKAN은 2.10부터 Solr 8과 Solr 9만 공식적으로 지원합니다

포함 컬럼은 title, tag, notes, pricing, maintainer 입니다. 이 중 pricing은 gimi9.com에서 제공하는 데이터로 extra 입니다. pricing으로 인해 에러가 발생하지 않겠지만 plugin.py를 적절히 수정하여 extra를 제거하거나 추가할 수 있습니다.

ckan.ini에서 설정할 수 있도록 개선하고 싶지만, 짧은 코드라서 그대로 두었습니다.

## Index budild

CKAN에 데이터셋이 등록되거나 수정될 때마다 자동으로 벡터 임베딩이 생성되어 Solr에 저장됩니다.

기존 데이터셋을 업데이트할 때는 ckan search-index rebuild 명령어를 사용하세요. 이 명령은 CKAN cli 명령어로, CKAN의 데이터셋 인덱스를 갱신합니다. 자세한 사용법은 공식 설명서를 참고하세요. https://docs.ckan.org/en/latest/maintaining/cli.html#search-index-search-index-commands


## Example

```json
{
  "responseHeader":{
    "status":0,
    "QTime":0,
    "params":{
      "q":"{!term f=name}ex_729",
      "indent":"true",
      "q.op":"OR",
      "useParams":"",
      "_":"1744810299220"
    }
  },
  "response":{
    "numFound":1,
    "start":0,
    "numFoundExact":true,
    "docs":[{
      "vector":[-0.065421514,0.050400585,0.10282599,-0.057955716,0.1183206,-0.06513496,0.02261043,-0.010070728,-0.0183888,-0.06734211,0.08669137,-0.0070586386,0.04243353,-0.054944314, 생략...],
      "author":"한국도로공사",
      "name":"ex_729",
      "notes":"수도권 구간 통행속도(집계일자,콘존ID,차로유형구분코드,통행속도),
      "title":"한국도로공사 - 수도권 구간 통행속도",
      "title_ngram":"한국도로공사 - 수도권 구간 통행속도",
      "url":"http://data.ex.co.kr/portal/fdwn/view?type=VDS&num=AD&requestfrom=dataset",
      "version":"2024-03-01",
      "dataset_type":"dataset",
      생략...
    }]
  }
}
```

## Requirements

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.10 and earlier | not tested    |
| 2.11             | yes    |


## Installation

1. solr managed_schema 수정.

* knn_vector 타입 추가
```xml
<fieldType name="knn_vector" class="solr.DenseVectorField" knnAlgorithm="hnsw" vectorDimension="384"/>
```

* knn_vector vector 추가
```xml
<field name="vector" type="knn_vector" multiValued="false" indexed="true" stored="true"/>
```

2. 익스텐션 설치

NOT DOCUMENTED YET!!!

3. ckan.ini 수정

plugins = embedding


NOT DOCUMENTED YET!!!

To install ckanext-embedding:

1. Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

    git clone https://github.com/gisman/ckanext-embedding.git
    cd ckanext-embedding
    pip install -e .
	pip install -r requirements.txt

3. Add `embedding` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload


## Config settings

NOT DOCUMENTED YET!!!

None at present

**TODO:** Document any optional config settings here. For example:

	# The minimum number of hours to wait before re-checking a resource
	# (optional, default: 24).
	ckanext.embedding.some_setting = some_default_value


## Developer installation

NOT DOCUMENTED YET!!!

To install ckanext-embedding for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/gisman/ckanext-embedding.git
    cd ckanext-embedding
    pip install -e .
    pip install -r dev-requirements.txt


## Tests

NOT DOCUMENTED YET!!!

To run the tests, do:

    pytest --ckan-ini=test.ini


## Releasing a new version of ckanext-embedding

NOT DOCUMENTED YET!!!

If ckanext-embedding should be available on PyPI you can follow these steps to publish a new version:

1. Update the version number in the `pyproject.toml` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.

2. Make sure you have the latest version of necessary packages:

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version:

       python -m build && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI:

       twine upload dist/*

5. Commit any outstanding changes:

       git commit -a
       git push

6. Tag the new release of the project on GitHub with the version number from
   the `setup.py` file. For example if the version number in `setup.py` is
   0.0.1 then do:

       git tag 0.0.1
       git push --tags

## License

MIT
