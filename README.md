# Automações Web com Python

### Integrações disponíveis

1. Spotify

### Uso

```python

from data import SPOTIFY

autobot = AutoBot(browser = 'chrome', data = SPOTIFY)

autobot.__choose_browser_and_login__()

autobot.__select_image_click__(function = 'search')

autobot.__write__('marília mendonça bin')

```
