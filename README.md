# Course Calendar Python

Get started with reading the UBC Course Calendar CSV data using Python 3.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for use with UBC course calendar data available from the [Learning Analytics Project](https://learninganalytics.ubc.ca/for-students/hackathons/) site.

### Prerequisites

1. **Install [Python 3](https://www.python.org)**.
2. **Install [Git](https://git-scm.com/downloads)**.

### Installation

1. Clone this repo. `git clone https://github.com/ubccapico/course-calendar-python.git`
1. Then cd into the repo. `cd course-calendar-python`
1. Copy/paste the `ubc_course_calendar_data.csv` file you downloaded to the `course-calendar-python` folder.
1. Create a python [virtual environment](https://docs.python.org/3/library/venv.html) `python3 -m venv .venv` (if you get the following error on Mac `xcrun: error: invalid active developer path`, try installing the x-code dev tools `xcode-select --install`).
1. Activate the virtual environment `source .venv/bin/activate`
1. Install project dependencies `pip install -r requirements.txt`
1. Run `python hack_courses.py` to read the CSV and print some information about the dataset.

## Author

* **Craig Thompson**
craig.thompson@ubc.ca

## License

This project is licensed under the GNU General Public License v3.0.
