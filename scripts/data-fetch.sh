rm -rf ./data/*
kaggle datasets download -d adaoduque/campeonato-brasileiro-de-futebol
unzip campeonato-brasileiro-de-futebol.zip -d ./data
rm campeonato-brasileiro-de-futebol.zip
