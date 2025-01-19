# HtmlPythonLoggerFormatter

HTML Details Logger is a Python-based logging utility that generates detailed HTML-formatted log outputs. It extends the standard Python logging module to provide rich, collapsible log entries with context information and stack traces.

## Features

- HTML-formatted log outputs with collapsible details
- Captures local context (variables and arguments) of the logged function
- Includes full stack trace for each log entry
- Configurable log levels and output destinations

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/html-details-logger.git
cd html-details-logger
```

## Usage

1. Import the HTMLDetailsFormatter:

```python
from html_logger import HTMLDetailsFormatter
```

2. Initialize the logger:

```python
HTMLDetailsFormatter.initLogger(output='logs/errors.html', log_level=logging.ERROR)
```

3. Use the logger in your code:

```python
logger = logging.getLogger('html_details_logger')
logger.error("Message for ERROR")
```

## Example

```python
from html_logger import HTMLDetailsFormatter
import logging

# Setup HTML logger for errors
HTMLDetailsFormatter.initLogger(output='logs/errors.html')

# Setup plain text logger for other levels
logger = logging.getLogger('html_details_logger')
info_handler = logging.FileHandler('info.log', mode='w', encoding='utf-8')
info_handler.setLevel(logging.INFO)
info_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
info_handler.setFormatter(info_formatter)
logger.addHandler(info_handler)

# Example output
logger.debug("Message for DEBUG")
logger.info("Message for INFO")
logger.error("Message for ERROR")
```

## Requirements

- Python 3.x


## License

The HtmlPythonLoggerFormatter is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
