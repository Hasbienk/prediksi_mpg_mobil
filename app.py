{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns"
      ],
      "metadata": {
        "id": "AKJ0GkEEo1ZS"
      },
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv('auto-mpg.csv')\n",
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "kxJQLl7EpEme",
        "outputId": "79504cff-da62-44b6-d67e-0a338dd61d47"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "    mpg  cylinders  displacement horsepower  weight  acceleration  model year  \\\n",
              "0  18.0          8         307.0        130    3504          12.0          70   \n",
              "1  15.0          8         350.0        165    3693          11.5          70   \n",
              "2  18.0          8         318.0        150    3436          11.0          70   \n",
              "3  16.0          8         304.0        150    3433          12.0          70   \n",
              "4  17.0          8         302.0        140    3449          10.5          70   \n",
              "\n",
              "   origin                   car name  \n",
              "0       1  chevrolet chevelle malibu  \n",
              "1       1          buick skylark 320  \n",
              "2       1         plymouth satellite  \n",
              "3       1              amc rebel sst  \n",
              "4       1                ford torino  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-3a2fee18-b85f-4307-beeb-bc554c50814c\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>mpg</th>\n",
              "      <th>cylinders</th>\n",
              "      <th>displacement</th>\n",
              "      <th>horsepower</th>\n",
              "      <th>weight</th>\n",
              "      <th>acceleration</th>\n",
              "      <th>model year</th>\n",
              "      <th>origin</th>\n",
              "      <th>car name</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>18.0</td>\n",
              "      <td>8</td>\n",
              "      <td>307.0</td>\n",
              "      <td>130</td>\n",
              "      <td>3504</td>\n",
              "      <td>12.0</td>\n",
              "      <td>70</td>\n",
              "      <td>1</td>\n",
              "      <td>chevrolet chevelle malibu</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>15.0</td>\n",
              "      <td>8</td>\n",
              "      <td>350.0</td>\n",
              "      <td>165</td>\n",
              "      <td>3693</td>\n",
              "      <td>11.5</td>\n",
              "      <td>70</td>\n",
              "      <td>1</td>\n",
              "      <td>buick skylark 320</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>18.0</td>\n",
              "      <td>8</td>\n",
              "      <td>318.0</td>\n",
              "      <td>150</td>\n",
              "      <td>3436</td>\n",
              "      <td>11.0</td>\n",
              "      <td>70</td>\n",
              "      <td>1</td>\n",
              "      <td>plymouth satellite</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>16.0</td>\n",
              "      <td>8</td>\n",
              "      <td>304.0</td>\n",
              "      <td>150</td>\n",
              "      <td>3433</td>\n",
              "      <td>12.0</td>\n",
              "      <td>70</td>\n",
              "      <td>1</td>\n",
              "      <td>amc rebel sst</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>17.0</td>\n",
              "      <td>8</td>\n",
              "      <td>302.0</td>\n",
              "      <td>140</td>\n",
              "      <td>3449</td>\n",
              "      <td>10.5</td>\n",
              "      <td>70</td>\n",
              "      <td>1</td>\n",
              "      <td>ford torino</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-3a2fee18-b85f-4307-beeb-bc554c50814c')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-3a2fee18-b85f-4307-beeb-bc554c50814c button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-3a2fee18-b85f-4307-beeb-bc554c50814c');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 398,\n  \"fields\": [\n    {\n      \"column\": \"mpg\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 7.815984312565782,\n        \"min\": 9.0,\n        \"max\": 46.6,\n        \"num_unique_values\": 129,\n        \"samples\": [\n          17.7,\n          30.5,\n          30.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"cylinders\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 3,\n        \"max\": 8,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          4,\n          5,\n          6\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"displacement\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 104.26983817119581,\n        \"min\": 68.0,\n        \"max\": 455.0,\n        \"num_unique_values\": 82,\n        \"samples\": [\n          122.0,\n          307.0,\n          360.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"horsepower\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 94,\n        \"samples\": [\n          \"112\",\n          \"?\",\n          \"78\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"weight\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 846,\n        \"min\": 1613,\n        \"max\": 5140,\n        \"num_unique_values\": 351,\n        \"samples\": [\n          3730,\n          1995,\n          2215\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"acceleration\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2.7576889298126757,\n        \"min\": 8.0,\n        \"max\": 24.8,\n        \"num_unique_values\": 95,\n        \"samples\": [\n          14.7,\n          18.0,\n          14.3\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"model year\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 3,\n        \"min\": 70,\n        \"max\": 82,\n        \"num_unique_values\": 13,\n        \"samples\": [\n          81,\n          79,\n          70\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"origin\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 1,\n        \"max\": 3,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          1,\n          3,\n          2\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"car name\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 305,\n        \"samples\": [\n          \"mazda rx-4\",\n          \"ford f108\",\n          \"buick century luxus (sw)\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()\n",
        "\n",
        "df.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 592
        },
        "id": "nesnaNG9pMN-",
        "outputId": "a8f7262a-edf7-46ca-b14e-1a73b867081c"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 398 entries, 0 to 397\n",
            "Data columns (total 9 columns):\n",
            " #   Column        Non-Null Count  Dtype  \n",
            "---  ------        --------------  -----  \n",
            " 0   mpg           398 non-null    float64\n",
            " 1   cylinders     398 non-null    int64  \n",
            " 2   displacement  398 non-null    float64\n",
            " 3   horsepower    398 non-null    object \n",
            " 4   weight        398 non-null    int64  \n",
            " 5   acceleration  398 non-null    float64\n",
            " 6   model year    398 non-null    int64  \n",
            " 7   origin        398 non-null    int64  \n",
            " 8   car name      398 non-null    object \n",
            "dtypes: float64(3), int64(4), object(2)\n",
            "memory usage: 28.1+ KB\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "              mpg   cylinders  displacement       weight  acceleration  \\\n",
              "count  398.000000  398.000000    398.000000   398.000000    398.000000   \n",
              "mean    23.514573    5.454774    193.425879  2970.424623     15.568090   \n",
              "std      7.815984    1.701004    104.269838   846.841774      2.757689   \n",
              "min      9.000000    3.000000     68.000000  1613.000000      8.000000   \n",
              "25%     17.500000    4.000000    104.250000  2223.750000     13.825000   \n",
              "50%     23.000000    4.000000    148.500000  2803.500000     15.500000   \n",
              "75%     29.000000    8.000000    262.000000  3608.000000     17.175000   \n",
              "max     46.600000    8.000000    455.000000  5140.000000     24.800000   \n",
              "\n",
              "       model year      origin  \n",
              "count  398.000000  398.000000  \n",
              "mean    76.010050    1.572864  \n",
              "std      3.697627    0.802055  \n",
              "min     70.000000    1.000000  \n",
              "25%     73.000000    1.000000  \n",
              "50%     76.000000    1.000000  \n",
              "75%     79.000000    2.000000  \n",
              "max     82.000000    3.000000  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-65fe2ccf-1502-4407-a26a-ed8dbb719c2d\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>mpg</th>\n",
              "      <th>cylinders</th>\n",
              "      <th>displacement</th>\n",
              "      <th>weight</th>\n",
              "      <th>acceleration</th>\n",
              "      <th>model year</th>\n",
              "      <th>origin</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>398.000000</td>\n",
              "      <td>398.000000</td>\n",
              "      <td>398.000000</td>\n",
              "      <td>398.000000</td>\n",
              "      <td>398.000000</td>\n",
              "      <td>398.000000</td>\n",
              "      <td>398.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>23.514573</td>\n",
              "      <td>5.454774</td>\n",
              "      <td>193.425879</td>\n",
              "      <td>2970.424623</td>\n",
              "      <td>15.568090</td>\n",
              "      <td>76.010050</td>\n",
              "      <td>1.572864</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>7.815984</td>\n",
              "      <td>1.701004</td>\n",
              "      <td>104.269838</td>\n",
              "      <td>846.841774</td>\n",
              "      <td>2.757689</td>\n",
              "      <td>3.697627</td>\n",
              "      <td>0.802055</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>9.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>68.000000</td>\n",
              "      <td>1613.000000</td>\n",
              "      <td>8.000000</td>\n",
              "      <td>70.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>17.500000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>104.250000</td>\n",
              "      <td>2223.750000</td>\n",
              "      <td>13.825000</td>\n",
              "      <td>73.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>23.000000</td>\n",
              "      <td>4.000000</td>\n",
              "      <td>148.500000</td>\n",
              "      <td>2803.500000</td>\n",
              "      <td>15.500000</td>\n",
              "      <td>76.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>29.000000</td>\n",
              "      <td>8.000000</td>\n",
              "      <td>262.000000</td>\n",
              "      <td>3608.000000</td>\n",
              "      <td>17.175000</td>\n",
              "      <td>79.000000</td>\n",
              "      <td>2.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>46.600000</td>\n",
              "      <td>8.000000</td>\n",
              "      <td>455.000000</td>\n",
              "      <td>5140.000000</td>\n",
              "      <td>24.800000</td>\n",
              "      <td>82.000000</td>\n",
              "      <td>3.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-65fe2ccf-1502-4407-a26a-ed8dbb719c2d')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-65fe2ccf-1502-4407-a26a-ed8dbb719c2d button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-65fe2ccf-1502-4407-a26a-ed8dbb719c2d');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 8,\n  \"fields\": [\n    {\n      \"column\": \"mpg\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 133.37523833494922,\n        \"min\": 7.815984312565782,\n        \"max\": 398.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          23.514572864321607,\n          23.0,\n          398.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"cylinders\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 139.0071020301553,\n        \"min\": 1.7010042445332094,\n        \"max\": 398.0,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          398.0,\n          5.454773869346734,\n          8.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"displacement\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 143.57617465667641,\n        \"min\": 68.0,\n        \"max\": 455.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          193.42587939698493,\n          148.5,\n          398.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"weight\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1535.5522437115258,\n        \"min\": 398.0,\n        \"max\": 5140.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          2970.424623115578,\n          2803.5,\n          398.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"acceleration\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 135.93788360342714,\n        \"min\": 2.7576889298126757,\n        \"max\": 398.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          15.568090452261307,\n          15.5,\n          398.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"model year\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 120.24225119423292,\n        \"min\": 3.697626646732623,\n        \"max\": 398.0,\n        \"num_unique_values\": 8,\n        \"samples\": [\n          76.01005025125629,\n          76.0,\n          398.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"origin\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 140.19214256834297,\n        \"min\": 0.8020548777266163,\n        \"max\": 398.0,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          398.0,\n          1.5728643216080402,\n          3.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Jumlah nilai '?' di horsepower:\", (df['horsepower'] == '?').sum())\n",
        "\n",
        "df['horsepower'] = df['horsepower'].replace('?', np.nan)\n",
        "df['horsepower'] = pd.to_numeric(df['horsepower'])\n",
        "\n",
        "df = df.dropna(subset=['horsepower'])\n",
        "\n",
        "df = df.drop('car name', axis=1)\n",
        "\n",
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4NeXY5kBpVv5",
        "outputId": "0ee86cbd-f732-4baa-b624-3020167d603b"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Jumlah nilai '?' di horsepower: 6\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Index: 392 entries, 0 to 397\n",
            "Data columns (total 8 columns):\n",
            " #   Column        Non-Null Count  Dtype  \n",
            "---  ------        --------------  -----  \n",
            " 0   mpg           392 non-null    float64\n",
            " 1   cylinders     392 non-null    int64  \n",
            " 2   displacement  392 non-null    float64\n",
            " 3   horsepower    392 non-null    float64\n",
            " 4   weight        392 non-null    int64  \n",
            " 5   acceleration  392 non-null    float64\n",
            " 6   model year    392 non-null    int64  \n",
            " 7   origin        392 non-null    int64  \n",
            "dtypes: float64(4), int64(4)\n",
            "memory usage: 27.6 KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(8,6))\n",
        "sns.heatmap(df.corr(), annot=True, cmap='coolwarm')\n",
        "plt.title('Korelasi Antar Fitur terhadap MPG')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 624
        },
        "id": "bAuVpdBMpgj5",
        "outputId": "3db814aa-bf2f-4561-f9f8-34efb9f596a1"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x600 with 2 Axes>"
            ],
            "image/png": "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fYWPjw8ajYYffvih0M2EZWnw4MFMmTKFMWPG4ObmRo8ePe5Y387Ojm7duhX7er169QA4ffq0Wbm1tbWpXVE38QohHjyZVAthYQ8//DDr16+nd+/edO/end27d5su59ra2hISElKozfnz51Gr1XedgNeqVQsAT0/PO35xF+X333/HYDDw22+/mUUai0sZadOmDW3atOGDDz5g5cqVDB06lFWrVt3TUnhr164lKyuLRYsWFYruhoSEMG3aNPbu3cujjz56T9tS3KQ0KCiI+Ph41q5dS4cOHUzloaGh99R/WSlunDcju7f/CM7NyG15vGetWrX4888/adeuXbmfTJw6dYoLFy6wdOlShg0bZiq/GYm9qXr16kDBFZhb3f7v5Ndff0Wv17N161azKyY//PBDkWMoqs8LFy5ga2tb6ATiTqpVq0a7du0ICgri5Zdfvqe12YsSEBBAnTp1WL9+PQsXLqxQy2QKIcxJTrUQFUDXrl356aefuHTpEj179iQlJQUrKyt69OjBhg0bzJZSi46OZuXKlTz66KN3Td8IDAzE0dGR//3vf0XmO99csqsoN6OLt0Z8k5OTC01KEhMTC0WFmzVrBmB2yb0kli9fTs2aNXnppZcYMGCA2ePNN9/E3t7+vnKSb05Ebp+UFrWN2dnZfPXVV/f8HmXBzs6uUMoJFJwc3brEW15eHv/3f/9XJu8JhffNwIEDycvLY/bs2YXa5ObmlvpXLm9V1HFQFIVPP/3UrJ6Pjw/NmjVj6dKlZvtp+/btnD17tlCfKpXKLJofFhbG+vXrixzD/v37zdJHrl27xoYNG+jRo0exkfbivP/++8yYMYNXX331ntoVZ+bMmcTFxTFmzJgi/x2X5KqMEKL8SaRaiAqif//+LF68mOeff57HH3+cLVu28P7777N9+3YeffRRxo4di7W1Nd988w0Gg4F58+bdtU9HR0cWLVrEc889R/PmzRk0aBAeHh6Eh4ezadMm2rVrxxdffFFk2x49eqDVaunbty8vvvgiaWlpLF68GE9PTyIjI031li5dyldffUX//v2pVasWqampLF68GEdHRx577LESb/+NGzf4+++/GT9+fJGv63Q6AgMDWbNmDZ999pnZcm5306xZM6ysrPjwww9JTk5Gp9PRpUsXHnnkEVxcXBg+fDjjx49HpVKxbNkyi01SWrRowerVq5k4cSKt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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X = df.drop('mpg', axis=1)\n",
        "y = df['mpg']"
      ],
      "metadata": {
        "id": "m3rdvzpkpwZh"
      },
      "execution_count": 25,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
        "\n",
        "print(\"Jumlah data latih:\", X_train.shape[0])\n",
        "print(\"Jumlah data uji:\", X_test.shape[0])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FR7aNs8upx2i",
        "outputId": "3c865f76-e7a9-41a8-a32d-ed0d75d77086"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Jumlah data latih: 313\n",
            "Jumlah data uji: 79\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LinearRegression\n",
        "from sklearn.metrics import mean_squared_error, r2_score\n",
        "\n",
        "lr_model = LinearRegression()\n",
        "lr_model.fit(X_train, y_train)\n",
        "\n",
        "y_pred_lr = lr_model.predict(X_test)\n",
        "\n",
        "print(\"Linear Regression:\")\n",
        "print(\"R² Score:\", r2_score(y_test, y_pred_lr))\n",
        "print(\"RMSE:\", np.sqrt(mean_squared_error(y_test, y_pred_lr)))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QqWDy9Qap2UV",
        "outputId": "5a73071f-fa7a-432a-efba-43e4b77b21ed"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Linear Regression:\n",
            "R² Score: 0.7901500386760351\n",
            "RMSE: 3.2727457003009515\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.ensemble import RandomForestRegressor\n",
        "\n",
        "rf_model = RandomForestRegressor(n_estimators=100, random_state=42)\n",
        "rf_model.fit(X_train, y_train)\n",
        "\n",
        "y_pred_rf = rf_model.predict(X_test)\n",
        "\n",
        "print(\"Random Forest:\")\n",
        "print(\"R² Score:\", r2_score(y_test, y_pred_rf))\n",
        "print(\"RMSE:\", np.sqrt(mean_squared_error(y_test, y_pred_rf)))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JdrYin07p2Of",
        "outputId": "b24c3a63-746a-4535-db9f-122bd56b96b2"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Random Forest:\n",
            "R² Score: 0.888712085258602\n",
            "RMSE: 2.3833170321947033\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import joblib\n",
        "\n",
        "joblib.dump(rf_model, 'model_mpg.pkl')\n",
        "print(\"Model berhasil disimpan!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "L4XOHO6-p1-2",
        "outputId": "97d2eae3-b53b-4f86-ec00-a15094e6b39f"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Model berhasil disimpan!\n"
          ]
        }
      ]
    }
  ]
}
