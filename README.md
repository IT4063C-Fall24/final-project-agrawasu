# The Rise of EVs and their Impact on the Environment
<!-- Edit the title above with your project title -->

## Project Overview

### Topic:
The rapid increase in electric vehicles (EV) available on the road has offered a very promising solution to global warming efforts around the world. However, understanding the impact of EVs on the environment starts with the full lifecycle starting from the manufacturing to usage on the road and inevitably disposal. This topic is important because it seems that people ar shifting over to EVs for everyday commuting due to the financial benefits and reliefs that may come in the form of gas and maintenance. This paired with the rising concern in the environment and global warming brings it fairly high on the relevance charts.

### Project Questions and Potential Answer Formats:

#### What is the current state of EV adoption around the world, and which geographic regions are experiencing the most significant growth?
> Including visuals, such as a bar graph or a heat map, can show sales and growth trends in different regions.

#### How do greenhouse gas emissions through the lifespan of an EV compare to the traditional gas-powered combustion engine?
> Use a bar chart or pie chart to compare the different stages of the lifespan of the vehicles.

#### How does the availability of EV charging stations influence the amount of EVs on the road there?
> A heat map to show EV stations as well as number of EVs on the road would work great here.

### Data Sources:
#### Source: International Energy Agency (IEA)
> **Data type:** Downloadable data reports (file)

> **Description:** Shows annual reports on EVs in general, such as adoption, stock, charging, and emissions impact on the environment.

> **Relation:** This can be paired with the other sources as they have similar data points. I can merge common/supporting columns after I analyze and clean the data.

**Link:** https://www.iea.org/data-and-statistics/data-tools/global-ev-data-explorer

#### Source: Our World in Data
> **Data type:** Downloadable data reports and API (file and API)

> **Description:** Shows global EV adoption, environmental impacts, and charging infrastruction

> **Relation:** Pairing this with the IEA data source will allow me to combine similar points and compare globally.

**Link:** https://ourworldindata.org/electric-car-sales

#### Source: Open Charge Map
> **Data type:** API access (API)

> **Description:** API containing location data for EV charge infrastructure.

> **Relation:** This can be paired with the other two sources quite well, as this would give a good visual representation. This goes for each of the previous sources as well, but the data sources will be paired with research involving information that can not be easily shown as data to make conclusions.

**Link:** https://openchargemap.org/site/develop/api#/

## Self Assessment and Reflection

<!-- Edit the following section with your self assessment and reflection -->

### Self Assessment
<!-- Replace the (...) with your score -->

| Category          | Score    |
| ----------------- | -------- |
| **Setup**         | ... / 10 |
| **Execution**     | ... / 20 |
| **Documentation** | ... / 10 |
| **Presentation**  | ... / 30 |
| **Total**         | ... / 70 |

### Reflection
<!-- Edit the following section with your reflection -->

#### What went well?
#### What did not go well?
#### What did you learn?
#### What would you do differently next time?

---

## Getting Started
### Installing Dependencies

To ensure that you have all the dependencies installed, and that we can have a reproducible environment, we will be using `pipenv` to manage our dependencies. `pipenv` is a tool that allows us to create a virtual environment for our project, and install all the dependencies we need for our project. This ensures that we can have a reproducible environment, and that we can all run the same code.

```bash
pipenv install
```

This sets up a virtual environment for our project, and installs the following dependencies:

- `ipykernel`
- `jupyter`
- `notebook`
- `black`
  Throughout your analysis and development, you will need to install additional packages. You can can install any package you need using `pipenv install <package-name>`. For example, if you need to install `numpy`, you can do so by running:

```bash
pipenv install numpy
```

This will update update the `Pipfile` and `Pipfile.lock` files, and install the package in your virtual environment.

## Helpful Resources:
* [Markdown Syntax Cheatsheet](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
* [Dataset options](https://it4063c.github.io/guides/datasets)
