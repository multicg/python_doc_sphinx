# 프로젝트 설정 및 문서화

이 프로젝트는 [`Poetry`](https://python-poetry.org/ "Go to definition")와 [`Sphinx`](https://www.sphinx-doc.org/ "Go to definition")를 사용하여 Python 프로젝트를 설정하고 문서화하는 방법을 설명합니다.

## 프로젝트 설치

다음 명령어를 사용하여 프로젝트를 설치할 수 있습니다:

```sh
git clone https://github.com/multicg/python_doc_sphinx.git
cd python_doc_sphinx
poetry install
```

## Poetry 설정

[`Poetry`](https://python-poetry.org/ "Go to definition")는 Python 프로젝트의 종속성을 관리하는 도구입니다. 다음 명령어를 사용하여 [`Poetry`](https://python-poetry.org/ "Go to definition")를 설치할 수 있습니다:

```sh
pip install poetry
```

프로젝트 디렉토리에서 다음 명령어를 실행하여 Poetry 환경을 설정합니다:

```sh
poetry config virtualenvs.in-project true
```

## Sphinx 설정

[`Sphinx`](https://www.sphinx-doc.org/ "Go to definition")는 Python 문서화를 위한 강력한 도구입니다. 다음 명령어를 사용하여 [`Sphinx`](https://www.sphinx-doc.org/ "Go to definition")를 설치할 수 있습니다:

```sh
poetry run sphinx-quickstart
```

## 문서 빌드

[`Sphinx`](https://www.sphinx-doc.org/ "Go to definition") 문서를 HTML로 빌드하려면 다음 명령어를 실행합니다:

```sh
.\make.bat html
```

이 명령어는 build/html 디렉토리에 HTML 파일을 생성합니다.

## FastAPI 설정

[`FastAPI`](https://fastapi.tiangolo.com/ko/ "Go to definition")를 사용하여 웹 애플리케이션을 설정하려면 다음 명령어를 실행합니다

```sh
poetry add fastapi uvicorn
```

[`FastAPI`](https://fastapi.tiangolo.com/ko/ "Go to definition") 애플리케이션을 실행하려면 다음 명령어를 실행합니다:

```sh
poetry run uvicorn main:app --reload
```

이 명령어는 로컬 서버를 시작하고 코드 변경 시 자동으로 다시 로드합니다.

# 프로젝트 구조

프로젝트의 기본 디렉토리 구조는 다음과 같습니다:

```sh
python_doc_sphinx/
├── main.py
├── README.md
├── pyproject.toml
├── poetry.lock
├── make.bat
├── source/
│   ├── conf.py
│   ├── index.rst
│   └── ...
└── build/
    └── html/
        └── ...
```
