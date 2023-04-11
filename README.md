[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://lucasmccabe-emailgpt-app-jspyxu.streamlit.app/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![GitHub Repo stars](https://img.shields.io/github/stars/lucasmccabe/emailGPT?style=social)

# emailGPT

`emailGPT` is a quick and easy interface to generate emails with [ChatGPT](https://openai.com/blog/chatgpt/). 
This fork use OpenAI API directly instead of using revChatGPT.


<img src="assets/lazy_email.png" alt="drawing" width="200"/>

## Table of Contents
* [Table of Contents](#table-of-contents)
* [Examples](#examples)
* [Usage](#usage)
* [Installation](#installation)
* [Contact](#contact)
* [License](#license)


## Examples

<img src="assets/vader.png" alt="vader" width="500"/>
<br><br>

<img src="assets/pooh.png" alt="pooh" width="500"/>
<br><br>

<img src="assets/coyote.png" alt="coyote" width="500"/>


## Usage

`emailGPT` is deployed as a `Streamlit` app. It is available [here](https://lucasmccabe-emailgpt-app-jspyxu.streamlit.app/).

## Installation


1. Install requirements:
```bash
pip install -r requirements.txt
```
2. Export API KEY 

Generate your API KEY using platform.openai.com and make it our environment variable 

```
export OPENAI_API_KEY=<YOUR-OPENAI-API-KEY> 
```

3. Run streamlit on your local machine 

```
streamlit run app.py

```


## Contact

Questions? Reach out:
- Lucas ([email](mailto:lucasmccabe@gwu.edu))

## License
[MIT](https://choosealicense.com/licenses/mit/)
