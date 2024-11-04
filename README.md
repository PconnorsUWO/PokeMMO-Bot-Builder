
# PokeMMO-Bot-Builder

PokeMMO-Bot-Builder is a flexible, user-friendly tool that enables you to create custom scripts for the popular online game [PokeMMO](https://pokemmo.eu). With this bot builder, you can design, customize, and automate specific actions in PokeMMO, enhancing your gameplay experience.

## Features

- **Script Builder:** Easily create scripts to automate various actions within PokeMMO.
- **User-Friendly Interface:** Simple and intuitive interface for script creation.
- **Customizable Commands:** Set up unique sequences and behaviors tailored to your in-game goals.
- **Modular Design:** Add, edit, or remove commands with minimal effort.
- **Error Handling:** Built-in error handling for smoother operation and troubleshooting.

## Getting Started

### Prerequisites

To use PokeMMO-Bot-Builder, ensure you have:

- Python 3.8+
- PokeMMO client
- Necessary dependencies (listed in `requirements.txt`)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/pconnorsUWO/PokeMMO-Bot-Builder.git
   ```

2. Navigate to the project folder:

   ```bash
   cd PokeMMO-Bot-Builder
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Open the bot builder interface:** Run the main script to start the bot builder.

   ```bash
   python main.py
   ```

2. **Create a new script:** Follow the prompts to set up your script’s actions, delays, and conditions.

3. **Save and execute:** Once configured, save your script and run it within PokeMMO.

## Script Example

Here’s a basic example of a PokeMMO script:

```python
from bot_builder import PokeScript

script = PokeScript()
script.add_action('move', direction='up', duration=2)
script.add_action('interact', target='npc')
script.add_action('attack', move='Thunderbolt')
script.run()
```

## Contributing

Contributions are welcome! Feel free to open issues for bugs, feature requests, or general feedback. If you'd like to contribute code, please fork the repository and submit a pull request.

## Disclaimer

This bot builder is intended for educational and personal use only. Use of automated scripts may violate PokeMMO’s terms of service and result in account penalties. Use at your own risk.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
