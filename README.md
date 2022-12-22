```bash
conda create -n gan python=3.10
conda activate gan
```

```bash
pip install -r requirements.txt
pip install -r dev-requirements.txt
```

```bash
uvicorn tiger:app --port 5000 --reload
```


```bash
uvicorn app:app --reload
```

