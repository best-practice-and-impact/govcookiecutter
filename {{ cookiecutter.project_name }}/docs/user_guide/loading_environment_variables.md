# Loading environment variables

We use [`python-dotenv`][python-dotenv] to load environment variables, as these are only loaded when
inside the project folder. This can prevent accidental conflicts with identically named
variables. Alternatively you can use [`direnv` to load environment variables][direnv] if
you meet [certain conditions](#installing-direnv).

## Using `python-dotenv`

To load the environment variables, first make sure you have
python-dotenv install, and [make sure you have a `.secrets` file to store
secrets and credentials](#storing-secrets-and-credentials). Then to load in the
environment variables into a python script see instructions in `.env` file.

## Using `direnv`

To load the environment variables, first [follow the `direnv` installation
instructions](#installing-direnv), and [make sure you have a `.secrets` file to store
secrets and credentials](#storing-secrets-and-credentials). Then:

1. Open your terminal;
2. Navigate to the project folder; and
   - You should see the following message:
     ```shell
     direnv: error .envrc is blocked. Run `direnv allow` to approve its content.
     ```
3. Allow `direnv`.
   ```shell
   direnv allow
   ```

You only need to do this once, and again each time `.envrc` and `.secrets` are modified.

### Installing `direnv`

These instructions assume you are running on macOS with administrator privileges using
a bash terminal. For other ways of installing `direnv`, and its shell hooks, consult
the `direnv` documentation.

1. Open your terminal;
2. [Install `direnv` using Homebrew][homebrew];
   ```shell
   brew install direnv
   ```
3. Add the shell hooks to your `.bash_profile`;
   ```shell
   echo 'eval "$(direnv hook bash)"' >> ~/.bash_profile
   ```
4. Check that the shell hooks have been added correctly; and
   ```shell
   cat ~/.bash_profile
   ```
   - This should display `eval "$(direnv hook bash)"`
5. Restart your terminal.

## Storing secrets and credentials

Secrets and credentials must be stored in the `.secrets` file. This file is not
version-controlled, so no secrets should be committed to GitHub.

In your terminal navigate to the root folder, and create a `.secrets` file.

```shell
touch .secrets
```

Open this new `.secrets` file using your preferred text editor, and add any secrets as
environmental variables. For example, to add a JSON credentials file for Google
BigQuery, save the following changes to `.secrets`.

```shell
GOOGLE_APPLICATION_CREDENTIALS="path/to/credentials.json"
```

Once complete, load the `.secrets` file using:

```shell
from dotenv import load_dotenv
import os

#Load secrets from the `.secrets` file, overriding any system environment variables
load_dotenv(".secrets", override=True)
#Example variable
EXAMPLE_VARIABLE = os.getenv("EXAMPLE_VARIABLE")
```

## Further Reading

For more information on virtual environments, please visit: (https://saurabh-kumar.com/python-dotenv/)

[python-dotenv]: https://saurabh-kumar.com/python-dotenv/
[direnv]: https://direnv.net/
[homebrew]: https://brew.sh/
[env]: https://github.com/best-practice-and-impact/govcookiecutter/%7B%7B%20cookiecutter.repo_name%20%7D%7D/.env
