prepare-commit-msg
==================

Yet another tool for the `prepare-commit-msg` git hook. To use with **pre-commit**

For pre-commit: see https://github.com/pre-commit/pre-commit

## What's all about

In many projects some sort of ticket system is used. The commit messages are used for updating the status of the ticket by "linking" the ticket name, which it is nothing more than mentioning the ticket name, in the commit message.

This allows for using a jinja2 template for formatting your commit message.

You can configure this with the following commandline options:
- `-t` / `--template ` - absolute path to the template. Default value:
  name of bundled template: `prepare_commit_msg_append.j2` file
- `-b` / `--branch` - may be specified multiple times to exclude branches
  from formatting the commit message. Default values: `main, master`
- `-p` / `--pattern` - may be specified multiple times to include branches
  for formatting the commit message. Default value: `(?<=feature/).*`

## Usage

```yaml
# .pre-commit-config.yaml file
default_install_hook_types:
  - pre-commit
  - prepare-commit-msg
repos:
  - repo: https://github.com/davidmpaz/prepare-commit-msg
    rev: v0.0.1
    hooks:
      - id: prepare-commit-msg
        name: Prepare Commit Message
        description: Add a message template to the commit message.
        stages: [ prepare-commit-msg ]
        args: [ # args can be omitted, sensible default values are provided
          -t, prepare_commit_msg_prepend.j2,
          -b, main, -b, master, -b, test, -b develop,
          -p, '(?<=feature/).*', -p, '(?<=release/).*'
        ]
```

or if having the package installed via pip:

```yaml
# .pre-commit-config.yaml file
default_install_hook_types:
  - pre-commit
  - prepare-commit-msg
repos:
  - repo: local
    hooks:
      - id: prepare-commit-msg
        name: Prepare Commit Message
        description: Add a message template to the commit message.
        stages: [ prepare-commit-msg ]
        entry: prepare-commit-msg
        args: [ # args can be omitted, sensible default values are provided
          -t, prepare_commit_msg_prepend.j2,
          -b, main, -b, master, -b, test, -b develop,
          -p, '(?<=feature/).*', -p, '(?<=release/).*'
        ]
```

## Templating

Some example can be seen in package:

```
{{ original | join('') | trim() }}

Relates: #{{ ticket }}

{{ rest | join('') }}
```

The variables passed currently to templates are:
* ticket: matched part of the patterns given as parameter
* original: recognised original message, if any
* rest: rest of the prepared commit file presented by git, removing `original`
* full: complete prepared commit file presented by git
