<p align="center"><img src="https://github.com/StrangePineAplle/AI-SportTech/blob/main/media/AI-SportTech.png"></p>

&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![language](https://img.shields.io/badge/RU%2FENG-red)
## Basic Overview
A solution to the problem of cheating steps when using fitness applications\
based on machine learning algorithms, prepared for the [Мой фитнес](https://xn--e1afclhdzfq.xn--p1ai/) company.

---

Решение проблемы накрутки шагов при использовании фитнес приложений\
на основе алгоритмов машинного обучения, подготовленное для компании [Мой фитнес](https://xn--e1afclhdzfq.xn--p1ai/).

## About the problem
But what is the problem with increasing steps? Fitness apps these days provide the opportunity not only to track your own steps, but also to participate in various competitions. Often, organizers provide prizes for winning competitions, and employers holding competitions to improve the health of their employees provide bonuses. Therefore, people begin to use a variety of external scam methods (such as phone swings for example) that cannot be tracked systematically. Despite this, when analyzing data obtained from such accounts, it is possible to identify a pattern and prevent fraud.

---

Но что за проблема накрутки шагов? Фитнес приложения в наши дни предоставляют возможность не только отслеживать свои собственные шаги, но и участвовать в разнообразных соревнованиях. Часто за победу в соревнованиях организаторы предоставляют призы, а работодатели проводящие соревнования для улучшения состояния здоровья своих работников предоставляют премии. Поэтому люди начинают использовать разнообразные внешние методы жульничества (такие, как качели для телефона например) которые невозможно отследить системно. Несмотря на это при анализе данных полученных с подобных аккаунтов можно выявить закономерность и предотвратить жульничество.

## [Data](https://www.kaggle.com/datasets/isotech/fitness-app-data-from-myfitnes) structure

The following data is required for the neural network to work: 'meters','hr_delta','birth_date','sex','weight'

meters: meters or steps walked

hr_delta: difference between heart rate at rest and during exercise (beats/minute)

birth_date: date of birth (in unix time)

sex: gender (0 - female, 1 - male)

weight: weight (kg)

---

Для работы нейросети требуются следующие данные: 'meters','hr_delta','birth_date','sex','weight'

meters: пройденные метры или шаги 

hr_delta: разница между сердцебиением в покое и при нагрузке (ударов/минута)

birth_date: дата рождения (в unix времени)

sex: пол (0 - женщина, 1 - мужчина)

weight: вес (кг)

## PCA
A factor analysis of the dataset was carried out using the principal component method, due to which the number of parameters for training was reduced and the accuracy of the model was increased.

---

Был проведен факторный анализ датасета методом главных компонент, за счет чего было уменьшено количество параметров обучения и увеличена точность модели.

## Used AI model
To solve the problem, the 'random forest' machine learning model is used, this provides high accuracy of prediction based on a combination of steps, heartbeat, training time, gender, weight and age of the user.
Model accuracy diagram. As you can see, the prediction coincides with real data by almost 99%

---

Для решения задачи используется модель машинного обучения 'random forest', это обеспечивает высокую точность предсказания основанную на совокупности шагов, сердцебиения, времени тренировки, пола, веса и возраста пользователя.
Диаграмма точности модели. Как можно видеть предсказание совпадает с реальными данными практически на 99%

### Model metrics:

- Precision: 0.994

- Recall: 0.982

- RMSE: 0.089

- R2: 0.964
<p align="center"><img src="https://github.com/StrangePineAplle/AI-SportTech/blob/main/media/perception.png"></p>

## About the repository

Here you can familiarize yourself with the structure of this repository. For convenience, it is divided into two parts: a complete script with inputdata processing and model training, and a docker image with a pre-trained model that can be downloaded and used by you

---

Здесь вы можете ознакомиться со структурой данного репозитория. Для удобства он поделён на две части: полный скрипт с обработкой входных данных и обучением модели и докер образ с заранее обученной моделью который может быть скачан и использован вами

## [Full model](https://github.com/StrangePineAplle/AI-SportTech/tree/main/fullModel)
The folder contains the data on which the model was trained, an example of an input file for prediction, and a folder for saving the trained model.

The full model jupyter notebook file can be found [here](https://github.com/StrangePineAplle/AI-SportTech/blob/main/fullModel/AI_SportTech.ipynb)

The data is available for download from the link in the [readme](https://github.com/StrangePineAplle/AI-SportTech/tree/main/fullModel/data)  file.

Attention. The model references data in the folder named [data](https://github.com/StrangePineAplle/AI-SportTech/tree/main/fullModel/data). Do NOT change the folder name. The data is divided into 4 datasets: cheaters, honest ones, user profiles and test datasets consisting of a single user session. Please keep the original file names or you will have to adapt the data preprocessing.

---

В папке находятся данные, на которых обучалась модель, пример входного файла для прогнозирования и папка для сохранения обученной модели.

Полный файл модели jupyter notebook можно найти [здесь](https://github.com/StrangePineAplle/AI-SportTech/blob/main/fullModel/AI_SportTech.ipynb)

Данные доступны для загрузки по ссылке в [readme](https://github.com/StrangePineAplle/AI-SportTech/tree/main/fullModel/data) файле

Внимание. Модель ссылается на данные в папке [data](https://github.com/StrangePineAplle/AI-SportTech/tree/main/fullModel/data) НЕ меняйте название папки. Данные разбиты на 4 датасета: читеры, честные, профили пользователей и тестовые состоящии из сессии одного пользователя. Пожалуйста, сохраняйте оригинальные наименования файлов или вам придётся адаптировать предобработку данных.

## [Trained model](https://github.com/StrangePineAplle/AI-SportTech/tree/main/trainedModel)

The folder contains a docker image that can be downloaded or built as follows:

Папка содержит докер образ который может быть скачан или собран следующим образом: 

### Build the image

all operations are performed in the directory [ml_model](https://github.com/StrangePineAplle/AI-SportTech/tree/main/trainedModel/ml_model)

Все операции выполняются в директории [ml_model](https://github.com/StrangePineAplle/AI-SportTech/tree/main/trainedModel/ml_model)

```bash
docker build -t ml_model .
```

### or

### [Download Docker image](https://hub.docker.com/repository/docker/fpineaplle/ai-sporttech/general)

---

### Running the image

local:

```bash
docker run --rm --mount type=bind,source="$(pwd)/input-sample.json",target=/input.json ml_model
```

web:

```bash
docker run --rm --mount type=bind,source="$(pwd)/input-sample.json",target=/input.json fpineaplle/ai-sporttech:ml_model
```

Where 'input-sample.json' is your data 

---

Где 'input-sample.json' — ваши данные
