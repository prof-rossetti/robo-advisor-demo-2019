# "Robo Advisor" Project - Demo

A demo version of the "Robo Advisor" project, for student reference.

Issues requests to the [AlphaVantage Stock Market API](https://www.alphavantage.co/) in order to provide automated stock or cryptocurrency trading recommendations.

## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

## Installation

Fork this repository under your own control, then clone or download the resulting repository onto your computer. Then navigate there from the command line:

```sh
cd robo-advisor-demo-2019
```

> NOTE: subsequent usage and testing commands assume you are running them from the repository's root directory.

Use Anaconda to create and activate a new virtual environment, perhaps called "stocks-env". 

```sh
conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install requests
```

## Setup

Before using or developing this application, take a moment to [obtain an AlphaVantage API Key](https://www.alphavantage.co/support/#api-key) (e.g. "abc123").

After obtaining an API Key, copy the ".env.example" file to a new file called ".env", and update the contents of the ".env" file to specify your real API Key:

    ALPHA_VANTAGE_API_KEY="abc123"

Don't worry, the ".env" has already been [ignored](/.gitignore) from version control for you!

## Usage

Run the recommendation script:

```py
python app/robo_advisor.py
```

## Testing

Install pytest (first time only):

```sh
pip install pytest
```

Run tests:

```sh
pytest --disable-pytest-warnings
```

## [License](/LICENSE.md)
