# :rocket: Millennium Falcon Challenge @ [Dataiku](https://www.dataiku.com/)

> :book: [Project's Specification](https://github.com/dataiku/millenium-falcon-challenge)

## :floppy_disk: Database Creation & Population

The following command creates and populates the `universe.db` database based on `universe.sql`:

```bash
cat universe.sql | sqlite3 universe.db
```

_**Note:** this command doesn't need to be run if you do not modify `universe.sql`, since the database is already initialized in this repo._

The `ROUTES` table of `universe.db` contains the following data:

|  origin  | destination | travel_time |
| :------: | :---------: | :---------: |
| Tatooine |   Dagobah   |      6      |
| Dagobah  |    Endor    |      4      |
| Dagobah  |    Hoth     |      1      |
|   Hoth   |    Endor    |      1      |
| Tatooine |    Hoth     |      6      |

---

## :gear: Backend

### :bookmark_tabs: Dependencies

- [Python 3](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/index.html)
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)

Install all the dependencies locally with:

```bash
pip3 install -r requirements.txt
```

### :gear: Launching the backend

Launch the backend with:

```bash
python3 app.py
```

And navigate to http://localhost:5000/ to explore the [Swagger](https://swagger.io/) documentation of the backend RESTful API.

---

## :round_pushpin: Frontend

---

## CLI

First, add the following lines to your RUNCOM (`.bashrc`, `.zshrc`, etc. depending on your shell) file:

```shell
export MFC_PATH=~/<path_to_this_folder>
source $MFC_PATH/cli/give-me-the-odds.sh
```

Then, you will be able to use the `give-me-the-odds` command:

`give-me-the-odds give-me-the-odds <millennium-falcon.json> <empire.json>` will return the probability of success of the mission as a number ranging from 0 to 100.

It takes 2 file paths as input - respectively the paths toward the `millennium-falcon.json` and `empire.json` files.
