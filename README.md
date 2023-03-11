<h1 align="center">Analyze bike thefts in Berlin.</h1>
<p align="center">Project Description</p>
This project has the main objective to analyze bike thefts in Berlin, including the number of bikes expected to be stolen. 

* Main conclusions include:
- from `EDA` 
    - data; distributions, missing vals, outliers
    - correlations identified
    - useful, additional data to have
- from modeling

## Content of the project
* 1. data directory
* 2. EDA (including feature importance)
* 3. model fit 
* 4. artifacts folder containing pickled model
* 5. `utils.py`
* 6. `streamlit` app

## For running the models locally in designated environment
- clone repo locally
- create an environment with the contents of the requirements.txt file (if you are using conda: install pip first via "conda install pip" and then "pip install -r requirements.txt")

## For running the app in a docker container
- clone repo locally
- build image with
`docker build -t berlinbikethefts:latest -f docker/Dockerfile .`
- run image with
`docker run -p 8501:8501 berlinbikethefts:latest`
- in your web browser: map your localhost to port 8501 in container


## Future Updates
- [ ] Feature engineer for retraining `Logistic Regression`


## Author

**Carlos Pumar-Frohberg**

- [Profile](https://github.com/cpumarfrohberg)
- [Email](mailto:cpumarfrohberg@gmail.com?subject=Hi "Hi!")


## 🤝 Support

Comments, questions and/or feedback are welcome!
