## Maintenance

Code may need fixing. If you have found a bug in a large system, you need strategies and tactics to let you read the code at increasing levels of detail until you have found the problem. Use tools such as the debugger, the compiler's warnings or symbolic code output, a system call tracer, your database's Structured Query Language (SQL) logging facility, packet dump tools to locate a bug's location.

Examine the code from the problem manifestation to the source of the problem. Follow only the related paths. Use debugger's stack trace, single stepps and breakpoints to narrow down the search.

Add print statements in strategic locations of the execution path. For OS interfaces, system call tracing is useful.