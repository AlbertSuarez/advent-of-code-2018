# Advent of code

🎁 Small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. You don't need a computer science background to participate - just a little programming knowledge and some problem solving skills will get you pretty far. Nor do you need a fancy computer; every problem has a solution that completes in at most 15 seconds on ten-year-old hardware.

## Requirements

- Python 3.6+

## Recommendations

Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

## Usage

To run the server, please execute the following from the root directory:

1. Setup virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

2. Install dependencies

```bash
pip3 install -r requirements.txt
```

3. Run any problem solver
    
```bash
python3 -m src.day_[DAY_NUMBER]
```

## Notes

All input data is kept in the `data` folder and all the problem solvers are saved in `src`.

## License

MIT © Albert Suarez