<h1 align="center">Analyze bike thefts in Berlin.</h1>
<p align="center">Project Description</p>
This project has the main objective to analyze bike thefts in Berlin, including the number of bikes expected to be stolen. 

## Content of the project
* 1. data directory
* 2. `utils.py`: define class `BikeThefts()`for data transformation
* 3. `app.py` (`streamlit` app)
* 4. `transform.py`: transform data for running analysis 
* 4. `requirements.txt`

## For running the models locally in designated environment
- clone repo locally
- create an environment with the contents of the requirements.txt file (if you are using conda: install pip first via "conda install pip" and then "pip install -r requirements.txt")
- run `streamlit run app.py` on your terminal

## For running the app in a docker container
- clone repo locally
- build image with
`docker build -t streamlitchurnapp:latest -f docker/Dockerfile .`
- run image with
`docker run -p 8501:8501 streamlitchurnapp:latest`
- in your web browser: map your localhost to port 8501 in container

## Author

**Carlos Pumar-Frohberg**

- [Profile](https://github.com/cpumarfrohberg)
- [Email](mailto:cpumarfrohberg@gmail.com?subject=Hi "Hi!")


## 🤝 Support

Comments, questions and/or feedback are welcome!
