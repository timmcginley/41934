# Introduction to using Git

For managing our codebase, we will utilize [Git](/Concepts/GIT).
Git helps versioning (keeping track of changes) and sharing our code.

## Prerequisites

- Register an account at [GitHub](https://github.com/) if you don't already have one.
- It's recommended to install [GitHub Desktop](https://desktop.github.com/download/).
- Managers will need to have `git` in their [command line](/Concepts/CommandLine.md) environment. If you don't, [install git](https://git-scm.com/downloads).


## Create a repository

Create your own repository at GitHub using either [analyst template](https://github.com/timmcginley/BIManalyst_g_xy) if you are an analyst, or [manager template](https://github.com/timmcginley/BIMmanager_g_xy) if you are a manager.

Each group should only have _one repository_. Remaining group members shall be added as collaborators for the repository.

Please respect the naming convention for the repositories according to the templates.

```{figure} img/GitHub-template-button.png
:width: 500
:alt: GitHub template button

Create a new repository using GitHub template.
```

```{warning}
Only one group member should do this!
```

## Clone your repository to your local machine and do your first commit!

Using GitHub Desktop, clone the newly created repository to access it through your local machine.

Open `README.md` in your text editor of choice, and edit the document heading to match your group number.
Save the file, and head to GitHub Desktop.

In GitHub Desktop, select the changed file and commit it.
It's good practice to provide useful commit messages such as "Updated heading to match group number", that describe the change.

Only one group member should alter the group number and commit.
Remaining group members should use the "fetch origin" button to fetch the changes that has just been made.

Verify that remaining group members have the changes to the `README.md` file on their machines.


## For managers

Managers has to collect the code from multiple analyst repositories into their own repository.
This may be achived through [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

TODO: Add instruction for git submodules...



