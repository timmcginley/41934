# Git, Github and Github Desktop

*Git solves the problem of effectively tracking and managing changes in source code and facilitating collaborative software development among multiple contributors.*

**Git** is a free and open-source **distributed version control** system created by Linus Torvalds in 2005 to make collaborative development of the Linux kernel easier. At its most basic, a version control system tracks changes made to your files. It allows you to go back in time and see what changes were made, who made them, and when they were made. This is really helpful if you're working on a big project with other people or if you want to make sure you don't lose any important work. 

A **distributed version control** system just means that in stead of having just one copy of all the files online that everybody tries to acces and change at the same time (think of Microsoft Teams or Google Drive), every contributor has a local copy on their own computer and only synchronises it with others once in a while. This has a lot of advantages from being much faster, allowing offline and parallel work to being much better protected against data loss or server failures.

Here is a 2min video explaining [Git](https://www.youtube.com/watch?v=2ReR1YJrNOM).

Git is normally used without a GUI (graphical user interface) through the command line. Git is often used in combination with a code hosting platform, either commercial solutions such as GitHub, SourceForge, Bitbucket or GitLab, but also self-hosted options exist, like Gitea or Forgejo. 

*These platforms solve the problem of providing a centralised and user-friendly platform for hosting, collaborating on, and managing Git repositories, streamlining the development and collaboration process.*

The most popular code-hosting platform based on Git is the Microsoft-owned **GitHub**. Apart from providing the version control features of Git, Github provides features that make collaboration on projects easier, like bug tracking, task management, continuous integration, wikis etc. To further test its possibilities we use it in this course to host all our course documentation.

Usually, software developers use the command line to interact with git repositories. However, if learning Git commands and the command line is too daunting in the beginning, Github has made a GUI platform for this purpose, called **GitHub Desktop**. With GitHub Desktop you won't be able to use advanced features of Git, but it can help beginners visualise the steps of pushing and pulling repositories. Watch [this video](https://www.youtube.com/watch?v=8Dd7KRpKeaE) for an introduction to Github Desktop. 

You can also perform some basic things like committing new files directly on the Github webpage, which should be enough for the purposes of this course.

Github allows single files of up to 100mb, so most of the time it wouldn't be enough to share big native BIM files from programs like Revit. Badly exported IFC files can also sometimes have prohibitively large file sizes because of inefficient geometry. Native IFC files are typically much smaller than that, but if they became too large, a good modeller would look into strategies for lowering model size by f.ex. breaking it down into different disciplines. Read more about dealing with large models [here](https://blenderbim.org/docs/users/dealing_with_large_models.html).  Because IFC files come in human-readable text file formats (the most popular, .ifc,  being a STEP format), they are a perfect fit for version control with Git. Therefore BlenderBIM now includes [IFC Git](https://blenderbim.org/docs/users/git_support.html), a tool to track, merge and review changes, create forks and branches of your model and visually shows the geometry changed all inside Blender. 

**Get a Github account**, (at least one per team). This will make it possible to host your code on Github and make it easier for us to provide you support and also get feedback and help from your peers. Ultimately we are trying to build a strong community of OpenBIM learning at DTU and this is a great way to do it. 😊
