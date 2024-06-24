# AUCTION-HOUSE

Inspired by [History TV18's show "Baggage Battles"](https://www.historyindia.com/show/baggage-battles)

## How it works?

-   **Register** yourself if you are new here.(use good username).
-   **Login** to your account if not already logged in.
-   Select the item which you liked and **bid** on it.
-   Make sure that your bid is **high enough**.
-   You can comment in **comment section** of the particular item.
-   After owner close the Auction the user with **_highest bid_** will win.
-   **Winner** will able to see message in the listing of that item.
-   Have **fun** bidding!😃🤟

#### <a href="https://auction2.up.railway.app/">Open the auction and Let the battle begin.</a>

---

# How to set up on local machine

## Pre-setup

Create a new folder anywhere on your system
open terminal in this new folder.

## Setup

1. The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/chetan6780/Auctions.git
$ cd Auctions
```

2. Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ .\env\Scripts\activate
```

    for linux

```sh
$ source env/bin/activate
```

3. install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

_Note: `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.
For pipenv you will not see any `(env)` in front of the propt._

4. Once `pip` has finished downloading the dependencies:

```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```

The application should be running on `http://127.0.0.1:8000/`

## Preview

![1](https://poly-screenshots.wellfound.com/Project/0d/1367298/f8c5f8d598fd769d4840b3a51081cda0-original.png)
![2](https://poly-screenshots.wellfound.com/Project/0d/1367298/5b9ef5d4d5cb1561b59c85152b78cc47-original.png)
![3](https://poly-screenshots.wellfound.com/Project/0d/1367298/650db39d04e20573760a8c4886edcefd-original.png)
![4](https://poly-screenshots.wellfound.com/Project/0d/1367298/0518eb8db85378d25ceae16c3e602f6d-original.png)
![5](https://poly-screenshots.wellfound.com/Project/0d/1367298/7c953349bec7dea06bdd072bd8152798-original.png)
![6](https://poly-screenshots.wellfound.com/Project/0d/1367298/5a45f408965e848cbaceab5c8c88d98e-original.png)
![7](https://poly-screenshots.wellfound.com/Project/0d/1367298/d4636ae87cd535f79e7f8900ac4e4aa0-original.png)
![8](https://poly-screenshots.wellfound.com/Project/0d/1367298/5611fc7ad60f2b6e99e462ab458ed7da-original.png)
![9](https://poly-screenshots.wellfound.com/Project/0d/1367298/8f89da67e5ed65b75a265035cde1eca6-original.png)
