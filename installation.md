




#### Import csv file to mongo db 6.0 community

Sourace: 
```
https://www.mongodb.com/docs/database-tools/mongoimport/#examples
```

```mongoimport --db=users --collection=contacts --type=csv \
   --columnsHaveTypes \
   --fields="name.string(),birthdate.date(2006-01-02),contacted.boolean(),followerCount.int32(),thumbnail.binary(base64)" \
   --file=/example/file.csv
```

