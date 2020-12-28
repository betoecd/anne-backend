db.createUser({
    user : "mongodb-admin",
    pwd : "mongodb-admin",
    roles : [
        {
            role : "readWrite",
            db : "anne-backend"
        }
    ]
})
