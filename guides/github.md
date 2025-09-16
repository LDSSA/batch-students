# Setup _Git_ and _GitHub_

Having a _GitHub_ account and knowing the basics of committing and pushing changes are **mandatory** for this academy. All the learning materials and exercises will be released in this repository. If you need a refresher on Git, check out the learning units 3 and 6 in our [Python prep course](https://github.com/LDSSA/ds-prep-course-2024).

With this guide, you will set up GitHub, then create and clone your workspace repository and clone the learning material repository (this one).

To set up GitHub, follow these steps:

1. If you don't have a _GitHub_ account, [Sign up](https://github.com/join) for _GitHub_.

If you have a _GitHub_ account but git is not set up in your system, complete the following steps:

1. [Checking for existing SSH keys](https://help.github.com/en/github/authenticating-to-github/checking-for-existing-ssh-keys)
1. [Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
1. [Adding a new SSH key to your GitHub account](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)
1. [Testing your SSH connection](https://help.github.com/en/github/authenticating-to-github/testing-your-ssh-connection)

### 1. Set Up Your Workspace Repository

The workspace directory/repository is where you will place everything you are working on, solve exercises, make changes to files, etc. In this academy that **is a requirement** as it is how you will make your work available to us.

#### 1.1 Create the Workspace Repository

1. Log into _GitHub_
1. Create a new **private** _GitHub_ repository called *batch9-workspace*, see
[Creating a new repository](https://help.github.com/en/articles/creating-a-new-repository).
:warning: The repo **MUST** be named *batch9-workspace*! 
If you name it anything else, you will be unable to submit any of your work for grading.

    1. You need to explicitly select **Private** - This is your work and you will be graded on it, so it should not be open to the world while you are working on it.
    1. Initialize with a README.
    This is mostly just so that you don't initialize an empty repo.
    1. Add a Python `.gitignore`. :warning:
    **This step is insanely important.** If you don't do this, you may check files into the repo that can break the grading process and you will not get any points for your work.

![Create Repository](../media/create_repository.png "Create Repository")

#### 1.2 Add a Deploy Key to your Repository

Since your repository is private you will have to explicitly give access to our grading system so that it can fetch material from the repository.
To do this, you need to add a deploy key to your repository, which we
provide to you in our [_Portal_](https://portal.lisbondatascience.org/).

1. Go to the [_Portal_](https://portal.lisbondatascience.org/)
1. Log in with your account
1. Go to your [profile](https://portal.lisbondatascience.org/users/info/) and
copy the deploy key including the `ssh-rsa` part.
![Profile](../media/profile.png "Profile")
1. Go back to the repository you have just created
1. Go to `Settings > Deploy Keys`
1. Click "Add deploy key" (no need to grant Write Access)
1. Give it a recognizable name like "grader" and paste the key from the
_Portal_
![Deploy keys](../media/deploy_key.png "Deploy key")

#### 1.3 Add your Slack ID to the Portal

As you're already in the portal, please add your SlackID to your profile. In your **Profile** in the **Portal**, besides your *GitHub Handle*, you should add your **SlackID**. You can find information on how to find it [following this link](https://moshfeu.medium.com/how-to-find-my-member-id-in-slack-workspace-d4bba942e38c)

#### 1.3 Clone Your Workspace Repository

1. Open a Terminal or Git Bash. The next steps are on this terminal.
1. Clone your `<username>/batch9-workspace` repository. If you're not sure where to put the repository, you can create a `~/projects` folder, and clone it there.

1. If you have your [**ssh keys set up**](#Setup-Git-and-GitHub) as instructed (replace `<username>` with your GitHub username):

```bash
git clone git@github.com:<username>/batch9-workspace.git
```

If for some reason you don't have the ssh key, do:

```bash
git clone https://github.com/<username>/batch9-workspace.git
```

### 2. Get the Learning Material

Now you will clone the [batch-students](https://github.com/LDSSA/batch-students)
repository. All the learning material will be made available on this repo
as the academy progresses.

1. Open a Terminal or Git Bash, the next steps are on this terminal
1. Clone the students repository
[batch-students](https://github.com/LDSSA/batch-students)

```bash
git clone git@github.com:LDSSA/batch-students.git
```

Or if you don't have the ssh keys set up:

```bash
git clone https://github.com/LDSSA/batch-students.git

```

Your repo setup is ready now.
