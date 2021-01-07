-> Instructions to test program :-

Required libraries ->
	1. pip install fastapi
	2. pip install uvicorn
	3. pip install pandas
	4. pip install pymongo

Steps to test ->

1. Go to "app" directory

2. run command -> uvicorn fastapi:app

What to check ->

	1. Open "127.0.0.1:8000/docs" (SwaggerUI interface)
	
	2. API endpoints ->
		a) Insert -> inserts csv data into mongoDB
		b) Delete -> deletes csv data from mongoDB
		c) Stop ->  stops insertion/deletion process in between and returns total records affected.