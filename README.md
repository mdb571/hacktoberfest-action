<div align="center"><img  src="https://hacktoberfest.digitalocean.com/assets/h-dark-d1a5f262f5aa5936d3bc526365938d98f3946e669f6e2cd9ae1e7a848c57e351.svg" width=100 height=100></img></div>
<h1 align="center">Hacktoberfest Github Action :zap:</h1>

Celebrate this festival of opensource by using the hacktoberfest github action which automatically labels all issues with ```hacktoberfest``` label in the month of october and automatically removes the label at the end of october.

## Usage

Add the following workflow to your project and forget the rest!The action adds labels only in the month of October :rocket:

```name:  Hacktoberfest Issue Labeler
on:
  issues:
    types: [opened,labeled]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: hacktoberfest-action
        uses: mdb571/hacktoberfest-action@master
        env:
          LABEL_COLOR: ${{ secrets.LABEL_COLOR }}
          LABEL_FILTER: ${{secrets.LABEL_FILTER}} 
```
 ## Secrets
 
 Add the following secrets to your repo to customize the action for labelling issues with a filter label and you can also change the label color.
 
 SECRET          | Purpose                                              | 
------------------|-------------------------------------------------------|
LABEL_COLOR     | The hex code of the label color          | 
LABLE_FILTER    | Adds label only to the issues having this filter       | 

## Contributions
Feel free to contribute and making this action do much more :heart: Star this repo if you find this helped you :star:
