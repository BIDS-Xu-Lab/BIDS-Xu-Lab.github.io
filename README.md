# Lab Website

# Development

Once all dependent packages are installed, run `pelican -r -l` to start a development server for testing.

# Deployment

To deploy the generated static site on GitHub Pages, the following steps should be followed:

1. Enable workflow permissions. In "Settings / Action / General", ensure the "Workflow permissions" is set to "Read and write permissions".
2. Enable GitHub Action and add a new workflow `main.yml`. 
   Copy the following content to create the workflow action. 
   It will take a few minutes to run. Once it shows completed without any error in the Action, you can move next step.
3. Enable the GitHub Pages. In "Settings / Pages", select:
    - Source: Deploy from a branch
    - Branch: gh-pages, /(root)

If everything works fine, you can find the `gh-pages` branch has been deployed on GitHub Pages and you can access it.

```yaml
# This is a basic workflow to help you get started with Actions

name: Deploy Latest Pages by Pelican

# Controls when the workflow will run
on:
  # Triggers the workflow on push or pull request events but only for the "main" branch
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v3

      # Runs a single command using the runners shell
      - name: Run a one-line script
        run: echo Hello, Pelican!
          
      # Runs a build for pelican
      - name: GitHub Pages Pelican Build Action
        uses: nelsonjchen/gh-pages-pelican-action@0.1.10
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

```