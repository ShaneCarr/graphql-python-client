# Yammer Graph demo
This is a an demo application to call yammer/viva apis. 

## install and configure
```bash
brew install pyenv
pyenv install 3.11
echo 'export PATH="$(pyenv root)/bin:$PATH"' >> ~/.zshrc
export PATH="$(pyenv root)/bin:$PATH"
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

## create virtual enviornment
python -m venv .cdx
source .cdx/bin/activate
pip install gql


 
## run application
get a token from graph
````
```bash
python main.py
```
