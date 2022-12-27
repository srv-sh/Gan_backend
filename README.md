
Create new conda environment
```bash
conda create -n gan python=3.9.0
conda activate gan
```

Install Dependencies
```bash
pip install -r requirements.txt
pip install -r dev-requirements.txt
```

Run the servers
```bash
python web-server.py  
```


## Send the request in postman as 

Emit at `prompt`
```python
{"user_id" : "rukaiya",
 "prompt" : "red hat"
}
```

And listen at `generated_img` 