To verify if `ActiveRecord::Base.establish_connection` has successfully established a connection to your database from the Rails console, you can use the `ActiveRecord::Base.connected?` method. This method returns `true` if the connection to the database has been established and is still open; otherwise, it returns `false`.

Here's how you can check the database connection status:

1. Open your Rails console by running `rails console` or `rails c` from your project's root directory.
2. Once in the console, check if the connection has been established by executing:

```ruby
ActiveRecord::Base.connected?
```

If the method returns `true`, it means that your application has successfully connected to the database. If it returns `false`, the application is not connected to the database.

For more detailed information about the current connection, including the database adapter being used and the connection parameters, you can inspect the `ActiveRecord::Base.connection` object. For example:

```ruby
ActiveRecord::Base.connection
```

This will print out the connection details to the console. Remember, executing `ActiveRecord::Base.connection` will also establish a connection if one is not already established, so it's also a way to initiate a connection manually.
