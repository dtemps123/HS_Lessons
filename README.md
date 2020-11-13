# HS_Lessons
Lessons for the Hinsdale HS Summer Students 2019, 2020.
Requirements:
- Git
- Python 3 (preferably Anaconda)
- Jupyter (included by default with Anaconda)

To "clone" this git repository, open a terminal, and navigate to where you would like to create a new folder using `cd`. Then run the following:
`git clone -b master_unanswered git@github.com:dtemps123/HS_Lessons.git`
This should create a new folder and copy the code over. Git is installed by default on Mac/Linux. If you cannot get git to work, you can download a zip archive of the repository using the webpage. Once you have the code cloned, do the following.

## On UNIX
Move into the cloned directory (the following line assumes you are still in the directory where you issued the clone command):
`cd HS_Lessons`
Now, you'll want to create your own branch (replace `new_branch_name` with whatever yuo'd like):
`git checkout -b new_branch_name`
Then start a jupyter notebook session (assuming you have Anaconda/jupyter installed)
`jupyter notebook`
Go to the web browser that opens, and begin working on your code.

## On Windows
Lame.
Open the start menu, and type "Anaconda Navigator" then click on the Jupyter icon, use the menus to navigate to where you cloned the repository.
Alternatively, open the "Anaconda Prompt" from the start menu, `cd` to the cloned repository's directory, then type `jupyter notebook`.
