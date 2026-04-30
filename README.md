## LAB-01: First Image and First Container

This scenario shows how to build an image from Dockerfile, how to run a docker container from this image.

### Steps

- Create a directory (“example”) on your Desktop.
- Create a file (“index.py”) in the “example” directory (copy from below) (this is a simple Flask that returns “Hello World” on the browser).

```
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
```

- Create “Dockerfile” (there is no extension) in the “example” directory (Copy from below) (it copies to /app directory in the container, run requirements.txt, expose 5000 port and run python app).

```
FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./index.py
```

- Create “requirements.txt” and copy it below (it only includes “flask”).

```
flask
```

- Now, we have 3 files in the “example” directory.

 ![image](https://user-images.githubusercontent.com/10358317/113274100-99299900-92dd-11eb-9431-a1839dd0b280.png)



- Run on the terminal which is open in “example” directory, “docker build --tag my-python-app .” (creating an image from Docker file and the image name is “my-python-app”, it runs in order, first download python image which is run on Alpine, finally it is prepared to run “CMD python ./index.py” while running container).

```
docker build --tag my-python-app .
```

![image](https://user-images.githubusercontent.com/10358317/113274060-8c0caa00-92dd-11eb-8ac3-285d1552c54d.png)


- Run on terminal “docker run --name python-app -p 5000:5000 my-python-app” (run container from created image “my-python-app”, container name is “python-app”, host port 5000 binds to container port 5000).

```
docker run --name python-app -p 5000:5000 my-python-app
```

![image](https://user-images.githubusercontent.com/10358317/113274079-92028b00-92dd-11eb-9902-da00b07602bb.png)


- Open Browser (http://127.0.0.1:5000) to see the result. You created the first Docker image and run the first container. Congratulations! 😊 

 ![image](https://user-images.githubusercontent.com/10358317/113274597-2967de00-92de-11eb-8a76-1b1adde27f3a.png)

 
