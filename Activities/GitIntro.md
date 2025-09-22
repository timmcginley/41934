# Introduction to using Git

For managing our codebase, we will utilize [Git](/Concepts/GIT.md).
Git helps versioning (keeping track of changes) and sharing our code.


```{Important}
If you have no prior experience with git, watch the following two videos:
- [How git works](https://www.youtube.com/watch?v=e9lnsKot_SQ)
- [Introduction to git and GitHub](https://www.youtube.com/watch?v=Oaj3RBIoGFc)

**Please watch both videos carefully before asking git related questions.**
```

## Prerequisites

- Register an account at [GitHub](https://github.com/) if you don't already have one.
- It's recommended to install [GitHub Desktop](https://desktop.github.com/download/).
- Managers will need to have `git` in their [command line](/Concepts/CommandLine.md) environment. If you don't, [install git](https://git-scm.com/downloads).


## Create a repository

Create your own repository at GitHub using either [analyst template](https://github.com/timmcginley/BIManalyst_g_xy) if you are an analyst, or [manager template](https://github.com/timmcginley/BIMmanager_g_xy) if you are a manager.

Each group should only have _one repository_. Remaining group members shall be added as collaborators for the repository.

Please respect the naming convention for the repositories according to the templates.

```{figure} img/GitHub-template-button.png
:width: 800
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

```{Tip}
It's good practice to commit often, thus keeping the changes contained in a single commit fairly low.
The changes should be able to be summarized in a few words.
```

```{Tip}
Changes containing code that does not work yet, should *not* be committed to the [main branch](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell).
This is to avoid having managers and other team members pull broken code to their own systems.

In other words, the main branch should be kept "clean".
```


## For managers

Managers has to collect the code from multiple analyst repositories into their own repository.
This may be achived through [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

### Add a submodule

For a consistent and structured organization of submodules, they should live within the `./external/` directory.

Open up the command line in the root of your repository, then enter the `./external/` directory:

```console
./$ cd external
```

Identify which analysts you need, and gather the web URL for their repositories.

```{figure} img/GitHub-submodule-link.png
:width: 800
:alt: GitHub repository link

Copy web URL of an analyst repository.
```

Next, add the analyst repository as a submodule to your own repository:

```console
./external$ git submodule add -b main https://github.com/timmcginley/BIManalyst_g_xy.git
```

Open up GitHub Desktop and identify the yet to be committed changes.
If there were no changes beforehand, there should be exactly two changes:

```{figure} img/GitHub-submodule-commit.png
:width: 800
:alt: Changes after adding submodule

Changes after adding submodule.
```

Make a commit containing the changes. Remember to craft a short descriptive commit summary.
After committing, press the "Push origin" button.

Open up your web-browser and head to your own repository.
Verify that the just added submodule is present in the `./external/` directory.

In `./external/BIManalyst_g_xy/` code of the analsyt should now be present.


**The above steps** should be repeated for each analyst repository that you desire to utilize.


### Pulling changes from submodules

On the web, go to your repository and enter the `./external/` directory.

The name of each submodule that you have added should be visible followed by `@` and a 7-character hexadecimal string.
This is the commit-hash that the submodule points to.

Click the name to enter the analyst repository.
Watch the button right under the repository name. This button will display the commit-hash.
This means that you are browsing the repository with all the changes leading up to that specific commit.
If there are more recent commits, these changes will not be visible.

To view the latest version of the repository, click the button and select main.

If the repository has any changes and you wish to fetch them to your own repository, you should update the submodule to point to the most recent commit.

In the command line, enter the submodule directory and pull changes:

```console
./$ cd external/BIManalyst_g_xy
./external/BIManalyst_g_xy/$ git pull origin main
```

To update all submodules at once:
```console
./$ git submodule update --rebase --remote --recursive
```

In GitHub Desktop, observe that each updated submodule has a message that the submodule changed its commit from one to another.

Finish by committing the updated submodules and push to origin.


