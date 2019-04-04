# "Robo Advisor" Project

A solution for the ["Robo Advisor" project](https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/projects/robo-advisor.md).

Issues requests to the [AlphaVantage Stock Market API](https://www.alphavantage.co/) in order to provide automated stock or cryptocurrency trading recommendations.

[![Build Status](https://travis-ci.com/s2t2/robo-advisor-screencast.svg?branch=v3-testing)](https://travis-ci.com/s2t2/robo-advisor-screencast)

## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

## Installation

Clone or download [this repository](https://github.com/s2t2/robo-advisor-screencast) onto your computer. Then navigate there from the command line:

```sh
cd robo-advisor-screencast
```

Use Anaconda to create and activate a new virtual environment, perhaps called "stocks-env". From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Setup

Before using or developing this application, take a moment to [obtain an AlphaVantage API Key](https://www.alphavantage.co/support/#api-key) (e.g. "abc123").

After obtaining an API Key, create a new file in this repository called ".env", and update the contents of the ".env" file to specify your real API Key:

    ALPHAVANTAGE_API_KEY="abc123"

## Usage

Run the recommendation script:

```py
python app/robo_advisor.py
```

## Tests

Install pytest package (first time only):

```sh
pip install pytest
```

Run tests:

```sh
pytest
```

## [License](/LICENSE.md)
