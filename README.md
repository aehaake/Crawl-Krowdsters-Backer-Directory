# Web Scraper for Krowdster Backer Directory

This project consists of a Python script that automates the login process to the [Krowdster](https://app.krowdster.co/backer/directory) platform and scrapes the Backer Directory for data. It provides an educational example of how to use tools like `Selenium` and `BeautifulSoup` for website interaction and data extraction.

**Disclaimer**: This code is provided for educational purposes only. Use this script responsibly and ethically, and make sure to adhere to Krowdster's terms and conditions. Note that a paid account on the platform is required to access backer data.

## What Does The Project Do?

The script automates the process of logging in to the Krowdster platform, navigating to the Backer Directory, and scraping data about backers. The scraped data includes the number of projects backed, backer's name, location, and associated URLs. The data is then stored in an Excel file for further use.

This might be usefull if you want to directly promote your own Kickstarter campaign by reaching out to Kickstarter users.

To simulate human-like interaction with the webpage, the script also generates and performs mouse movement patterns.

## How To Run The Project?

To run this project, you need Python installed on your machine. You can download Python [here](https://www.python.org/downloads/).

### Step 1: Clone the repository

Firstly, clone this repository using git:

```
git clone https://github.com/aehaake/Krowdster-Web-Scraper.git
```

Navigate to the cloned directory:

```
cd Krowdster-Web-Scraper
```

### Step 2: Install the requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.

```bash
pip install -r requirements.txt
```

### Step 3: Run the script

Once the packages are installed, you can add your username and password and run the script:

```bash
python crawl-krowdster.py
```

## Contributions

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/aehaake/Krowdster-Web-Scraper/issues) if you want to contribute.

## License

Distributed under the MIT License. See `LICENSE` for more information.
