## Step 1: Hello Copilot

Welcome to your **"Getting Started with GitHub Copilot"** exercise! :robot:

In this exercise, you will be using different GitHub Copilot features to work on a website that allows students of Mergington High School to sign up for extracurricular activities. 🎻 ⚽️ ♟️

<img width="600" alt="screenshot of Mergington High School WebApp" src="../images/mergington-high-school-webapp.png" />

### 📖 Theory: Getting to know GitHub Copilot

<img width="150" align="right" alt="copilot logo" src="../images/copilot-logo.png" />

GitHub Copilot is an AI coding assistant that helps you write code faster and with less effort, allowing you to focus more energy on problem solving and collaboration.

GitHub Copilot has been proven to increase developer productivity and accelerate the pace of software development. For more information, see [Research: quantifying GitHub Copilot’s impact on developer productivity and happiness in the GitHub blog.](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)

As you work in your IDE, you'll most often interact with GitHub Copilot in the following ways:

| Interaction Mode          | 📝 Description                                                                                                                 | 🎯 Best For                                                                                                     |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| **⚡ Inline suggestions** | AI-powered code suggestions that appear as you type, offering context-aware completions from single lines to entire functions. | Completion of the current line, sometimes a whole new block of code                                             |
| **💭 Inline Chat**        | Interactive chat scoped to your current file or selection. Ask questions about specific code blocks.                           | Code explanations, debugging specific functions, targeted improvements                                          |
| **💬 Ask Mode**           | Optimized for answering questions about your codebase, coding, and general technology concepts.                                | Understanding how code works, brainstorming ideas, asking questions                                             |
| **🤖 Agent Mode**         | Recommended default mode for most coding tasks: autonomous edits, tool use, and follow-through until the task is done.         | Daily coding tasks, from scoped fixes to larger multi-file implementation work                                   |
| **🧭 Plan Agent**         | Optimized for drafting a plan and asking clarifying questions before any code changes are made.                                | When you want a reviewed plan first, then hand off to implementation                                            |

As you work, you'll find GitHub Copilot can help out in several places across the `github.com` website and in your favorite coding environments such as VS Code, Jet Brains, and Xcode!

For today's coding, we will practise with VS Code using your own fork of this prepared workshop repository.

> [!TIP]
> You can learn more about current and upcoming features in the [GitHub Copilot Features](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features) documentation.

### :keyboard: Activity: Get a project intro from Copilot Chat

Let's start up our development environment, use Copilot to learn a bit about the project, and then give it a test run.

1. Fork this repository to your own GitHub account.

   Do not create branches or commit directly in the original `martinpolivka` repository. All workshop changes should be made in a branch in your fork, then submitted back with a pull request.

1. Clone your fork to your machine.

   ```bash
   # Clone your fork of the prepared workshop repository and enter its folder.
   git clone https://github.com/<your-github-username>/skills-getting-started-with-github-copilot.git
   cd skills-getting-started-with-github-copilot
   ```

1. Open the cloned repository in VS Code.

1. In the left sidebar, click the extensions tab and verify that the `GitHub Copilot` and `Python` extensions are installed and enabled.

   <img width="350" alt="copilot extension for VS Code" src="../images/copilot-extension-vscode.png" />

   <img width="350" alt="python extension for VS Code" src="../images/python-extension-vscode.png" />

1. At the top of VS Code, locate and click the **Toggle Chat icon** to open a Copilot Chat side panel.

   <img width="150" alt="image" src="../images/toggle-chat-icon.png" />

   > 🪧 **Note:** If this is your first time using GitHub Copilot, you will need to accept the usage terms to continue.

1. Make sure you are in **Ask Mode** for our first interaction

   <img width="350" alt="screenshot showing Ask Mode selection in Copilot Chat" src="../images/ask-mode-selection.png" />

1. Enter the below prompt to ask Copilot to introduce you to the project.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Please briefly explain the structure of this project.
   > What should I do to run it?
   > ```

   > 🪧 **Note:** It is not necessary to follow Copilot's recommended instructions. We have already prepared the environment for you.

1. Now that we know a bit more about the project, let's actually try running it! In the left sidebar, select the `Run and Debug` tab and then press the **Start Debugging** icon.

   <img width="300" alt="image" src="../images/run-and-debug-tab.png" />

1. We want to see our webpage running in a browser, so let's find the url and port. If it isn't visible, expand the lower panel and select the **Ports** tab.

1. In the list, find port `8000` and the related link. Hover over the link and select the **Open in browser** icon.

   ![image](../images/open-in-browser-icon.png)

### :keyboard: Activity: Use Copilot to help remember a terminal command 🙋

Great work! Now that we are familiar with the app and we know it works, let's ask Copilot for help starting a branch so we can do some customising.

1. In VS Code's bottom panel, select the **Terminal** tab and on the right side click the plus `+` sign to create a new terminal window.

   > 🪧 **Note:** This will avoid stopping the existing debug session that is hosting our web application service.

1. Within the new terminal window use the keyboard shortcut `Ctrl + I` (windows) or `Cmd + I` (mac) to bring up **Copilot's Terminal Inline Chat**.

1. Let's ask Copilot to help us remember a command we have forgotten: creating a branch in our fork and publishing it.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Hey Copilot, how can I create and publish a new Git branch called "participant/<your-name>" in my fork?
   > ```

   Replace `<your-name>` with your own name or GitHub username before running the command.

   > 💡 **Tip:** If Copilot doesn't give you quite what you want, you can always continue explaining what you need. Copilot will remember the conversation history for follow-up responses.

1. Press the `Run` button to let Copilot insert the terminal command for us. No need to copy and paste!

1. After a moment, look in the VS Code lower status bar, on the left, to see the active branch. It should now say `participant/<your-name>`. If so, you are all done with this step!

<details>
<summary>Having trouble? 🤷</summary><br/>

If you don't get feedback, here are some things to check:

- Make sure you created a branch named `participant/<your-name>` and replaced `<your-name>` with your own name or GitHub username.
- Make sure the branch was published to your fork, not to the original `martinpolivka` repository.

</details>

---

### Navigation

- [Back to README](../../README.md)
- Next: [Step 2](2-step.md)
