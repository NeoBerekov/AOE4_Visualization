# AOE4 Data of Ranks Visualization


This project is a visualization of the data of ranks in the game Age of Empires IV with a separate front-end and back-end architecture.

My Visualization course project.

## Data-Source

- The data is obtained from the public APIs of [aoe4world.com](https://aoe4world.com/api).
- The guy who maintains the API is super nice.

## How to Run

- Run `python3 app.py` in the main directory to start the back-end.
- Open `index.html` in the `webapp` directory to start the front-end.
- - If the Web app fails to show flags, its request may be blocked due to your browser's security policy. 
- - - You can try to open it with a Vscode extension called **Live Server**.

## Structure
### Back-End

- The back-end utilizes **Altair** for visualizing data obtained from public APIs and saves it in JSON format.
- A simple local API is set up using **Flask** to provide the front-end with the necessary data.
- The back-end can also refresh data from public APIs based on front-end requests.

### Front-End

- The front-end is a Web app written in **JavaScript**.

## Special Thanks
[@WhiskeyXD](https://github.com/SignedWhiskeyXD), who helped me a lot with the front-end. He is an angel.