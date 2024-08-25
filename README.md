# copyclipboard

`copyclipboard` is a command-line tool that allows you to copy the structure of a folder and the contents of specific file types to your clipboard. This can be especially useful when working with repositories and sharing the structure and code with LLM interfaces like ChatGPT.

## Installation
You must have `tree` installed on your system. on mac you can install with `brew install tree` and on ubuntu you can install with `sudo apt-get install tree` (if it's not already installed).
To install `copyclipboard`, simply run:

```bash
pip install copyclipboard
```

## Usage

Once installed, you can use the copyclipboard command in your terminal.

### Copy All File Types
By default, the tool will copy the structure and contents of all files in your repository:

```bash
copyclipboard
```

### Copy Specific File Types
You can specify the file types you want to copy using the --extensions option:

```bash
copyclipboard --extensions .py .yaml
```

This will also update your configuration file in ~/.copyclipboard_config with the specified extensions.

### Manual Configuration
If you prefer, you can manually edit the configuration file located at `~/.copyclipboard_config` to specify which file types should be copied.


