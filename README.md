<p align="center"><img src="https://github.com/StrangePineAplle/AI-SportTech/blob/main/media/AI-SportTech.png"></p>

## Basic Overview
A solution to the problem of cheating steps when using fitness applications\
based on machine learning algorithms, prepared for the [Мой фитнес](https://xn--e1afclhdzfq.xn--p1ai/) company.

Решение проблемы накрутки шагов при использовании фитнес приложений\
на основе алгоритмов машинного обучения, подготовленное для компании [Мой фитнес](https://xn--e1afclhdzfq.xn--p1ai/).

## Used AI model
To solve the problem, the 'random forest' machine learning model is used, this provides high accuracy of prediction based on a combination of steps, heartbeat, training time, gender, weight and age of the user.

Для решения задачи используется модель машинного обучения 'random forest', это обеспечивает высокую точность предсказания основанную на совокупности шагов, сердцебиения, времени тренировки, пола, веса и возраста пользователя.

## About the repository

Here you can familiarize yourself with the structure of this repository. For convenience, it is divided into two parts: a complete script with inputdata processing and model training, and a docker image with a pre-trained model that can be downloaded and used by you\
(can be downloaded later)

Здесь вы можете ознакомиться со структурой данного репозитория. Для удобства он поделён на две части: полный скрипт с обработкой входных данных и обучением модели и докер образ с заранее обученной моделью который может быть скачан и использован вами\
(может быть загружен позже)

## [Full model](https://github.com/StrangePineAplle/AI-SportTech/tree/main/fullModel)
The folder contains the data on which the model was trained, an example of an input file for prediction, and a folder for saving the trained model.
В папке находятся данные, на которых обучалась модель, пример входного файла для прогнозирования и папка для сохранения обученной модели.

## [Trained model](https://github.com/StrangePineAplle/AI-SportTech/tree/main/trainedModel)
The folder contains a docker image which can be installed as follows:
Папка содержит докер образ который может быть установлен следующим образом: 
