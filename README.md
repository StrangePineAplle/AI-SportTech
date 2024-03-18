<p align="center"><img src="https://github.com/StrangePineAplle/AI-SportTech/blob/main/media/AI-SportTech.png"></p>

## Basic Overview
A solution to the problem of cheating steps when using fitness applications\
based on machine learning algorithms, prepared for the [Мой фитнес](https://xn--e1afclhdzfq.xn--p1ai/) company.

Решение проблемы накрутки шагов при использовании фитнес приложений\
на основе алгоритмов машинного обучения, подготовленное для компании [Мой фитнес](https://xn--e1afclhdzfq.xn--p1ai/).

## About the problem
But what is the problem with increasing steps? Fitness apps these days provide the opportunity not only to track your own steps, but also to participate in various competitions. Often, organizers provide prizes for winning competitions, and employers holding competitions to improve the health of their employees provide bonuses. Therefore, people begin to use a variety of external scam methods (such as phone swings for example) that cannot be tracked systematically. Despite this, when analyzing data obtained from such accounts, it is possible to identify a pattern and prevent fraud.

Но что за проблема накрутки шагов? Фитнес приложения в наши дни предоставляют возможность не только отслеживать свои собственные шаги, но и участвовать в разнообразных соревнованиях. Часто за победу в соревнованиях организаторы предоставляют призы, а работодатели проводящие соревнования для улучшения состояния здоровья своих работников предоставляют премии. Поэтому люди начинают использовать разнообразные внешние методы жульничества (такие, как качели для телефона например) которые невозможно отследить системно. Несмотря на это при анализе данных полученных с подобных аккаунтов можно выявить закономерность и предотвратить жульничество.

## Used AI model
To solve the problem, the 'random forest' machine learning model is used, this provides high accuracy of prediction based on a combination of steps, heartbeat, training time, gender, weight and age of the user.

Для решения задачи используется модель машинного обучения 'random forest', это обеспечивает высокую точность предсказания основанную на совокупности шагов, сердцебиения, времени тренировки, пола, веса и возраста пользователя.

Model accuracy diagram. As you can see, the prediction coincides with real data by almost 99%

Диаграмма точности модели. Как можно видеть предсказание совпадает с реальными данными практически на 99%

Model metrics:

Метрики модели:

- Precision: 0.994

- Recall: 0.982

- RMSE: 0.089

- R2: 0.964
<p align="center"><img src="https://github.com/StrangePineAplle/AI-SportTech/blob/main/media/perception.png"></p>

## About the repository

Here you can familiarize yourself with the structure of this repository. For convenience, it is divided into two parts: a complete script with inputdata processing and model training, and a docker image with a pre-trained model that can be downloaded and used by you\
(can be downloaded later)

Здесь вы можете ознакомиться со структурой данного репозитория. Для удобства он поделён на две части: полный скрипт с обработкой входных данных и обучением модели и докер образ с заранее обученной моделью который может быть скачан и использован вами\
(может быть загружен позже)

## [Full model](https://github.com/StrangePineAplle/AI-SportTech/tree/main/fullModel)
The folder contains the data on which the model was trained, an example of an input file for prediction, and a folder for saving the trained model.

В папке находятся данные, на которых обучалась модель, пример входного файла для прогнозирования и папка для сохранения обученной модели.

The full model jupyter notebook file can be found [here](https://github.com/StrangePineAplle/AI-SportTech/blob/main/fullModel/AI_SportTech.ipynb)

Полный файл модели jupyter notebook можно найти [здесь](https://github.com/StrangePineAplle/AI-SportTech/blob/main/fullModel/AI_SportTech.ipynb)

The data is available for download from the link in the [readme](https://github.com/StrangePineAplle/AI-SportTech/blob/main/fullModel/data/readme.txt)  file.

Данные доступны для загрузки по ссылке в [readme](https://github.com/StrangePineAplle/AI-SportTech/blob/main/fullModel/data/readme.txt) файле

## [Trained model](https://github.com/StrangePineAplle/AI-SportTech/tree/main/trainedModel)
The folder contains a docker image which can be installed as follows:

Папка содержит докер образ который может быть установлен следующим образом: 
