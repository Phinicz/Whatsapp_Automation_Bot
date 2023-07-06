# WELCOME TO WHATSAPP AUTOMESSAGE BOT

This bot will send a message to whatever number of phones you put in the data.json file

## Installation
Download this repository from the green code button, after unzipping the file drag and drop it into vs code press CTRL + SHIFT + ~ OR Terminal -> new Terminal

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install WhatsApp_AutoMessage_Bot dependencies.

```bash
pip install -r requirements.txt
```

## Usage

```bash
py main.py
````
OR 
```bash
python main.py
```
Download Google Chrome and set it as the default browser as the Bot assumes that Google chrome is the default browser or change it your default browser here
##### main.py
```python
subprocess.call("TASKKILL /f  /IM  CHROME.EXE") 
#change CHROME.EXE TO : 
#To MSEDGE.EXE if you have edge as the default browser
#To FIREFOX.EXE if you have firefox as your default browser
```
## Phone Numbers
edit the data.json file to put the numbers you want to send to you only need to fill the website attribute and the phone attribute in each entry in the data file you can ignore any other attribute 
## Discussion
Join the Discussion Chat to ask any question you have in mind
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
